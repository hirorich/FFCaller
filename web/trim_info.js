// 小数点以下3桁のFloat型に変換
let convertFloat = function(value) {
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

// コンポーネント定義
const trim_info = {
    components: {
        'video-player': video_player
    },
    data: function() {
        return {
            video_src: "video/input.mp4",
            frame_specification_flag : false,
            video_duration: 0,
            in_start_time: 0,
            in_end_time: 0,
            in_start_frame: 0,
            in_end_frame: 0,
            in_video_fade_in: 0,
            in_video_fade_out: 0,
            in_audio_fade_in: 0,
            in_audio_fade_out: 0,
            out_start_time: 0,
            out_end_time: 0,
            out_video_fade_in: 0,
            out_video_fade_out: 0,
            out_audio_fade_in: 0,
            out_audio_fade_out: 0
        }
    },
    template: `
        <div>
            <div class="row">
                <video-player ref="video" class="col-12"
                    v-bind:video-src="video_src"
                    v-bind:start-time="out_start_time"
                    v-bind:end-time="out_end_time"
                    v-bind:video-fade-in="out_video_fade_in"
                    v-bind:video-fade-out="out_video_fade_out"
                    v-bind:audio-fade-in="out_audio_fade_in"
                    v-bind:audio-fade-out="out_audio_fade_out"
                    v-on:load="onLoad"></video-player>
            </div>
            <div>
                <div class="form-group">
                    <div class="form-check">
                        <input type="checkbox" v-model="frame_specification_flag" class="form-check-input position-static">
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">start_time</label>
                    <div class="form-group col-8">
                        <input v-model="in_start_time" v-on:blur="onBlurStartTime()" type="number" step=0.001 class="form-control" v-bind:disabled="frame_specification_flag">
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">end_time</label>
                    <div class="form-group col-8">
                        <input v-model="in_end_time" v-on:blur="onBlurEndTime()" type="number" step=0.001 class="form-control" v-bind:disabled="frame_specification_flag">
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">start_frame</label>
                    <div class="form-group col-8">
                        <input v-model="in_start_frame" v-on:blur="onBlurStartFrame()" type="number" step=1 class="form-control" v-bind:disabled="!frame_specification_flag">
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">end_frame</label>
                    <div class="form-group col-8"">
                        <input v-model="in_end_frame" v-on:blur="onBlurEndFrame()" type="number" step=1 class="form-control" v-bind:disabled="!frame_specification_flag">
                    </div>
                </div>
                <div class="form-row">
                    <lebel class="col-4">video_fade_in</lebel>
                    <div class="form-group col-8">
                        <input v-model="in_video_fade_in" v-on:blur="onBlurVideoFadeIn()" type="number" step=0.001 class="form-control">
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">video_fade_out</label>
                    <div class="form-group col-8">
                        <input v-model="in_video_fade_out" v-on:blur="onBlurVideoFadeOut()" type="number" step=0.001 class="form-control">
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">audio_fade_in</label>
                    <div class="form-group col-8">
                        <input v-model="in_audio_fade_in" v-on:blur="onBlurAudioFadeIn()" type="number" step=0.001 class="form-control">
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">audio_fade_out</label>
                    <div class="form-group col-8">
                        <input v-model="in_audio_fade_out" v-on:blur="onBlurAudioFadeOut()" type="number" step=0.001 class="form-control">
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {
        onLoad: function(value) {
            this.video_duration = convertFloat(value);
            if (this.out_end_time <= 0) {
                this.in_end_time = this.video_duration;
                this.out_end_time = this.video_duration;
            }
        },
        onBlurStartTime: function() {
            let work_start_time = convertFloat(this.in_start_time);
            if (isNaN(work_start_time)) {
                this.in_start_time = this.out_start_time;
                return;
            }
            this.in_start_time = work_start_time;
            this.out_start_time = work_start_time;
        },
        onBlurEndTime: function() {
            let work_end_time = convertFloat(this.in_end_time);
            if (isNaN(work_end_time)) {
                this.in_end_time = this.out_end_time;
                return;
            }
            this.in_end_time = work_end_time;
            this.out_end_time = work_end_time;
        },
        onBlurStartFrame: function() {},
        onBlurEndFrame: function() {},
        onBlurVideoFadeIn: function() {
            let work_video_fade_in = convertFloat(this.in_video_fade_in);
            if (isNaN(work_video_fade_in)) {
                this.in_video_fade_in = this.out_video_fade_in;
                return;
            }
            this.in_video_fade_in = work_video_fade_in;
            this.out_video_fade_in = work_video_fade_in;
        },
        onBlurVideoFadeOut: function() {
            let work_video_fade_out = convertFloat(this.in_video_fade_out);
            if (isNaN(work_video_fade_out)) {
                this.in_video_fade_out = this.out_video_fade_out;
                return;
            }
            this.in_video_fade_out = work_video_fade_out;
            this.out_video_fade_out = work_video_fade_out;
        },
        onBlurAudioFadeIn: function() {
            let work_audio_fade_in = convertFloat(this.in_audio_fade_in);
            if (isNaN(work_audio_fade_in)) {
                this.in_audio_fade_in = this.out_audio_fade_in;
                return;
            }
            this.in_audio_fade_in = work_audio_fade_in;
            this.out_audio_fade_in = work_audio_fade_in;
        },
        onBlurAudioFadeOut: function() {
            let work_audio_fade_out = convertFloat(this.in_audio_fade_out);
            if (isNaN(work_audio_fade_out)) {
                this.in_audio_fade_out = this.out_audio_fade_out;
                return;
            }
            this.in_audio_fade_out = work_audio_fade_out;
            this.out_audio_fade_out = work_audio_fade_out;
        }
    }
}
