// モーダル画面
// slotでtitle, body, buttonを指定
const modal_component = {
    template: `
        <div class="modal fade" data-backdrop="static">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <slot name="title"></slot>
                    </div>
                    <div class="modal-body">
                        <slot name="body"></slot>
                    </div>
                    <div class="modal-footer">
                        <slot name="button"></slot>
                        <button class="btn btn-secondary" v-on:click="close_modal()">閉じる</button>
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {
        show_modal: function() {
            $(this.$el).modal('show');
        },
        close_modal: function() {
            $(this.$el).modal('hide');
        }
    }
}
