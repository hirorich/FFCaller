// 設定情報
var property=new Vue({
    el:'#property',
    data:{
        outdir:''
    },
    computed:{
        outdir_frame: function() {
            return this.outdir + 'frame/';
        }
    },
    methods:{
        clear_outdir: function(){
            eel.clear_outdir();
            eel.get_property();
        }
    }
});

// プロパティ情報取得
eel.expose(set_property)
function set_property(outdir) {

    // 出力フォルダ
    property.outdir=outdir;
}

eel.get_property();
