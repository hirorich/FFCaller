// コンポーネント定義
const target_component = {
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
                        <th>時間指定</th>
                        <th>ファイル情報</th>
                        <th>ファイルパス</th>
                    </tr>
                </thead>
                <tbody v-cloak>
                    <tr v-for="(item, index) in this.target_data">
                        <th>{{index + 1}}</th>
                        <th>{{item.filename}}</th>
                        <th>{{formatTime(item.start_time)}} - {{formatTime(item.end_time)}}</th>
                        <th>
                            <button class="btn btn-primary" v-on:click="show_trim_info(item.target_id)">表示</button>
                        </th>
                        <th>
                            <button class="btn btn-primary" v-on:click="show_media_info(item.file_id)">表示</button>
                        </th>
                        <th>{{item.filepath}}</th>
                    </tr>
                </tbody>
            </table>
        </div>
    `,
    methods: {
        set_target_list: function(target_list) {
            this.target_data = target_list;
        },
        show_trim_info: function(file_id) {
            alert(file_id);
        },
        show_media_info: function(file_id) {
            let request = {file_id: file_id};
            eel.ffc_request_get_media_info(request);
        }
    }
}
