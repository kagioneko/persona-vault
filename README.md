# persona-vault

EmiliaLab 外縁系OSSのキャラクタープロファイル共有リポジトリ。

NeuroState初期値・バイアス設定・ペルソナ説明をJSONで管理します。コミュニティで作ったペルソナをPRで追加できます。

## プロファイル一覧

| ID | 名前 | タグ |
|----|------|------|
| `paranoid_reviewer` | 偏執的レビュアー | analytical, strict, code-review |
| `empathic_listener` | 共感型リスナー | emotional, supportive, night |
| `chaotic_founder` | カオスな創業者 | creative, entrepreneurial, fast |
| `board_advisor` | ボードアドバイザー | analytical, business, strategic |
| `debug_mode` | デバッグモード | experimental, meta, chaos |

## 使い方

### Pythonから

```python
from loader import load_persona, list_personas, to_system_prompt

# IDで読み込む
persona = load_persona("empathic_listener")
print(persona["neuro_state"])   # {"D": 50, "S": 70, ...}
print(persona["bias_preset"])   # "empathic_assistant"

# タグで絞り込む
analytical = list_personas(tags=["analytical"])

# system promptのベースを生成
prompt = to_system_prompt(persona)
```

### JSONを直接使う

`profiles/` 配下のJSONをそのまま参照してください。

```json
{
  "id": "paranoid_reviewer",
  "name": "偏執的レビュアー",
  "neuro_state": {"D": 45, "S": 40, "C": 80, ...},
  "bias_preset": "paranoid_reviewer",
  "prompt_blocks": ["neuro", "anti_yesman"],
  "persona_text": "..."
}
```

### neurostate-sdkと組み合わせる

```python
from loader import load_persona
from neurostate_sdk import NeuroState, BiasEngine, build_system_prompt
from neurostate_sdk.bias import PRESETS

persona = load_persona("chaotic_founder")

# NeuroStateに初期値を適用
ns = persona["neuro_state"]
state = NeuroState(D=ns["D"], S=ns["S"], C=ns["C"],
                   O=ns["O"], G=ns["G"], E=ns["E"])

# バイアスプリセットを適用
engine = BiasEngine(persist=False)
engine.activate_preset(persona["bias_preset"])

# system prompt生成
prompt = build_system_prompt(
    state=state,
    persona_name=persona["name"],
    blocks=persona["prompt_blocks"],
)
```

## プロファイルのフォーマット

```json
{
  "id": "unique_id",
  "name": "表示名",
  "description": "このペルソナの説明",
  "tags": ["タグ1", "タグ2"],
  "neuro_state": {
    "D": 50, "S": 50, "C": 50,
    "O": 0, "G": 50, "E": 50
  },
  "bias_preset": "bias-engine-mcpのプリセット名",
  "prompt_blocks": ["neuro", "anti_yesman"],
  "persona_text": "system promptに追加するペルソナ説明",
  "author": "作者名",
  "version": "1.0.0"
}
```

## PRでペルソナを追加する

1. `profiles/` に `your_persona_id.json` を作成
2. フォーマットに沿って記述
3. PRを送る

## 関連プロジェクト

| リポジトリ | 役割 |
|-----------|------|
| [neurostate-sdk](https://github.com/kagioneko/neurostate-sdk) | 統合SDK |
| [neurostate-engine](https://github.com/kagioneko/neurostate-engine) | 感情状態管理 |
| [bias-engine-mcp](https://github.com/kagioneko/bias-engine-mcp) | 思考傾向管理 |
| [apie](https://github.com/kagioneko/apie) | ビジュアルUI |

## ライセンス

MIT
