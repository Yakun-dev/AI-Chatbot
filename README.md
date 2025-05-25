# AI Chatbot

FlaskとCohereを使用したシンプルなチャットボットアプリケーションです。

## セットアップ方法

1. 必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

2. CohereのAPIキーを設定:
- `.env`ファイルをプロジェクトのルートディレクトリに作成
- 以下の内容を追加:
```
COHERE_API_KEY=your_api_key_here
```

## アプリケーションの起動方法

1. ターミナルで以下のコマンドを実行:
```bash
python app.py
```

2. ブラウザで以下のURLにアクセス:
```
http://localhost:5000
```

## 機能

- ユーザーとAIのメッセージを異なる色で表示
- シンプルで使いやすいインターフェース
- Enterキーでメッセージを送信可能 