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
                        <th>開始時間</th>
                        <th>切り取り時間</th>
                        <th>時間指定</th>
                        <th>ファイル情報</th>
                        <th>ファイルパス</th>
                    </tr>
                </thead>
                <tbody v-cloak>
                    <tr v-for="(item, index) in this.target_data">
                        <th>{{index + 1}}</th>
                        <th>{{item.filename}}</th>
                        <th>{{item.start_time}}</th>
                        <th>{{item.trim_duration}}</th>
                        <th>{{item.target_id}}</th>
                        <th>{{item.file_id}}</th>
                        <th>{{item.filepath}}</th>
                    </tr>
                </tbody>
            </table>
        </div>
    `,
    methods: {
        set_target_list: function(target_list) {
            this.target_data = target_list;
        }
    }
}
