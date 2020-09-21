// モーダル表示のサンプル
// 参考：https://getbootstrap.jp/docs/4.2/components/modal/
const app = new Vue({
    el: '#modalSample',
    components: {
        'modal-component': modal_component
    },
    template: `
        <div>
            <modal-component ref="modal">
                <div slot="title">Title</div>
                <div slot="body">Body</div>
                <button class="btn btn-primary" slot="button" v-on:click="execute()">実行</button>
            </modal-component>
            <button class="btn btn-primary" v-on:click="$refs.modal.show_modal()">開く</button>
        <div>
    `,
    methods: {
        execute: function() {
            alert('Sample');
            this.$refs.modal.close_modal();
        }
    }
})
