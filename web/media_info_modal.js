// 定義したコンポーネントを登録
const vm_media_info = new Vue({
    el: '#media-info-components',
    components: {
        'modal-component': modal_component,
        'media-info-component': media_info_component
    },
    template: `
        <div>
            <modal-component ref="modal">
                <p slot="title" class="h4 text-primary">動画情報</p>
                <media-info-component ref="info" slot="body"></media-info-component>
                <button slot="button" class="btn btn-secondary" v-on:click="hide_modal()">閉じる</button>
            </modal-component>
        <div>
    `,
    methods: {
        show_modal: function(media_info) {
            this.$refs.info.set_media_info(media_info);
            this.$refs.modal.show_modal();
        },
        hide_modal: function() {
            this.$refs.modal.hide_modal();
        }
    }
});

// ターゲット一覧取得
eel.expose(ffc_response_media_info)
function ffc_response_media_info(response) {
    vm_media_info.show_modal(response);
}
