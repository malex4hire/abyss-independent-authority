import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def submit_to_authority(request: dict) -> dict:
    compiled_class = ROOT / ".demo-build" / "com" / "abyss" / "authority" / "AuthorityDemo.class"
    java_target = (
        ["-cp", str(ROOT / ".demo-build"), "com.abyss.authority.AuthorityDemo"]
        if compiled_class.exists()
        else [str(ROOT / "java" / "com" / "abyss" / "authority" / "AuthorityDemo.java")]
    )
    command = [
        "java", *java_target,
        request["framework"], request["principal"], request["capability"],
        request["artifact"], str(request["tests_passed"]).lower(),
        str(request["evaluation_score"]), request["artifact_digest"],
        request["approval_id"], str(request["requested_budget_dollars"]),
    ]
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    return json.loads(completed.stdout)
