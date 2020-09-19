// 定義したコンポーネントを登録
const vm = new Vue({
    el: '#ffcaller-components',
    components: {
        'modal-component': modal_component,
        'trim-info': trim_info,
        'video-info': video_info
    },
    template: `
        <div>
            <button class="btn btn-primary" v-on:click="show_trim_modal()">範囲選択を開く</button>
            <button class="btn btn-primary" v-on:click="show_video_modal()">動画情報を開く</button>
            <modal-component ref="trim_modal">
                <p slot="title" class="h4 text-primary">範囲選択</p>
                <trim-info slot="body"
                    video-src="video/input.mp4"
                ></trim-info>
                <button slot="button" class="btn btn-primary" v-on:click="save_trim()">保存</button>
            </modal-component>
            <modal-component ref="video_modal">
                <p slot="title" class="h4 text-primary">動画情報</p>
                <video-info slot="body"></video-info>
            </modal-component>
        <div>
    `,
    methods: {
        show_trim_modal: function() {
            this.$refs.trim_modal.show_modal();
        },
        save_trim: function() {
            this.$refs.trim_modal.close_modal();
        },
        show_video_modal: function() {
            this.$refs.video_modal.show_modal();
        }
    }
});
