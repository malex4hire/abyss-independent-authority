package com.abyss.authority;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public final class AuthorityDemo {
    private AuthorityDemo() {}

    public static void main(String[] args) {
        if (args.length != 9) {
            System.err.println("Expected: framework principal capability artifact tests score digest approval budget");
            System.exit(2);
        }

        DeploymentRequest request = new DeploymentRequest(
                args[0], args[1], args[2], args[3], Boolean.parseBoolean(args[4]),
                Double.parseDouble(args[5]), args[6], args[7], Integer.parseInt(args[8]));
        Decision decision = new AuthorityEngine().evaluate(request);
        System.out.println(decision.toJson());
    }
}

record DeploymentRequest(
        String framework,
        String principal,
        String capability,
        String artifact,
        boolean testsPassed,
        double evaluationScore,
        String artifactDigest,
        String approvalId,
        int requestedBudgetDollars) {}

record Decision(
        String framework,
        String artifact,
        String outcome,
        List<String> reasonCodes,
        String auditId,
        String recordedAt) {

    String toJson() {
        String reasons = reasonCodes.stream()
                .map(value -> "\"" + escape(value) + "\"")
                .reduce((left, right) -> left + "," + right)
                .orElse("");
        return "{" +
                "\"framework\":\"" + escape(framework) + "\"," +
                "\"artifact\":\"" + escape(artifact) + "\"," +
                "\"outcome\":\"" + outcome + "\"," +
                "\"reasonCodes\":[" + reasons + "]," +
                "\"auditId\":\"" + auditId + "\"," +
                "\"recordedAt\":\"" + recordedAt + "\"" +
                "}";
    }

    private static String escape(String value) {
        return value.replace("\\", "\\\\").replace("\"", "\\\"");
    }
}

final class AuthorityEngine {
    private static final String EXPECTED_DIGEST = "sha256:verified-demo-artifact";
    private static final int BUDGET_LIMIT = 100;

    Decision evaluate(DeploymentRequest request) {
        List<String> failures = new ArrayList<>();

        if (!"deployment-agent".equals(request.principal())) failures.add("PRINCIPAL_NOT_AUTHORIZED");
        if (!"deploy.production".equals(request.capability())) failures.add("CAPABILITY_NOT_GRANTED");
        if (!request.testsPassed()) failures.add("MISSING_TEST_EVIDENCE");
        if (request.evaluationScore() < 0.95) failures.add("EVALUATION_THRESHOLD_NOT_MET");
        if (!EXPECTED_DIGEST.equals(request.artifactDigest())) failures.add("ARTIFACT_DIGEST_MISMATCH");
        if (!request.approvalId().matches("APR-[0-9]{4}")) failures.add("INVALID_APPROVAL");
        if (request.requestedBudgetDollars() > BUDGET_LIMIT) failures.add("BUDGET_EXCEEDED");

        String outcome = failures.isEmpty() ? "ALLOW" : "DENY";
        String auditId = "AUD-" + Integer.toUnsignedString(request.hashCode(), 16).toUpperCase(Locale.ROOT);
        return new Decision(request.framework(), request.artifact(), outcome, List.copyOf(failures), auditId,
                Instant.now().toString());
    }
}

