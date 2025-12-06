import argparse
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def generate_qr_code(url, output_path="qrcode.png"):
    """
    Chromedriverを使用してURLのQRコードを生成します

    Args:
        url (str): QRコードに変換するURL
        output_path (str): 保存先のファイルパス
    """
    print(f"QRコード生成中: {url}")

    # 出力ディレクトリが存在しない場合は作成
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"ディレクトリを作成しました: {output_dir}")

    # Chromeドライバーの設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ヘッドレスモード（ブラウザ画面を表示しない）
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Chromedriverの初期化（webdriver_managerで自動ダウンロード）
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # QRコード生成サイトにアクセス
        qr_service_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={url}"
        driver.get(qr_service_url)

        # ページの読み込みを待機
        time.sleep(2)

        # QRコード画像を保存
        driver.save_screenshot(output_path)
        print(f"QRコードを保存しました: {output_path}")

        # 絶対パスを表示
        abs_path = os.path.abspath(output_path)
        print(f"保存場所: {abs_path}")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        driver.quit()


def main():
    parser = argparse.ArgumentParser(
        description='URLのQRコードを生成するツール',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
使用例:
  uv run create_qr.py https://example.com
  uv run create_qr.py https://github.com -o github_qr.png
  uv run create_qr.py https://example.com -o custom/path/qr.png
        '''
    )

    parser.add_argument(
        'url',
        help='QRコードに変換するURL'
    )

    parser.add_argument(
        '-o', '--output',
        default='qrcode.png',
        help='出力ファイル名（デフォルト: image/qrcode.png）'
    )

    args = parser.parse_args()

    # 出力パスの処理：ファイル名のみの場合はimageフォルダーに保存
    output_path = args.output
    if os.path.dirname(output_path) == '':
        output_path = os.path.join('image', output_path)

    # QRコード生成
    generate_qr_code(args.url, output_path)


if __name__ == "__main__":
    main()
