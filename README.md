# QRコード生成ツール

Chromedriverを使用してURLのQRコードを生成するツールです。

## 前提条件

- [uv](https://docs.astral.sh/uv/)がインストールされていること
- Google Chromeがインストールされていること

## インストール

必要なパッケージをインストールします：

```bash
uv pip install -r requirements.txt
```

または、uvの仮想環境を使用する場合：

```bash
uv venv
uv pip install -r requirements.txt
```

## 使用方法

基本的な使い方（`image/qrcode.png`に保存されます）：

```bash
uv run create_qr.py https://example.com
```

出力ファイル名を指定する場合（`image`フォルダーに保存されます）：

```bash
uv run create_qr.py https://github.com -o github_qr.png
```

カスタムパスを指定する場合：

```bash
uv run create_qr.py https://example.com -o custom/path/qr.png
```

ヘルプを表示：

```bash
uv run create_qr.py -h
```

## 機能

- 任意のURLからQRコードを生成
- ヘッドレスモードで動作（ブラウザウィンドウを表示しない）
- Chromedriverの自動ダウンロード・管理
- デフォルトで`image`フォルダーに保存（フォルダーがない場合は自動作成）
- カスタム出力ファイル名・パスのサポート

## 必要な環境

- Python 3.7以上
- Google Chromeがインストールされていること

## 依存パッケージ

- selenium: Webブラウザの自動操作
- webdriver-manager: Chromedriverの自動管理
