// コンポーネント定義
const trim_info_component = {
    components: {
        'media-player-component': media_player_component
    },
    data: function() {
        return {
            guid: String($.guid),
            media_src: '',
            with_video: true,
            with_audio: true,
            frame_input_flag : false,
            r_frame_rate_numer: 1,
            r_frame_rate_denom: 0,
            media_duration: 0,
            nb_frames: 0,
            is_fade_from_white : false,
            is_fade_to_white : false,
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
            work_start_frame: 0,
            work_end_frame: 0,
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
            valid = valid && (this.work_start_time < this.work_end_time);
            valid = valid && (this.work_end_time <= this.media_duration);

            // フラグにより時間算出
            let start_time = this.work_start_time;
            let end_time = this.work_end_time;
            if (this.frame_input_flag) {
                if (this.r_frame_rate_numer < 1) {
                    return false;
                }
                valid = valid && (1 <= this.work_start_frame);
                valid = valid && (this.work_start_frame < this.work_end_frame);
                valid = valid && (this.work_end_frame <= this.nb_frames);
                let work_time = this.frame_to_time(this.work_start_frame, this.work_end_frame);
                start_time = work_time.start_time;
                end_time = work_time.end_time;
            }

            // 映像ありの場合
            if (this.with_video) {
                let video_fade_in_time = start_time + this.work_video_fade_in;
                let video_fade_out_time = end_time - this.work_video_fade_out;
                valid = valid && (start_time <= video_fade_in_time);
                valid = valid && (video_fade_in_time <= video_fade_out_time);
                valid = valid && (video_fade_out_time <= end_time);
            }

            // 音声ありの場合
            if (this.with_audio) {
                let audio_fade_in_time = start_time + this.work_audio_fade_in;
                let audio_fade_out_time = end_time - this.work_audio_fade_out;
                valid = valid && (start_time <= audio_fade_in_time);
                valid = valid && (audio_fade_in_time <= audio_fade_out_time);
                valid = valid && (audio_fade_out_time <= end_time);
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
                        <input type="checkbox" v-bind:id="[guid + '-frame-check']" v-model="frame_input_flag" class="form-check-input">
                        <label v-bind:for="[guid + '-frame-check']">フレーム指定</label>
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">start_time</label>
                    <div class="form-group col-8">
                        <input v-model="in_start_time" v-on:blur="onBlurStartTime()" type="number" step=0.001 class="form-control" v-bind:disabled="frame_input_flag">
                    </div>
                </div>
                <div class="form-row">
                    <label class="col-4">end_time</label>
                    <div class="form-group col-8">
                        <input v-model="in_end_time" v-on:blur="onBlurEndTime()" type="number" step=0.001 class="form-control" v-bind:disabled="frame_input_flag">
                    </div>
                </div>
                <div v-if="with_video" class="form-row">
                    <label class="col-4">start_frame</label>
                    <div class="form-group col-8">
                        <input v-model="in_start_frame" v-on:blur="onBlurStartFrame()" type="number" step=1 class="form-control" v-bind:disabled="!frame_input_flag">
                    </div>
                </div>
                <div v-if="with_video" class="form-row">
                    <label class="col-4">end_frame</label>
                    <div class="form-group col-8">
                        <input v-model="in_end_frame" v-on:blur="onBlurEndFrame()" type="number" step=1 class="form-control" v-bind:disabled="!frame_input_flag">
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
                <div v-if="with_video" class="form-row">
                    <div class="form-group col-6">
                        <div class="form-check">
                            <input type="checkbox" v-bind:id="[guid + '-fade-from-check']" v-model="is_fade_from_white" class="form-check-input">
                            <label v-bind:for="[guid + '-fade-from-check']">白からフェードイン</label>
                        </div>
                    </div>
                    <div class="form-group col-6">
                        <div class="form-check">
                            <input type="checkbox" v-bind:id="[guid + '-fade-to-check']" v-model="is_fade_to_white" class="form-check-input">
                            <label v-bind:for="[guid + '-fade-to-check']">白へフェードアウト</label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {

        // 切り取り情報設定
        set_trim_info: function(info) {

            // 動画ファイルパス
            let media_src = "";
            try {
                media_src = String(info.webpath).trim();
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
            let frame_input_flag = false;
            try {
                frame_input_flag = info.trim.frame_input_flag;
            } catch(e) {}
            if (typeof(frame_input_flag) != "boolean") {
                frame_input_flag = false;
            }
            this.frame_input_flag = frame_input_flag;

            // フレームレート(分子)
            let r_frame_rate_numer = 1;
            try {
                r_frame_rate_numer = info.r_frame_rate_numer;
            } catch(e) {}
            this.r_frame_rate_numer = r_frame_rate_numer;

            // フレームレート(分母)
            let r_frame_rate_denom = 0;
            try {
                r_frame_rate_denom = info.r_frame_rate_denom;
            } catch(e) {}
            this.r_frame_rate_denom = r_frame_rate_denom;

            // 再生時間
            let media_duration = 0;
            try {
                media_duration = convertFloat(info.duration);
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
                start_time = convertFloat(info.trim.start_time);
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
                end_time = convertFloat(info.trim.end_time);
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
                in_start_frame = parseInt(info.trim.start_frame);
            } catch(e) {}
            if (isNaN(in_start_frame) || in_start_frame < 0) {
                in_start_frame = 0;
            }
            this.in_start_frame = in_start_frame;
            this.work_start_frame = in_start_frame;

            // 再生終了フレーム
            let in_end_frame = 0;
            try {
                in_end_frame = parseInt(info.trim.end_frame);
            } catch(e) {}
            if (isNaN(in_end_frame) || in_end_frame < 0 || this.nb_frames < in_end_frame) {
                in_end_frame = this.nb_frames;
            }
            this.in_end_frame = in_end_frame;
            this.work_end_frame = in_end_frame;

            // 映像フェードイン期間
            let video_fade_in = 0;
            try {
                video_fade_in = convertFloat(info.trim.video_fade_in);
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
                video_fade_out = convertFloat(info.trim.video_fade_out);
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
                audio_fade_in = convertFloat(info.trim.audio_fade_in);
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
                audio_fade_out = convertFloat(info.trim.audio_fade_out);
            } catch(e) {}
            if (isNaN(audio_fade_out) || audio_fade_out < 0) {
                audio_fade_out = 0;
            }
            this.in_audio_fade_out = audio_fade_out;
            this.out_audio_fade_out = audio_fade_out;
            this.work_audio_fade_out = audio_fade_out;

            // フェードイン色
            let is_fade_from_white = false;
            try {
                is_fade_from_white = info.trim.is_fade_from_white;
            } catch(e) {}
            if (typeof(is_fade_from_white) != "boolean") {
                is_fade_from_white = false;
            }
            this.is_fade_from_white = is_fade_from_white;

            // フェードアウト色
            let is_fade_to_white = false;
            try {
                is_fade_to_white = info.trim.is_fade_to_white;
            } catch(e) {}
            if (typeof(is_fade_to_white) != "boolean") {
                is_fade_to_white = false;
            }
            this.is_fade_to_white = is_fade_to_white;

            // 再生位置の初期化
            this.$refs.media.showMedia();
        },

        // 切り取り情報取得
        get_trim_info: function() {
            return {
                frame_input_flag: this.frame_input_flag,
                start_time: this.work_start_time,
                end_time: this.work_end_time,
                start_frame: this.work_start_frame,
                end_frame: this.work_end_frame,
                video_fade_in: this.work_video_fade_in,
                video_fade_out: this.work_video_fade_out,
                audio_fade_in: this.work_audio_fade_in,
                audio_fade_out: this.work_audio_fade_out,
                is_fade_from_white: this.is_fade_from_white,
                is_fade_to_white: this.is_fade_to_white
            }
        },

        // フレームから時間を算出
        frame_to_time: function(start_frame, end_frame) {
            return convertFrameToTime(start_frame, end_frame, this.r_frame_rate_numer, this.r_frame_rate_denom);
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
            let prev_start_time = this.work_start_time;
            this.work_start_time = convertFloat(this.in_start_time);
            if (isNaN(this.work_start_time) || !this.validation) {
                this.in_start_time = prev_start_time;
                this.work_start_time = prev_start_time;
                return;
            }
            this.in_start_time = this.work_start_time;
            this.out_start_time = this.work_start_time;
        },

        // 再生終了時間
        onBlurEndTime: function() {
            let prev_end_time = this.work_end_time;
            this.work_end_time = convertFloat(this.in_end_time);
            if (isNaN(this.work_end_time) || !this.validation) {
                this.in_end_time = prev_end_time;
                this.work_end_time = prev_end_time;
                return;
            }
            this.in_end_time = this.work_end_time;
            this.out_end_time = this.work_end_time;
        },

        // 再生開始フレーム
        onBlurStartFrame: function() {
            let prev_start_frame = this.work_start_frame;
            this.work_start_frame = parseInt(this.in_start_frame);
            if ((this.r_frame_rate_numer < 1) || isNaN(this.work_start_frame) || !this.validation) {
                this.in_start_frame = prev_start_frame;
                this.work_start_frame = prev_start_frame;
                return;
            }
            this.in_start_frame = this.work_start_frame;
            this.out_start_time = this.frame_to_time(this.work_start_frame, this.work_end_frame).start_time;
        },

        // 再生終了フレーム
        onBlurEndFrame: function() {
            let prev_end_frame = this.work_end_frame;
            this.work_end_frame = parseInt(this.in_end_frame);
            if ((this.r_frame_rate_numer < 1) || isNaN(this.work_end_frame) || !this.validation) {
                this.in_end_frame = prev_end_frame;
                this.work_end_frame = prev_end_frame;
                return;
            }
            this.in_end_frame = this.work_end_frame;
            this.out_end_time = this.frame_to_time(this.work_start_frame, this.work_end_frame).end_time;
        },

        // 映像フェードイン期間
        onBlurVideoFadeIn: function() {
            let prev_video_fade_in = this.work_video_fade_in;
            this.work_video_fade_in = convertFloat(this.in_video_fade_in);
            if (isNaN(this.work_video_fade_in) || !this.validation) {
                this.in_video_fade_in = prev_video_fade_in;
                this.work_video_fade_in = prev_video_fade_in;
                return;
            }
            this.in_video_fade_in = this.work_video_fade_in;
            this.out_video_fade_in = this.work_video_fade_in;
        },

        // 映像フェードアウト期間
        onBlurVideoFadeOut: function() {
            let prev_video_fade_out = this.work_video_fade_out;
            this.work_video_fade_out = convertFloat(this.in_video_fade_out);
            if (isNaN(this.work_video_fade_out) || !this.validation) {
                this.in_video_fade_out = prev_video_fade_out;
                this.work_video_fade_out = prev_video_fade_out;
                return;
            }
            this.in_video_fade_out = this.work_video_fade_out;
            this.out_video_fade_out = this.work_video_fade_out;
        },

        // 音声フェードイン期間
        onBlurAudioFadeIn: function() {
            let prev_audio_fade_in = this.work_audio_fade_in;
            this.work_audio_fade_in = convertFloat(this.in_audio_fade_in);
            if (isNaN(this.work_audio_fade_in) || !this.validation) {
                this.in_audio_fade_in = prev_audio_fade_in;
                this.work_audio_fade_in = prev_audio_fade_in;
                return;
            }
            this.in_audio_fade_in = this.work_audio_fade_in;
            this.out_audio_fade_in = this.work_audio_fade_in;
        },

        // 音声フェードアウト期間
        onBlurAudioFadeOut: function() {
            let prev_audio_fade_out = this.work_audio_fade_out;
            this.work_audio_fade_out = convertFloat(this.in_audio_fade_out);
            if (isNaN(this.work_audio_fade_out) || !this.validation) {
                this.in_audio_fade_out = prev_audio_fade_out;
                this.work_audio_fade_out = prev_audio_fade_out;
                return;
            }
            this.in_audio_fade_out = this.work_audio_fade_out;
            this.out_audio_fade_out = this.work_audio_fade_out;
        }
    },
    watch: {
        frame_input_flag: function(value) {
            if (value) {
                this.onBlurStartFrame();
                this.onBlurEndFrame();
            } else {
                this.onBlurStartTime();
                this.onBlurEndTime();
            }
        }
    }
}
