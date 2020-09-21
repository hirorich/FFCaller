// 定義したコンポーネントを登録
const vm_media_trim = new Vue({
    el: '#media-trim-components',
    components: {
        'modal-component': modal_component,
        'media-trim-component': media_trim_component
    },
    template: `
        <div>
            <button class="btn btn-primary" v-on:click="show_modal()">範囲選択を開く</button>
            <modal-component ref="modal">
                <p slot="title" class="h4 text-primary">範囲選択</p>
                <media-trim-component ref="trim" slot="body"></media-trim-component>
                <button slot="button" class="btn btn-primary" v-on:click="save()">保存</button>
                <button slot="button" class="btn btn-secondary" v-on:click="hide_modal()">閉じる</button>
            </modal-component>
        <div>
    `,
    methods: {
        show_modal: function() {
            let info = {};
            info.media_src = "media/input.mp4";
            info.start_time = 250;
            info.media_duration = 300;
            info.with_video = true;
            info.with_audio = true;
            this.$refs.trim.set_media_trim(info);
            this.$refs.modal.show_modal();
        },
        hide_modal: function() {
            this.$refs.trim.$refs.media.pause();
            this.$refs.modal.hide_modal();
        },
        save: function() {
            this.$refs.trim.$refs.media.pause();
            this.$refs.modal.hide_modal();
        }
    }
});
