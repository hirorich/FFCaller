# FFCaller
***
## FFCaller とは
- ffmpeg で指定するオプションを画面から指定し、ffmpeg を実行するツール
- Python の勉強として作成
- 画面は作るのが面倒だったので eel を用いて HTML で作成
  - ついでに勉強中だった Bootstrap と Vue.js を使用

***
## 環境構築
### コマンド, アプリ
- [ffmpeg, ffprobe](https://www.ffmpeg.org/download.html) v.4.2.2
  - GPLv3 License
  - Windowsの場合はexeをダウンロードし、コマンドラインから実行できるようにpathを設定
  - 呼び出すだけで再配布は行わないため GPLv3 は適用外のはず
    - [プログラムがforkやexecでプラグインを呼び出すならば、プラグインは別のプログラムであり、メインプログラムのライセンスはそれらにはなんの条件も課しません。](https://www.gnu.org/licenses/gpl-faq.ja.html#GPLAndPlugins)
- [Google Chrome](https://www.google.com/intl/ja/chrome/)
  - eel のローカルサーバとして localhost:0 を使用予定

### Python
- python v.3.8.2 ([Anaconda](https://www.anaconda.com/products/individual))
  - [Anaconda インストール手順](https://www.python.jp/install/anaconda/index.html)
    - コマンドから conda が実行できるように Anaconda3/condabin にpathを設定
  - FFCaller の名前で環境を作成
- [numpy](https://anaconda.org/anaconda/numpy) v.1.18.1
  - BSD 3-Clause License
- [opencv](https://anaconda.org/anaconda/opencv) v.4.0.1
  - BSD 3-Clause License
  - アイコン作成、一部バグ対応に使用
- [eel](https://github.com/samuelhwilliams/Eel) v.0.12.3
  - MIT License
  - Anacondaからターミナルを開き以下を実行することでインストール
    ```
    conda activate FFCaller
    pip install eel
    ```
- [plyer](https://github.com/kivy/plyer)
  - MIT License
  - デスクトップ通知に使用
  - Anacondaからターミナルを開き以下を実行することでインストール
    ```
    conda activate FFCaller
    pip install plyer
    ```

### HTML, CSS, Javascript
- [Bootstrap](https://github.com/twbs/bootstrap/releases) v.4.5.3
  - MIT License
- [jQuery](https://jquery.com/download/) v.3.5.1
  - MIT License
- [Popper.js](https://github.com/popperjs/popper-core/releases/tag/v1.16.0) v.1.16.0
  - MIT License
  - BootstrapのCDNからの参照がv.1.16.0であるため
- [Vue.js](https://github.com/vuejs/vue/releases) v.2.6.11
  - MIT License
- [Vue.Draggable](https://github.com/SortableJS/Vue.Draggable/releases) v.2.24.0
  - MIT License
- [sortablejs](https://github.com/SortableJS/sortablejs/releases) v.1.10.2
  - MIT License
