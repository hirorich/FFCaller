// コンポーネント定義
const media_trim_component = {
    components: {
        'media-player-component': media_player_component
    },
    data: function() {
        return {
            guid: String($.guid),
            media_src: '',
            with_video: true,
            with_audio: true,
            frame_specification_flag : false,
            media_duration: 0,
            nb_frames: 0,
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
            out_audio_fade_out: 0,
            work_start_time: 0,
            work_end_time: 0,
            work_video_fade_in: 0,
            work_video_fade_out: 0,
            work_audio_fade_in: 0,
            work_audio_fade_out: 0
        }
    },
    computed :{

        // 入力値検証
        validation: function() {
            let valid = true;
            valid = valid && (0 <= this.work_start_time);
            valid = valid && (this.work_start_time <= this.work_end_time);
            valid = valid && (this.work_end_time <= this.media_duration);

            // 映像ありの場合
            if (this.with_video) {
                let video_fade_in_time = this.work_start_time + this.work_video_fade_in;
                let video_fade_out_time = this.work_end_time - this.work_video_fade_out;
                valid = valid && (this.work_start_time <= video_fade_in_time);
                valid = valid && (video_fade_in_time <= video_fade_out_time);
                valid = valid && (video_fade_out_time <= this.work_end_time);
            }

            // 音声ありの場合
            if (this.with_audio) {
                let audio_fade_in_time = this.work_start_time + this.work_audio_fade_in;
                let audio_fade_out_time = this.work_end_time - this.work_audio_fade_out;
                valid = valid && (this.work_start_time <= audio_fade_in_time);
                valid = valid && (audio_fade_in_time <= audio_fade_out_time);
                valid = valid && (audio_fade_out_time <= this.work_end_time);
            }

            return valid;
        }
    },
    template: `
        <div>
            <div class="row">
                <media-player-component ref="media" class="col-12"
                    v-bind:media-src="media_src"
                    v-bind:with-video="with_video"
                    v-bind:with-audio="with_audio"
                    v-bind:start-time="out_start_time"
                    v-bind:end-time="out_end_time"
                    v-bind:video-fade-in="out_video_fade_in"
                    v-bind:video-fade-out="out_video_fade_out"
                    v-bind:audio-fade-in="out_audio_fade_in"
                    v-bind:audio-fade-out="out_audio_fade_out"
                    v-on:load="onMediaLoad"></media-player-component>
            </div>
            <div v-cloak>
                <div v-if="with_video" class="form-group">
                    <div class="form-check">
                        <input type="checkbox" v-bind:id="[guid + '-check']" v-model="frame_specification_flag" class="form-check-input">
                        <label v-bind:for="[guid + '-check']">フレーム指定</label>
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
                <div v-if="with_video" class="form-row">
                    <label class="col-4">start_frame</label>
                    <div class="form-group col-8">
                        <input v-model="in_start_frame" v-on:blur="onBlurStartFrame()" type="number" step=1 class="form-control" v-bind:disabled="!frame_specification_flag">
                    </div>
                </div>
                <div v-if="with_video" class="form-row">
                    <label class="col-4">end_frame</label>
                    <div class="form-group col-8"">
                        <input v-model="in_end_frame" v-on:blur="onBlurEndFrame()" type="number" step=1 class="form-control" v-bind:disabled="!frame_specification_flag">
                    </div>
                </div>
                <div v-if="with_video" class="form-row">
                    <lebel class="col-4">video_fade_in</lebel>
                    <div class="form-group col-8">
                        <input v-model="in_video_fade_in" v-on:blur="onBlurVideoFadeIn()" type="number" step=0.001 class="form-control">
                    </div>
                </div>
                <div v-if="with_video" class="form-row">
                    <label class="col-4">video_fade_out</label>
                    <div class="form-group col-8">
                        <input v-model="in_video_fade_out" v-on:blur="onBlurVideoFadeOut()" type="number" step=0.001 class="form-control">
                    </div>
                </div>
                <div v-if="with_audio" class="form-row">
                    <label class="col-4">audio_fade_in</label>
                    <div class="form-group col-8">
                        <input v-model="in_audio_fade_in" v-on:blur="onBlurAudioFadeIn()" type="number" step=0.001 class="form-control">
                    </div>
                </div>
                <div v-if="with_audio" class="form-row">
                    <label class="col-4">audio_fade_out</label>
                    <div class="form-group col-8">
                        <input v-model="in_audio_fade_out" v-on:blur="onBlurAudioFadeOut()" type="number" step=0.001 class="form-control">
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {

        // 切り取り情報設定
        set_media_trim: function(info) {

            // 動画ファイルパス
            let media_src = "";
            try {
                media_src = String(info.media_src).trim();
            } catch(e) {}
            this.media_src = media_src;

            // 映像有無
            let with_video = true;
            try {
                with_video = info.with_video;
            } catch(e) {}
            if (typeof(with_video) != "boolean") {
                with_video = true;
            }
            this.with_video = with_video;

            // 音声有無
            let with_audio = true;
            try {
                with_audio = info.with_audio;
            } catch(e) {}
            if (typeof(with_audio) != "boolean") {
                with_audio = true;
            }
            this.with_audio = with_audio;

            // フレーム指定有無
            let frame_specification_flag = false;
            try {
                frame_specification_flag = info.frame_specification_flag;
            } catch(e) {}
            if (typeof(frame_specification_flag) != "boolean") {
                frame_specification_flag = false;
            }
            this.frame_specification_flag = frame_specification_flag;

            // 再生時間
            let media_duration = 0;
            try {
                media_duration = convertFloat(info.media_duration);
            } catch(e) {}
            if (isNaN(media_duration) || media_duration < 0) {
                media_duration = 0;
            }
            this.media_duration = media_duration;

            // フレーム数
            let nb_frames = 0;
            try {
                nb_frames = parseInt(info.nb_frames);
            } catch(e) {}
            if (isNaN(nb_frames) || nb_frames < 0) {
                nb_frames = 0;
            }
            this.nb_frames = nb_frames;

            // 再生開始時間
            let start_time = 0;
            try {
                start_time = convertFloat(info.start_time);
            } catch(e) {}
            if (isNaN(start_time) || start_time < 0) {
                start_time = 0;
            }
            this.in_start_time = start_time;
            this.out_start_time = start_time;
            this.work_start_time = start_time;

            // 再生終了時間
            let end_time = 0;
            try {
                end_time = convertFloat(info.end_time);
            } catch(e) {}
            if (isNaN(end_time) || end_time < 0 || this.media_duration < end_time) {
                end_time = this.media_duration;
            }
            this.in_end_time = end_time;
            this.out_end_time = end_time;
            this.work_end_time = end_time;

            // 再生開始フレーム
            let in_start_frame = 0;
            try {
                in_start_frame = parseInt(info.start_frame);
            } catch(e) {}
            if (isNaN(in_start_frame) || in_start_frame < 0) {
                in_start_frame = 0;
            }
            this.in_start_frame = in_start_frame;

            // 再生終了フレーム
            let in_end_frame = 0;
            try {
                in_end_frame = parseInt(info.end_frame);
            } catch(e) {}
            if (isNaN(in_end_frame) || in_end_frame < 0 || this.nb_frames < in_end_frame) {
                in_end_frame = this.nb_frames;
            }
            this.in_end_frame = in_end_frame;

            // 映像フェードイン期間
            let video_fade_in = 0;
            try {
                video_fade_in = convertFloat(info.video_fade_in);
            } catch(e) {}
            if (isNaN(video_fade_in) || video_fade_in < 0) {
                video_fade_in = 0;
            }
            this.in_video_fade_in = video_fade_in;
            this.out_video_fade_in = video_fade_in;
            this.work_video_fade_in = video_fade_in;

            // 映像フェードアウト期間
            let video_fade_out = 0;
            try {
                video_fade_out = convertFloat(info.video_fade_out);
            } catch(e) {}
            if (isNaN(video_fade_out) || video_fade_out < 0) {
                video_fade_out = 0;
            }
            this.in_video_fade_out = video_fade_out;
            this.out_video_fade_out = video_fade_out;
            this.work_video_fade_out = video_fade_out;

            // 音声フェードイン期間
            let audio_fade_in = 0;
            try {
                audio_fade_in = convertFloat(info.audio_fade_in);
            } catch(e) {}
            if (isNaN(audio_fade_in) || audio_fade_in < 0) {
                audio_fade_in = 0;
            }
            this.in_audio_fade_in = audio_fade_in;
            this.out_audio_fade_in = audio_fade_in;
            this.work_audio_fade_in = audio_fade_in;

            // 音声フェードアウト期間
            let audio_fade_out = 0;
            try {
                audio_fade_out = convertFloat(info.audio_fade_out);
            } catch(e) {}
            if (isNaN(audio_fade_out) || audio_fade_out < 0) {
                audio_fade_out = 0;
            }
            this.in_audio_fade_out = audio_fade_out;
            this.out_audio_fade_out = audio_fade_out;
            this.work_audio_fade_out = audio_fade_out;

            // 再生位置の初期化
            this.$refs.media.initTime(this.out_start_time);
        },

        // 動画読み込み時ハンドラ
        onMediaLoad: function(value) {
            if (this.work_end_time <= 0) {
                this.media_duration = convertFloat(value);
                this.in_end_time = this.media_duration;
                this.out_end_time = this.media_duration;
                this.work_end_time = this.media_duration;
            }
        },

        // 再生開始時間
        onBlurStartTime: function() {
            this.work_start_time = convertFloat(this.in_start_time);
            if (isNaN(this.work_start_time) || !this.validation) {
                this.in_start_time = this.out_start_time;
                this.work_start_time = this.out_start_time;
                return;
            }
            this.in_start_time = this.work_start_time;
            this.out_start_time = this.work_start_time;
        },

        // 再生終了時間
        onBlurEndTime: function() {
            this.work_end_time = convertFloat(this.in_end_time);
            if (isNaN(this.work_end_time) || !this.validation) {
                this.in_end_time = this.out_end_time;
                this.work_end_time = this.out_end_time;
                return;
            }
            this.in_end_time = this.work_end_time;
            this.out_end_time = this.work_end_time;
        },

        // 再生開始フレーム
        onBlurStartFrame: function() {},

        // 再生終了フレーム
        onBlurEndFrame: function() {},

        // 映像フェードイン期間
        onBlurVideoFadeIn: function() {
            this.work_video_fade_in = convertFloat(this.in_video_fade_in);
            if (isNaN(this.work_video_fade_in) || !this.validation) {
                this.in_video_fade_in = this.out_video_fade_in;
                this.work_video_fade_in = this.out_video_fade_in;
                return;
            }
            this.in_video_fade_in = this.work_video_fade_in;
            this.out_video_fade_in = this.work_video_fade_in;
        },

        // 映像フェードアウト期間
        onBlurVideoFadeOut: function() {
            this.work_video_fade_out = convertFloat(this.in_video_fade_out);
            if (isNaN(this.work_video_fade_out) || !this.validation) {
                this.in_video_fade_out = this.out_video_fade_out;
                this.work_video_fade_out = this.out_video_fade_out;
                return;
            }
            this.in_video_fade_out = this.work_video_fade_out;
            this.out_video_fade_out = this.work_video_fade_out;
        },

        // 音声フェードイン期間
        onBlurAudioFadeIn: function() {
            this.work_audio_fade_in = convertFloat(this.in_audio_fade_in);
            if (isNaN(this.work_audio_fade_in) || !this.validation) {
                this.in_audio_fade_in = this.out_audio_fade_in;
                this.work_audio_fade_in = this.out_audio_fade_in;
                return;
            }
            this.in_audio_fade_in = this.work_audio_fade_in;
            this.out_audio_fade_in = this.work_audio_fade_in;
        },

        // 音声フェードアウト期間
        onBlurAudioFadeOut: function() {
            this.work_audio_fade_out = convertFloat(this.in_audio_fade_out);
            if (isNaN(this.work_audio_fade_out) || !this.validation) {
                this.in_audio_fade_out = this.out_audio_fade_out;
                this.work_audio_fade_out = this.out_audio_fade_out;
                return;
            }
            this.in_audio_fade_out = this.work_audio_fade_out;
            this.out_audio_fade_out = this.work_audio_fade_out;
        }
    }
}
