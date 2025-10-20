from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # App Runnerはポート番号を環境変数PORTで指定する
    port = int(os.environ.get('PORT', 8000))
    
    print("🔒 脆弱なショッピングモール - ウェブセキュリティ演習サイト")
    print(f"🌐 サーバー起動中... ポート{port}")
    print("⚠️  このサイトは学習目的のみで使用してください")
    
    # 本番環境ではdebugをFalseに
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug_mode) 