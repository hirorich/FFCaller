// 定義したコンポーネントを登録
const media = new Vue({
    el: '#ffcaller-components',
    components: {
        'modal-component': modal_component,
        'media-trim': media_trim,
        'media-info': media_info
    },
    template: `
        <div>
            <button class="btn btn-primary" v-on:click="show_trim_modal()">範囲選択を開く</button>
            <button class="btn btn-primary" v-on:click="show_info_modal()">動画情報を開く</button>
            <modal-component ref="trim_modal">
                <p slot="title" class="h4 text-primary">範囲選択</p>
                <media-trim ref="trim" slot="body"></media-trim>
                <button slot="button" class="btn btn-primary" v-on:click="save_trim()">保存</button>
                <button slot="button" class="btn btn-secondary" v-on:click="close_trim_modal()">閉じる</button>
            </modal-component>
            <modal-component ref="info_modal">
                <p slot="title" class="h4 text-primary">動画情報</p>
                <media-info ref="info" slot="body"></media-info>
                <button slot="button" class="btn btn-secondary" v-on:click="close_info_modal()">閉じる</button>
            </modal-component>
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
            this.$refs.trim.set_media_trim(info);
            this.$refs.trim_modal.show_modal();
        },
        save_trim: function() {
            this.$refs.trim.$refs.media.pause();
            this.$refs.trim_modal.close_modal();
        },
        close_trim_modal: function() {
            this.$refs.trim.$refs.media.pause();
            this.$refs.trim_modal.close_modal();
        },
        show_info_modal: function() {
            let info = {};
            this.$refs.info.set_media_info(info);
            this.$refs.info_modal.show_modal();
        },
        close_info_modal: function() {
            this.$refs.info_modal.close_modal();
        }
    }
});
