// 定義したコンポーネントを登録
const vm = new Vue({
    el: '#ffcaller-components',
    components: {
        'target-component': target_component
    },
    template: `
        <div>
            <button class="btn btn-primary" v-on:click="add_target()">追加</button>
            <target-component ref="target"></target-component>
        </div>
    `,
    methods: {
        add_target: function() {
            eel.select_files();
        }
    }
});

// ターゲット一覧取得
eel.expose(ffc_response_target_list)
function ffc_response_target_list(target_list) {
    vm.$refs.target.set_target_list(target_list);
}
