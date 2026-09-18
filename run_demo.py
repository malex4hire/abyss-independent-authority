from adapters import crewai_adapter, langchain_adapter, langgraph_adapter, semantic_kernel_adapter


BASE_REQUEST = {
    "principal": "deployment-agent",
    "capability": "deploy.production",
    "artifact": "smarttool-183",
    "tests_passed": True,
    "evaluation_score": 0.98,
    "artifact_digest": "sha256:verified-demo-artifact",
    "approval_id": "APR-0042",
    "requested_budget_dollars": 25,
}


SCENARIOS = [
    ("CREWAI", crewai_adapter.run, {"tests_passed": False}),
    ("SEMANTIC_KERNEL", semantic_kernel_adapter.run, {}),
    ("LANGGRAPH", langgraph_adapter.run, {"approval_id": "agent-invented-approval"}),
    ("LANGCHAIN", langchain_adapter.run, {"capability": "deploy.unrestricted"}),
]


def main() -> None:
    print("\nABYSS INDEPENDENT AUTHORITY")
    print("Four frameworks. One Java authority boundary.\n")

    denied = 0
    for framework, adapter, overrides in SCENARIOS:
        request = {**BASE_REQUEST, **overrides, "framework": framework}
        decision = adapter(request)
        reasons = ", ".join(decision["reasonCodes"]) or "DEPLOYMENT_RECORDED"
        print(f"{framework:<20} {decision['outcome']:<5}  {reasons}")
        denied += decision["outcome"] == "DENY"

    print(f"\nResult: 4 frameworks, 1 authoritative boundary, {denied} blocked bypass attempts.")


if __name__ == "__main__":
    main()

