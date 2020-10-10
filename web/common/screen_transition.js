// ブラウザバックの抑制
history.pushState(null, null, null);
$(window).on("popstate", function (event) {
    if (!event.originalEvent.state) {
        history.pushState(null, null, null);
        return;
    }
});

// リロードの抑制
// 右クリックからの読み込みは抑制不可
$(document).on('keydown', function(e){
    switch (e.which || e.keyCode) {
        case 82:
            // Ctrl+Rキーの無効化
            // Ctrlが押されていない場合はOK
            if (!e.ctrlKey) {
                break;
            }
        case 116:
            // F5キーの無効化
            return false;
            break;
    }
});
