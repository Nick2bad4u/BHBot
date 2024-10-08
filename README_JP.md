# BHBot 

Brawlhalla 用のゴールド/XP ファーミング ボット

[BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) に大きく影響を受けています

### ------ -------------------------------------------------- ----------- 

### ボットがアクティブにメンテナンスされるようになりました。
###### [Discord](https://discord.gg/2HDmuqqq9p "Discord") に参加して、ボットの保守や新機能の追加を手伝ってください。

### ----------------------------------------------- -------------------- 

**警告:** このソフトウェアはもともと私的利用を目的として開発されました。
そのように設計されていませんが、ゲーム内通貨を使用したマルハラ内での取引の実行など、予期せぬ結果につながる可能性があります。

**開発者は、このソフトウェアの使用によって生じる可能性のあるあらゆる損害に対して一切の責任を負いません。ソフトウェアの使用は慎重に行い、ご自身の判断で使用することをお勧めします。** 

(2024 年 4 月 18 日の時点で、ボットは複数の人によって 3,000 時間以上問題なくテストされています) 

# インストール
最新リリースはいつでもダウンロードできます [ここから](https://github.com/Nick2bad4u/BHBot/releases) 

# 機能

- 完全にバックグラウンドで動作します
- 入力を直接 Brawlhalla に送信して邪魔をしません
- ゲームを自動的に起動します
- ロビーを自動的に作成/設定します
- 自動的に選択/変更しますキャラクターとゲーム時間
- XP 制限を自動的に検出してリセット
- カスタム モードをサポート
- カスタム言語をサポート
- カスタム フォントもサポート
- ~~コーヒーを淹れます~~ (現時点では紅茶のみサポートしています) 

# 使用法
- プロセスは直感的にわかるように設計されています。 [設定] ボタンをクリックして、必要な設定を選択するだけです
- 設定が保存されたら、[開始] ボタンをクリックしてプログラムを開始します。 

# 制限
- ボットでは、[クロスオーバーの折りたたみ] が [はい] に設定されている必要があります。自動的にそのように設定されるべきだと思われる場合は、[問題を開いてください](https://github.com/nick2bad4u/bhbot/issues) 
- ボットではゲーム内言語を英語に設定する必要があります。自動的にそのように設定する必要があると思われる場合は、[問題を開いてください](https://github.com/nick2bad4u/bhbot/issues) 

# 技術概要
- 基礎となるコードはいつでも誰でもレビューできます。
- 基本的に、ボットは Windows SendMessage API を使用して入力を Brawlhalla ウィンドウに直接送信します。ピクセル検出を利用して状態を識別し、いつでも適切なアクションを決定します。

- BrawlhallaBot クラスを直接利用することも、そのカスタム ラッパーを開発することもできます。これは独立して動作するように設計されており、gui.py は PySimpleGUI を使用するグラフィカル ラッパーとしてのみ機能します。
