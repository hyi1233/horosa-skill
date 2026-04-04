import json

from horosa_skill.config import Settings
from horosa_skill.memory.store import MemoryStore


def test_memory_store_writes_artifact(tmp_path) -> None:
    settings = Settings(
        server_root="http://127.0.0.1:9999",
        db_path=tmp_path / "memory.db",
        output_dir=tmp_path / "runs",
    )
    store = MemoryStore(settings)
    run_id = store.create_run(entrypoint="tool", query_text="test")
    ref = store.record_tool_result(
        run_id=run_id,
        tool_name="chart",
        ok=True,
        input_normalized={"date": "1990-01-01"},
        envelope_dict={"ok": True, "tool": "chart"},
        summary=["ok"],
        warnings=[],
        error=None,
    )
    assert ref.run_id == run_id
    assert ref.tool_name == "chart"
    assert (tmp_path / "runs").exists()
    artifact_path = tmp_path / "runs" / ref.artifact_path.split("/runs/", 1)[1]
    assert artifact_path.parent.parent.parent.parent == (tmp_path / "runs")
    artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
    assert artifact["tool"] == "chart"
    assert artifact["record_meta"]["schema"] == "horosa.skill.record.v1"
    assert artifact["conversation"]["user_question"] == "test"

    queried = store.query_runs(tool="chart", include_payload=True)
    assert queried[0]["artifacts"][0]["payload"]["tool"] == "chart"
    assert queried[0]["user_question"] == "test"
    manifest = [item for item in queried[0]["artifacts"] if item["kind"] == "run_manifest"]
    assert manifest
    assert manifest[0]["payload"]["kind"] == "horosa.skill.run.manifest"


def test_memory_store_attach_ai_response_updates_artifacts_and_manifest(tmp_path) -> None:
    settings = Settings(
        server_root="http://127.0.0.1:9999",
        db_path=tmp_path / "memory.db",
        output_dir=tmp_path / "runs",
    )
    store = MemoryStore(settings)
    run_id = store.create_run(entrypoint="dispatch", query_text="问事业", subject={"name": "甲"})
    store.record_tool_result(
        run_id=run_id,
        tool_name="chart",
        ok=True,
        input_normalized={"date": "1990-01-01"},
        envelope_dict={"ok": True, "tool": "chart", "data": {}},
        summary=["ok"],
        warnings=[],
        error=None,
    )

    result = store.attach_ai_response(
        run_id=run_id,
        user_question="我今年事业如何？",
        ai_answer="整体先抑后扬。",
        ai_answer_structured={"tone": "mixed"},
        answer_meta={"model": "test"},
    )

    assert result["ok"] is True
    queried = store.query_runs(tool="chart", include_payload=True)
    assert queried[0]["user_question"] == "我今年事业如何？"
    assert queried[0]["ai_answer_text"] == "整体先抑后扬。"
    assert queried[0]["ai_answer_structured"] == {"tone": "mixed"}
    artifact_payload = queried[0]["artifacts"][0]["payload"]
    assert artifact_payload["conversation"]["ai_answer_text"] == "整体先抑后扬。"
    manifest = [item for item in queried[0]["artifacts"] if item["kind"] == "run_manifest"][0]["payload"]
    assert manifest["run"]["ai_answer_text"] == "整体先抑后扬。"
    exact = store.query_runs(run_id=run_id, include_payload=True)
    assert len(exact) == 1
    assert exact[0]["run_id"] == run_id
