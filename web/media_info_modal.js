// 定義したコンポーネントを登録
const vm_media_info = new Vue({
    el: '#media-info-components',
    components: {
        'modal-component': modal_component,
        'media-info-component': media_info_component
    },
    template: `
        <div>
            <button class="btn btn-primary" v-on:click="show_modal()">動画情報を開く</button>
            <modal-component ref="modal">
                <p slot="title" class="h4 text-primary">動画情報</p>
                <media-info-component ref="info" slot="body"></media-info-component>
                <button slot="button" class="btn btn-secondary" v-on:click="hide_modal()">閉じる</button>
            </modal-component>
        <div>
    `,
    methods: {
        show_modal: function() {
            let info = {};
            this.$refs.info.set_media_info(info);
            this.$refs.modal.show_modal();
        },
        hide_modal: function() {
            this.$refs.modal.hide_modal();
        }
    }
});
