// コンポーネント定義
const trim_info = {
    components: {
        'video-player': video_player
    },
    data: function() {
        return {
            video_src: "video/input.mp4",
            frame_specification_flag : false,
            start_time: 0,
            end_time: 0,
            start_frame: 0,
            end_frame: 0,
            video_fade_in: 0,
            video_fade_out: 0,
            audio_fade_in: 0,
            audio_fade_out: 0,
            video_duration: 0
        }
    },
    template: `
        <div>
            <div class="row">
                <video-player ref="video" v-cloak class="col-12"
                    v-bind:video-src="video_src"
                    v-bind:start-time="start_time"
                    v-bind:end-time="end_time"
                    v-bind:video-fade-in="video_fade_in"
                    v-bind:video-fade-out="video_fade_out"
                    v-bind:audio-fade-in="audio_fade_in"
                    v-bind:audio-fade-out="audio_fade_out"
                    v-on:load="onLoad"></video-player>
            </div>
            <div class="form-group">
                <input type="checkbox" v-model="frame_specification_flag" class=".form-check-input position-static" v-cloak>
                <table class="table table-striped table-bordered">
                    <tbody v-cloak>
                        <tr>
                            <th class="text-white bg-dark">start_time</th>
                            <td><input v-model="start_time" type="number" class="form-control" v-bind:disabled="frame_specification_flag"></td>
                        </tr>
                        <tr>
                            <th class="text-white bg-dark">end_time</th>
                            <td><input v-model="end_time" type="number" class="form-control" v-bind:disabled="frame_specification_flag"></td>
                        </tr>
                        <tr>
                            <th class="text-white bg-dark">start_frame</th>
                            <td><input v-model="start_frame" type="number" class="form-control" v-bind:disabled="!frame_specification_flag"></td>
                        </tr>
                        <tr>
                            <th class="text-white bg-dark">end_frame</th>
                            <td><input v-model="end_frame" type="number" class="form-control" v-bind:disabled="!frame_specification_flag"></td>
                        </tr>
                        <tr>
                            <th class="text-white bg-dark">video_fade_in</th>
                            <td><input v-model="video_fade_in" type="number" class="form-control"></td>
                        </tr>
                        <tr>
                            <th class="text-white bg-dark">video_fade_out</th>
                            <td><input v-model="video_fade_out" type="number" class="form-control"></td>
                        </tr>
                        <tr>
                            <th class="text-white bg-dark">audio_fade_in</th>
                            <td><input v-model="audio_fade_in" type="number" class="form-control"></td>
                        </tr>
                        <tr>
                            <th class="text-white bg-dark">audio_fade_out</th>
                            <td><input v-model="audio_fade_out" type="number" class="form-control"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    `,
    methods: {
        onLoad: function(value) {
            this.video_duration = parseFloat(value);
            if (this.end_time <= 0) {
                this.end_time = this.video_duration;
            }
        }
    }
}
