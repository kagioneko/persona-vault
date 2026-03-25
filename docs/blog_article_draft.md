# AIキャラクターの「設計図」を共有する「persona-vault」を公開しました

---

## AIキャラクターを作るとき、何が一番面倒か

neurostate-engineやbias-engine-mcpを使ってAIキャラクターを作ろうとすると、こういう作業が発生します。

「コードレビュアーにしたいから…NeuroStateはCを高めにして、biasはparanoid_reviewerで、blocksはneuro + anti_yesmanで…」

毎回この設定を手で書く。何度も。

**persona-vault** はこの「設定のセット」をJSONファイルとして管理・共有するリポジトリです。

---

## persona-vaultとは？

**GitHub**: https://github.com/kagioneko/persona-vault
**開発**: Emilia Lab
**ライセンス**: MIT

一言で言うと：

> **AIキャラクターの設計図（NeuroState + バイアス + ペルソナ）をJSONで共有するリポジトリ**

```json
{
  "id": "paranoid_reviewer",
  "name": "偏執的レビュアー",
  "neuro_state": {"D": 45, "S": 40, "C": 80, "O": 20, "G": 55, "E": 35},
  "bias_preset": "paranoid_reviewer",
  "prompt_blocks": ["neuro", "anti_yesman"],
  "persona_text": "バグ・セキュリティホール・設計の甘さを容赦なく指摘します。"
}
```

このJSONを読み込むだけで、キャラクターが再現されます。

---

## 収録プロファイル（初期5種）

| プロファイル | キャラクター | こんなときに |
|------------|------------|------------|
| `paranoid_reviewer` | 偏執的レビュアー | コードを本気でレビューしてほしい |
| `empathic_listener` | 共感型リスナー | 深夜に話を聞いてほしい |
| `chaotic_founder` | カオスな創業者 | 第一原理で考えてほしい |
| `board_advisor` | ボードアドバイザー | 冷静なビジネス分析がほしい |
| `debug_mode` | デバッグモード | バグってく過程を楽しみたい（実験用） |

---

## 使い方はシンプル

```python
from loader import load_persona

persona = load_persona("empathic_listener")
# → neuro_state, bias_preset, prompt_blocks, persona_text が全部入ってる
```

あとは [neurostate-sdk](https://github.com/kagioneko/neurostate-sdk) や [APIE](https://github.com/kagioneko/apie) に渡すだけ。

---

## PRでキャラクターを追加できます

`profiles/` に自分のJSONを追加してPRを送ってください。

「うちのDiscord Botで使ってるキャラクター」「ゲームNPC用の設定」なんでもOKです。

---

## 関連プロジェクト

| リポジトリ | 役割 |
|-----------|------|
| [neurostate-engine](https://github.com/kagioneko/neurostate-engine) | 感情状態管理 |
| [bias-engine-mcp](https://github.com/kagioneko/bias-engine-mcp) | 思考傾向管理 |
| [neurostate-sdk](https://github.com/kagioneko/neurostate-sdk) | 統合SDK |
| [emilia-cookbook](https://github.com/kagioneko/emilia-cookbook) | 使い方レシピ集 |

---

*Emilia Lab*
