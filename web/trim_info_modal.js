// 定義したコンポーネントを登録
const vm_trim_info = new Vue({
    el: '#trim-info-components',
    components: {
        'modal-component': modal_component,
        'trim-info-component': trim_info_component
    },
    data: function() {
        return {
            target_id: 0
        }
    },
    template: `
        <div>
            <modal-component ref="modal">
                <p slot="title" class="h4 text-primary">範囲選択</p>
                <trim-info-component ref="trim" slot="body"></trim-info-component>
                <button slot="button" class="btn btn-primary" v-on:click="save()">保存</button>
                <button slot="button" class="btn btn-secondary" v-on:click="hide_modal()">閉じる</button>
            </modal-component>
        <div>
    `,
    methods: {
        show_modal: function(info) {
            this.target_id = info.target_id;
            this.$refs.trim.set_trim_info(info);
            this.$refs.modal.show_modal();
        },
        hide_modal: function() {
            this.$refs.modal.hide_modal();
        },
        hide_media: function() {
            this.$refs.trim.$refs.media.hideMedia();
        },
        save: function() {
            let request = {
                target_id: this.target_id,
                trim: this.$refs.trim.get_trim_info()
            };
            eel.ffc_request_update_trim_info(request);
            this.$refs.modal.hide_modal();
        }
    }
});

// 非表示時に動画コンテンツを削除
$(vm_trim_info.$refs.modal.$el).on('hidden.bs.modal', function () {
    vm_trim_info.hide_media();
});

// トリム情報取得
eel.expose(ffc_response_trim_info)
function ffc_response_trim_info(response) {
    vm_trim_info.show_modal(response);
}
