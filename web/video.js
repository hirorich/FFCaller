// 小数点以下3桁のFloat型に変換
const convertFloat = function(value) {
    let work_value = parseFloat(value);
    if (isNaN(work_value)) {
        return NaN;
    } else if (String(work_value) != String(value)) {
        return NaN;
    }

    try {
        return parseInt(work_value * 1000) / 1000;
    } catch(e) {
        return NaN;
    }
};

// 表示形式変換
const formattime = function(value) {
    let formatted = '--:--:--.---';
    try {
        let date = new Date(value * 1000);
        let HH = date.getUTCHours();
        let mm = ('00' + date.getUTCMinutes()).slice(-2);
        let ss = ('00' + date.getUTCSeconds()).slice(-2);
        let fff = ('000' + date.getUTCMilliseconds()).slice(-3);
        formatted = HH + ':' + mm + ':' + ss + '.' + fff;
    } catch(e) {}
    return formatted;
};

// 定義したコンポーネントを登録
const vm = new Vue({
    el: '#ffcaller-components',
    components: {
        'modal-component': modal_component,
        'video-trim': video_trim,
        'video-info': video_info
    },
    template: `
        <div>
            <button class="btn btn-primary" v-on:click="show_trim_modal()">範囲選択を開く</button>
            <button class="btn btn-primary" v-on:click="show_video_modal()">動画情報を開く</button>
            <modal-component ref="trim_modal">
                <p slot="title" class="h4 text-primary">範囲選択</p>
                <video-trim ref="trim" slot="body"
                    video-src="video/input.mp4"
                ></video-trim>
                <button slot="button" class="btn btn-primary" v-on:click="save_trim()">保存</button>
            </modal-component>
            <modal-component ref="video_modal">
                <p slot="title" class="h4 text-primary">動画情報</p>
                <video-info ref="info" slot="body"></video-info>
            </modal-component>
        <div>
    `,
    methods: {
        show_trim_modal: function() {
            this.$refs.trim_modal.show_modal();
        },
        save_trim: function() {
            this.$refs.trim_modal.close_modal();
        },
        show_video_modal: function() {
            this.$refs.video_modal.show_modal();
        }
    }
});
