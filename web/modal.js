// モーダル表示のサンプル
// 参考：https://getbootstrap.jp/docs/4.2/components/modal/
const modal_component = {
    template: `
        <div class="modal fade">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <slot name="title"></slot>
                    </div>
                    <div class="modal-body">
                        <slot name="body"></slot>
                    </div>
                    <div class="modal-footer">
                        <slot name="sub_btn"></slot>
                        <button class="btn btn-secondary" v-on:click="close_modal()">キャンセル</button>
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

const app = new Vue({
    el: '#testModal',
    components: {
        'modal-component': modal_component
    },
    template: `
        <div>
            <modal-component ref="modal">
                <div slot="title">Title</div>
                <div slot="body">Body</div>
                <button class="btn btn-primary" slot="sub_btn" v-on:click="execute()">実行</button>
            </modal-component>
            <button class="btn btn-primary" slot="sub_btn" v-on:click="$refs.modal.show_modal()">開く</button>
        <div>
    `,
    methods: {
        execute: function() {
            alert('TEST');
            this.$refs.modal.close_modal();
        }
    }
})