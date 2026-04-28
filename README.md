家計簿アプリ（Flask）
概要

Flaskで作成したシンプルな家計簿アプリです。
支出の記録・一覧表示・削除・月別フィルタ・合計金額表示ができます。

機能
支出の追加
一覧表示
削除
月別フィルタ
合計金額表示
SQLiteによるデータ永続化
技術スタック
Python/Flask/SQLite
HTML/CSS

セットアップ方法
git clone https://github.com/ユーザー名/kakeibo-app.git
cd kakeibo-app

python -m venv venv
source venv/bin/activate  # Windowsは venv\Scripts\activate

pip install -r requirements.txt
python app.py

ブラウザで以下にアクセス：　
http://127.0.0.1:5000
