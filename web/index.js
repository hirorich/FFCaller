// 定義したコンポーネントを登録
const vm = new Vue({
    el: '#ffcaller-components',
    components: {
        'target-component': target_component
    },
    data: function() {
        return {
            is_loading: false
        }
    },
    template: `
        <div>
            <button class="btn btn-primary" v-bind:disabled="is_loading" v-on:click="add_target()">
                <span v-if="is_loading" class="spinner-border spinner-border-sm"></span>
                <span v-if="is_loading">Loading...</span>
                <span v-else="is_loading">追加</span>
            </button>
            <target-component ref="target"></target-component>
        </div>
    `,
    methods: {
        add_target: function() {
            eel.ffc_request_choose_files();
            this.is_loading = true;
        },
        set_target: function(response) {
            this.$refs.target.set_target_list(response);
            this.is_loading = false;
        }
    }
});

// ターゲット一覧取得
eel.expose(ffc_response_target_list)
function ffc_response_target_list(response) {
    vm.set_target(response);
}
