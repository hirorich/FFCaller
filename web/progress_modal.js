// 定義したコンポーネントを登録
const vm_progress = new Vue({
    el: '#progress-components',
    components: {
        'modal-component': modal_component
    },
    data: function() {
        return {
            work_progress: 0,
            is_processing: true
        }
    },
    computed: {
        progress: function() {
            if (this.work_progress >= 100) {
                return 100;
            } else {
                return convertFloat(this.work_progress, 1);
            }
        }
    },
    template: `
        <div>
            <modal-component ref="modal">
                <p slot="title" class="h4 text-primary">Progress</p>
                <div class="progress" slot="body">
                    <div v-bind:class="['progress-bar progress-bar-striped', {'progress-bar-animated': is_processing}]" v-bind:style="{ width: progress + '%' }">{{this.progress}}%</div>
                </div>
                <button v-if="!is_processing" slot="button" class="btn btn-success" v-on:click="hide_modal()">完了</button>
            </modal-component>
        <div>
    `,
    methods: {
        show_modal: function() {
            this.$refs.modal.show_modal();
        },
        hide_modal: function() {
            this.$refs.modal.hide_modal();
        },
        change_progress: function(value) {
            this.work_progress = value;
        },
        start_processing: function() {
            this.is_processing = true;
        },
        end_processing: function() {
            this.is_processing = false;
        }
    }
});

// 進行度変更
eel.expose(ffc_start_vm_progress)
function ffc_start_vm_progress() {
    vm_progress.change_progress(0);
    vm_progress.start_processing();
    vm_progress.show_modal();
}

// 進行度変更
eel.expose(ffc_end_vm_progress)
function ffc_end_vm_progress() {
    vm_progress.change_progress(100);
    vm_progress.end_processing();
}

// 進行度変更
eel.expose(ffc_change_vm_progress)
function ffc_change_vm_progress(response) {
    vm_progress.change_progress(response);
}
