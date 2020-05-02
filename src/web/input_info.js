// 対象動画ファイル名
var input_info=new Vue({
    el:'#input_info',
    data:{
        filename:''
    },
    methods:{
        analyze: function(){
            filename=this.filename;
            eel.analyze(filename);
        }
    }
});
