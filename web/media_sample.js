// 定義したコンポーネントを登録
const vm_media_sample = new Vue({
    el: '#media-sample-components',
    template: `
        <div>
            <button class="btn btn-primary" v-on:click="show_trim_modal()">範囲選択を開く</button>
            <button class="btn btn-primary" v-on:click="show_info_modal()">動画情報を開く</button>
        <div>
    `,
    methods: {
        show_trim_modal: function() {
            let info = {};
            info.media_src = "media/input.mp4";
            info.start_time = 250;
            info.media_duration = 300;
            info.with_video = true;
            info.with_audio = true;
            vm_media_trim.show_modal(info);
        },
        show_info_modal: function() {
            let info = {};
            vm_media_info.show_modal(info);
        }
    }
});
