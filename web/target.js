const draggable = window['vuedraggable'];

// コンポーネント定義
const target_component = {
    components: {
        'draggable': draggable
    },
    data: function() {
        return {
            target_data: []
        }
    },
    template: `
        <div>
            <table class="table table-striped table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th>No.</th>
                        <th>ファイル名</th>
                        <th>時間</th>
                        <th>編集</th>
                        <th>ファイルパス</th>
                    </tr>
                </thead>
                <draggable tag="tbody" v-cloak>
                    <tr v-for="(item, index) in this.target_data" :key="item.target_id">
                        <th>{{index + 1}}</th>
                        <th>{{item.filename}}</th>
                        <th>{{formatTime(item.start_time)}} - {{formatTime(item.end_time)}}</th>
                        <th>
                            <button class="btn btn-primary" v-on:click="show_trim_info(item.target_id)">時間指定</button>
                            <button class="btn btn-primary" v-on:click="show_media_info(item.target_id)">ファイル情報</button>
                            <button class="btn btn-secondary" v-on:click="delete_target(item.target_id)">削除</button>
                        </th>
                        <th>{{item.filepath}}</th>
                    </tr>
                </draggable>
            </table>
            <button v-if="target_data.length > 0" class="btn btn-primary" v-on:click="marge()">マージ</button>
        </div>
    `,
    methods: {
        set_target_list: function(target_list) {
            this.target_data = target_list;
        },
        show_trim_info: function(target_id) {
            let request = {target_id: target_id};
            eel.ffc_request_get_trim_info(request);
        },
        show_media_info: function(target_id) {
            let request = {target_id: target_id};
            eel.ffc_request_get_media_info(request);
        },
        delete_target: function(target_id) {
            let request = {target_id: target_id};
            eel.ffc_request_delete_target(request);
        },
        marge: function() {
            eel.ffc_request_marge();
        }
    }
}
