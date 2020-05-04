# FFCaller
## FFCaller とは
- ffmpeg で指定するオプションを画面から指定し、ffmpeg を実行するツール
- Python の勉強として作成
- 画面は作るのが面倒だったので eel を用いて HTML で作成
  - ついでに勉強中だった Bootstrap と Vue.js を使用

***
## 環境構築
### コマンド, アプリ
- [ffmpeg, ffprobe](https://www.ffmpeg.org/download.html) v.4.2.2
  - Windowsの場合はexeをダウンロードし、コマンドラインから実行できるようにpathを設定
- [Google Chrome](https://www.google.com/intl/ja/chrome/)
  - eel のローカルサーバとして localhost:9090 を使用予定

### Python
- python v.3.8.2 ([Anaconda](https://www.anaconda.com/products/individual))
  - [Anaconda インストール手順](https://www.python.jp/install/anaconda/index.html)
    - コマンドから conda が実行できるように Anaconda3/condabin にpathを設定
  - FFCaller の名前で環境を作成
- [numpy](https://anaconda.org/anaconda/numpy) v.1.18.1
- [eel](https://github.com/samuelhwilliams/Eel) v.0.12.3
  - Anacondaからターミナルを開き以下を実行
    ```
    conda activate FFCaller
    pip install eel
    ```

### HTML, CSS, Javascript
- [Bootstrap](https://github.com/twbs/bootstrap/releases) v.4.4.1
- [jQuery](https://jquery.com/download/) v.3.5.0
- [Popper.js](https://github.com/popperjs/popper-core/releases) v.1.16.0
- [Vue.js](https://github.com/vuejs/vue/releases) v.2.6.11
