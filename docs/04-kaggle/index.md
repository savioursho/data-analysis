
# Kaggle

## memo

- テンプレートのコードをまとめておいた方がよいもの
  - ベースラインモデルの作成
  - 特徴量重要度の算出
  - 特徴量の管理
  - パラメータチューニング
  - 欠損値処理
    - [6.4. Imputation of missing values — scikit-learn 1.2.0
      documentation](https://scikit-learn.org/stable/modules/impute.html)
      - 欠損値処理を行うクラスがたくさんあるので見たほうがいい
  - sklearn のパイプライン
    - ColumnTransformer
    - FeatureUnion

  

- MLモデルでの予測が得意な部分と、ルールベースで決めた方が正確な部分とに分けるとよさそう。
- 欠損値処理はどんな場合でもパイプラインに組み込む
  - 訓練データに欠損がなくても、推論データに欠損があるかも知れないから
- 実行ファイルはpyファイルにするのがよさそう
  - OSに依存しないから

  

- [Target Encoding はなぜ有効なのか - Speaker
  Deck](https://speakerdeck.com/hakubishin3/target-encoding-hanazeyou-xiao-nafalseka)
  - 「より水準が増えていくと」 のスライドを見るとわかりやすい
  - ラベルエンコードだと、カテゴリをターゲットの大きさの順を無視しているので効率が悪いということ

### プロジェクト構成

考慮すべき観点  

- 実験を回しやすいか？
- 再利用性が高いか？
- 実運用に移すときに問題がないか？
  - 大幅にコードを書き直すということはしたくない

参考リンク  

- [arnabbiswas1/kaggle_pipeline_tps_aug_22: Kaggle Pipeline for tabular
  data
  competitions](https://github.com/arnabbiswas1/kaggle_pipeline_tps_aug_22)
- [RobMulla/kaggle-ieee-fraud-detection: IEEE-CIS Fraud Detection Kaggle
  Competition
  Code](https://github.com/RobMulla/kaggle-ieee-fraud-detection)
- [Home - Cookiecutter Data
  Science](https://drivendata.github.io/cookiecutter-data-science/)
- [オレオレKaggle実験管理](https://zenn.dev/fkubota/articles/f7efe69fd2044d)
- [機械学習実験環境を晒す -
  Qiita](https://qiita.com/chizuchizu/items/8261bb831b2eebf1a6af)
- [コンペ中のコード、どうしてる？ - Speaker
  Deck](https://speakerdeck.com/koukyo1994/konpezhong-falsekodo-dousiteru?slide=12)
- [ML Pipeline for Kaggleのススメ -
  重み元帥によるねこにっき](https://mocobt.hatenablog.com/entry/2020/03/18/230758)
- [KazukiOnodera/Home-Credit-Default-Risk: 2nd Place Solution
  💰🥈](https://github.com/KazukiOnodera/Home-Credit-Default-Risk)
- [学習・推論パイプラインを構築する上で大切にしていること - Speaker
  Deck](https://speakerdeck.com/takapy/xue-xi-tui-lun-paipurainwogou-zhu-surushang-deda-qie-nisiteirukoto)
- [ghmagazine/kagglebook](https://github.com/ghmagazine/kagglebook)
  - 「Kaggleで勝つデータ分析の技術」 のサンプルコード
- [takapy0210/takaggle:
  分析コンペ用のスクリプト集](https://github.com/takapy0210/takaggle)
