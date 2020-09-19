// https://qiita.com/iiishokoiii/items/3037d6d01248502aee68
// http://www.htmq.com/html5/input_type_range.shtml
// https://phpjavascriptroom.com/?t=js&p=event

// コンポーネント定義
const video_player = {
    props: {

        // 動画ファイルパス
        videoSrc: {
            type: String,
            required: true
        },

        // 再生開始時間
        startTime: {
            type: Number,
            required: true
        },

        // 再生終了時間
        endTime: {
            type: Number,
            required: true
        },

        // 映像フェードイン期間
        videoFadeIn: {
            type: Number,
            default: 0
        },

        // 映像フェードアウト期間
        videoFadeOut: {
            type: Number,
            default: 0
        },

        // 音声フェードイン期間
        audioFadeIn: {
            type: Number,
            default: 0
        },

        // 音声フェードアウト期間
        audioFadeOut: {
            type: Number,
            default: 0
        }
    },
    data: function() {
        return {
            time: parseFloat(this.startTime),
            is_playing: false,
            was_playing: false,
            opacity: 1.00,
            volume: 1.00
        }
    },
    computed: {

        // 動画ソース
        video_src: function() {
            return String(this.videoSrc).trim();
        },

        // 再生開始時間
        start_time: function() {
            return parseFloat(this.startTime);
        },

        // 再生終了時間
        end_time: function() {
            return parseFloat(this.endTime);
        },

        // 映像フェードイン終了時間
        video_fadein_end_time: function() {
            return this.start_time + parseFloat(this.videoFadeIn);
        },

        // 映像フェードアウト開始時間
        video_fadeout_start_time: function() {
            return this.end_time - parseFloat(this.videoFadeOut);
        },

        // 音声フェードイン終了時間
        audio_fadein_end_time: function() {
            return this.start_time + parseFloat(this.audioFadeIn);
        },

        // 音声フェードアウト開始時間
        audio_fadeout_start_time: function() {
            return this.end_time - parseFloat(this.audioFadeOut);
        },

        // 現在時間
        current_time : function() {
            return formattime(this.time - this.start_time);
        },

        // 再生時間
        duration: function() {
            return formattime(this.end_time - this.start_time);
        }
    },
    template: `
        <div>
            <div class="row" style="margin:0;background-color:black;">
                <video ref="video"
                    class="col-12"
                    v-bind:style="{padding:0, opacity:opacity}"
                    v-on:loadeddata="onLoad()"
                    v-on:play="onPlay()"
                    v-on:pause="onPause()"
                    v-on:timeupdate="onTimeUpdate()"
                    v-bind:src="video_src">
                </video>
            </div>
            <div class="row">
                <div class="col-12">
                    <input type="range"
                        class="form-control-range"
                        v-model="time"
                        v-bind:min="start_time"
                        v-bind:max="end_time"
                        v-on:mousedown="onMouseDown()"
                        v-on:mouseup="onMouseUp()"
                        step=0.001>
                    </input>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <button v-if="is_playing" class="btn btn-primary" v-on:click="toggle_play()">停止</button>
                    <button v-else class="btn btn-primary" v-on:click="toggle_play()">再生</button>
                    <span>{{current_time}} / {{duration}}</span>
                </div>
            </div>
        </div>
    `,
    methods:{

        // 動画読み込み時ハンドラ
        onLoad: function() {
            this.$refs.video.currentTime = this.start_time;
            this.$emit('load', this.$refs.video.duration);
        },

        // 動画再生時ハンドラ
        onPlay: function() {
            this.is_playing = true;
        },

        // 動画停止時ハンドラ
        onPause: function() {
            this.is_playing = false;
        },

        // 再生中動画位置ハンドラ
        onTimeUpdate: function() {
            if (this.is_playing) {
                this.time = this.$refs.video.currentTime;
            }
        },

        // シーク中ハンドラ
        onMouseDown: function() {
            if (this.is_playing) {
                this.was_playing = true;
            }
            this.pause();
        },

        // シーク終了ハンドラ
        onMouseUp: function() {
            if (this.was_playing) {
                this.play();
            }
            this.was_playing = false;
        },

        // 動画再生
        play: function() {
            this.$refs.video.play();
        },

        // 動画停止
        pause: function() {
            this.$refs.video.pause();
        },

        // 動画再生・停止切り替え
        toggle_play: function() {
            if (!this.is_playing) {
                this.play();
            } else {
                this.pause();
            }
        }
    },
    watch: {
        start_time: function(value) {
            if (this.time < value) {
                this.time = value;
                this.$refs.video.currentTime = value;
            }
        },
        end_time: function(value) {
            if (this.time > value) {
                this.time = value;
                this.$refs.video.currentTime = value;
            }
        },

        // 再生位置制御
        time: function(value) {
            if (value < this.start_time) {
                this.$refs.video.currentTime = this.start_time;
            } else if (value >= this.end_time) {
                this.pause();
                this.$refs.video.currentTime = this.end_time;
            } else if (!this.is_playing) {
                this.$refs.video.currentTime = value;
            }

            // videoフェードイン・フェードアウト
            if (value < this.video_fadein_end_time) {
                this.opacity = (value - this.start_time) / (this.video_fadein_end_time - this.start_time);
            } else if (this.video_fadeout_start_time < value) {
                this.opacity = (this.end_time - value) / (this.end_time - this.video_fadeout_start_time);
            } else {
                this.opacity = 1.00;
            }

            // audioフェードイン・フェードアウト
            if (value < this.audio_fadein_end_time) {
                this.volume = (value - this.start_time) / (this.audio_fadein_end_time - this.start_time);
            } else if (this.audio_fadeout_start_time < value) {
                this.volume = (this.end_time - value) / (this.end_time - this.audio_fadeout_start_time);
            } else {
                this.volume = 1.00;
            }
        },

        // 音量制御
        volume: function(value) {
            this.$refs.video.volume = value;
        }
    }
}
