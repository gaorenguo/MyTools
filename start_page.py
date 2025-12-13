import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. ブラウザを起動（Chrome）
# Chromeオプションを設定
chrome_options = Options()
# chrome_options.add_argument('--headless')  # ヘッドレスモード（ブラウザ画面を表示しない）が必要な場合
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--log-level=3')  # ログレベルを下げる

try:
    driver = webdriver.Chrome(options=chrome_options)
except Exception as e:
    print(f"ChromeDriverの初期化に失敗しました: {e}")
    print("\n以下を確認してください:")
    print("1. Google Chromeがインストールされているか")
    print("2. インターネット接続があるか（Selenium Managerがドライバーをダウンロードするため）")
    print("3. ファイアウォールやプロキシの設定")
    exit(1)

try:
    # 2. Googleのトップページを開く
    driver.get("https://www.google.com")

    # 3. 検索ボックスを見つける
    # Googleの検索ボックスは name="q" という属性を持っています
    search_box = driver.find_element(By.NAME, "q")

    # 4. キーワードを入力 ("Selenium Python")
    search_box.send_keys("Selenium Python")

    # 5. Enterキーを押して検索実行
    search_box.send_keys(Keys.RETURN)

    # 6. 結果を目視確認するために少し待機（通常は明示的な待機を使いますが、ここでは簡易的にsleep）
    time.sleep(3)

    # 7. ページタイトルを表示
    print(f"現在のページタイトル: {driver.title}")

    # (応用) 検索結果のタイトルを取得して表示
    # h3タグが検索結果の見出しに使われています
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    
    print("\n--- 検索結果トップ3 ---")
    for i, element in enumerate(results[:3]):
        print(f"{i+1}: {element.text}")

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    # 8. ブラウザを閉じる（必ず行う）
    driver.quit()