"""persona-vault — ペルソナプロファイルローダー"""

from __future__ import annotations
import json
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_persona(persona_id: str) -> dict:
    """IDでペルソナを読み込む"""
    path = PROFILES_DIR / f"{persona_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"ペルソナが見つかりません: {persona_id}")
    return json.loads(path.read_text(encoding="utf-8"))


def list_personas(tags: list[str] | None = None) -> list[dict]:
    """全ペルソナ一覧（tagsで絞り込み可）"""
    personas = []
    for f in sorted(PROFILES_DIR.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        if tags and not any(t in data.get("tags", []) for t in tags):
            continue
        personas.append(data)
    return personas


def to_system_prompt(persona: dict) -> str:
    """ペルソナ辞書からsystem promptのベースを生成"""
    lines = [
        f"# {persona['name']}",
        "",
        persona.get("persona_text", ""),
        "",
        f"// id: {persona['id']}",
        f"// tags: {', '.join(persona.get('tags', []))}",
    ]
    return "\n".join(lines)
