# AWS App Runner デプロイメントガイド

このガイドでは、脆弱なショッピングモールアプリケーションをAWS App Runnerにデプロイする手順を説明します。

## 🚀 デプロイ手順

### 1. 前提条件
- AWSアカウントが必要
- GitHubリポジトリ: `https://github.com/tmakxss/vulnerable-shopping-mall-apprunner2`
- App Runnerサービスへのアクセス権限

### 2. App Runnerサービスの作成

#### 2.1 AWSコンソールにログイン
1. AWS Management Consoleにサインイン
2. App Runnerサービスに移動
3. 「サービスを作成」をクリック

#### 2.2 ソース設定
1. **リポジトリタイプ**: "Source code repository" を選択
2. **プロバイダー**: "GitHub" を選択
3. **GitHub接続**: 新しい接続を作成するか、既存の接続を使用
4. **リポジトリURL**: `https://github.com/tmakxss/vulnerable-shopping-mall-apprunner2`
5. **ブランチ**: `master`
6. **自動デプロイ**: 有効にする（推奨）

#### 2.3 ビルド設定
1. **設定ファイル**: "Use a configuration file" を選択
2. **設定ファイル名**: `apprunner.yaml` （自動検出される）

#### 2.4 サービス設定
1. **サービス名**: `vulnerable-shopping-mall-app` (任意の名前)
2. **仮想CPU**: 0.25 vCPU (最小構成でOK)
3. **メモリ**: 0.5 GB (最小構成でOK)

### 3. 環境変数の設定

#### 3.1 基本環境変数
App Runnerコンソールの「設定」→「環境変数」で以下を設定：

```
PORT=8000
FLASK_ENV=production
PYTHONPATH=.
SECRET_KEY=your_secure_secret_key_here_change_this_in_production
EDUCATIONAL_USE_ONLY=true
SECURITY_WARNING=true
```

#### 3.2 データベース環境変数（Supabaseを使用する場合）
```
DB_TYPE=supabase
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

#### 3.3 PostgreSQL直接接続を使用する場合
```
DB_TYPE=postgresql
DATABASE_URL=postgresql://username:password@host:port/database
```

### 4. ヘルスチェック設定
1. **ヘルスチェックパス**: `/health`
2. **ヘルスチェック間隔**: 20秒
3. **ヘルスチェックタイムアウト**: 10秒
4. **正常なしきい値**: 1
5. **異常なしきい値**: 5

### 5. セキュリティ設定

#### 5.1 VPCコネクション（オプション）
データベースが専用VPC内にある場合：
1. App RunnerのVPC設定でVPCコネクターを作成
2. 適切なサブネットとセキュリティグループを選択

#### 5.2 IAMロール
必要に応じてApp Runner用のIAMロールを作成し、以下の権限を付与：
- CloudWatch Logsへの書き込み権限
- データベースアクセス権限（必要に応じて）

### 6. デプロイの実行
1. すべての設定を確認
2. 「作成して実行」をクリック
3. デプロイ完了まで5-10分程度待機

### 7. デプロイ後の確認

#### 7.1 アプリケーション動作確認
1. App RunnerコンソールでサービスURLを確認
2. ブラウザでアクセスして動作確認
3. ヘルスチェックエンドポイント (`/health`) でステータス確認

#### 7.2 ログ確認
1. App Runnerコンソールの「ログ」タブを確認
2. エラーがないかチェック
3. CloudWatch Logsで詳細ログを確認

## 🔍 トラブルシューティング

### よくある問題と解決法

#### 1. ビルドエラー
- `requirements.txt` の依存関係を確認
- Python バージョンの互換性を確認
- ビルドログでエラー詳細を確認

#### 2. アプリケーション起動エラー
- 環境変数が正しく設定されているか確認
- ポート番号が8000に設定されているか確認
- `run.py` の修正が正しく適用されているか確認

#### 3. データベース接続エラー
- データベース接続情報が正しいか確認
- VPCコネクション設定を確認
- セキュリティグループの設定を確認

#### 4. ヘルスチェック失敗
- `/health` エンドポイントがアクセス可能か確認
- ヘルスチェック設定を見直し
- アプリケーションが完全に起動するまで時間を調整

## 📊 モニタリング設定

### CloudWatch アラーム
以下のメトリクスでアラームを設定することを推奨：
- CPU使用率
- メモリ使用率
- HTTP 4xx/5xx エラー率
- レスポンス時間

### ログ監視
- アプリケーションエラーログ
- アクセスログ
- セキュリティ関連のログ

## 🛡️ セキュリティ考慮事項

⚠️ **重要**: このアプリケーションは教育目的で作成された脆弱なアプリケーションです。

### 本番環境での注意点
1. **適切なSecret Key**: SECRET_KEYは強力なランダム値に変更
2. **データベースセキュリティ**: 適切なアクセス制御とVPC設定
3. **HTTPS強制**: App RunnerのHTTPS設定を有効化
4. **ログ監視**: セキュリティイベントの監視設定
5. **アクセス制限**: 必要に応じてIP制限やWAF設定

## 📝 デプロイメント完了

デプロイが完了すると、以下のようなURLでアプリケーションにアクセスできます：
```
https://your-app-name.region.awsapprunner.com
```

このアプリケーションは学習目的のみで使用し、本番環境での使用は避けてください。

## 🔄 継続的デプロイメント

GitHubリポジトリの `master` ブランチに変更をプッシュすると、App Runnerが自動的に新しいバージョンをデプロイします。

---

📚 **参考リンク**:
- [AWS App Runner 開発者ガイド](https://docs.aws.amazon.com/apprunner/)
- [App Runner Configuration File Reference](https://docs.aws.amazon.com/apprunner/latest/dg/config-file.html)