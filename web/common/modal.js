// モーダル画面
// slotでtitle, body, buttonを指定
// 開閉のたびに再描画するかをcanRepaintで指定可能
const modal_component = {
    props: {
        canRepaint: {
            type: Boolean,
            default: false
        },
    },
    data: function() {
        return {
            is_show: false
        }
    },
    computed: {
        can_repaint : function() {
            return this.canRepaint;
        }
    },
    template: `
        <div class="modal fade" data-backdrop="static">
            <div class="modal-dialog">
                <div v-if="can_repaint || is_show" class="modal-content">
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
            this.is_show = true;
            $(this.$el).modal('show');
        },
        close_modal: function() {
            $(this.$el).modal('hide');
            this.is_show = false;
        }
    }
}
