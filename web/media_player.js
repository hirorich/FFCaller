// https://qiita.com/iiishokoiii/items/3037d6d01248502aee68
// http://www.htmq.com/html5/input_type_range.shtml
// https://phpjavascriptroom.com/?t=js&p=event

// コンポーネント定義
const media_player_component = {
    props: {

        // 動画ファイルパス
        mediaSrc: {
            type: String,
            required: true
        },

        // 映像有無
        withVideo: {
            type: Boolean,
            default: true
        },

        // 音声有無
        withAudio: {
            type: Boolean,
            default: true
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
            is_loading: false,
            is_show: false,
            is_error: false,
            is_playing: false,
            was_playing: false,
            opacity: 1.00,
            volume: 1.00
        }
    },
    computed: {

        // 動画ソース
        media_src: function() {
            return String(this.mediaSrc).trim();
        },

        // 映像有無
        with_video: function() {
            return Boolean(this.withVideo);
        },

        // 音声有無
        with_audio: function() {
            return Boolean(this.withAudio);
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
            if (this.with_video) {
                return this.start_time + parseFloat(this.videoFadeIn);
            } else {
                return this.start_time;
            }
        },

        // 映像フェードアウト開始時間
        video_fadeout_start_time: function() {
            if (this.with_video) {
                return this.end_time - parseFloat(this.videoFadeOut);
            } else {
                return this.end_time;
            }
        },

        // 音声フェードイン終了時間
        audio_fadein_end_time: function() {
            if (this.with_audio) {
                return this.start_time + parseFloat(this.audioFadeIn);
            } else {
                return this.start_time;
            }
        },

        // 音声フェードアウト開始時間
        audio_fadeout_start_time: function() {
            if (this.with_audio) {
                return this.end_time - parseFloat(this.audioFadeOut);
            } else {
                return this.end_time;
            }
        },

        // 現在時間
        current_time : function() {
            return formatTime(this.time - this.start_time);
        },

        // 再生時間
        duration: function() {
            return formatTime(this.end_time - this.start_time);
        },

        // 再生可能制御
        can_play: function() {
            return (this.with_video || this.with_audio) && this.is_show && !this.is_loading && !this.is_error && (this.start_time < this.end_time);
        }
    },
    template: `
        <div>
            <div v-if="is_loading" class="row">
                <div class="col-12 text-primary"">
                    <span class="spinner-border spinner-border-sm"></span>
                    <span>Loading...</span>
                </div>
            </div>
            <div v-if="is_error" class="row">
                <div class="col-12 bg-warning text-dark">
                    <span>読み込みエラー</span>
                </div>
            </div>
            <div v-if="with_video && is_show" class="row" style="margin:0;background-color:black;">
                <video ref="media"
                    class="col-12"
                    v-bind:style="{padding:0, opacity:opacity}"
                    v-on:loadstart="onLoad()"
                    v-on:loadeddata="onLoaded()"
                    v-on:error="onError()"
                    v-on:canplaythrough="onCanPlay()"
                    v-on:play="onPlay()"
                    v-on:pause="onPause()"
                    v-on:timeupdate="onTimeUpdate()"
                    v-bind:src="media_src">
                </video>
            </div>
            <audio v-else-if="with_audio && is_show" ref="media"
                v-on:loadstart="onLoad()"
                v-on:loadeddata="onLoaded()"
                v-on:error="onError()"
                v-on:canplaythrough="onCanPlay()"
                v-on:play="onPlay()"
                v-on:pause="onPause()"
                v-on:timeupdate="onTimeUpdate()"
                v-bind:src="media_src">
            </audio>
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
            <div class="row" v-cloak>
                <div class="col-12">
                    <button v-if="!can_play" class="btn btn-secondary" disabled>再生</button>
                    <button v-else-if="is_playing" class="btn btn-primary" v-on:click="toggle_play()">停止</button>
                    <button v-else class="btn btn-primary" v-on:click="toggle_play()">再生</button>
                    <span>{{current_time}} / {{duration}}</span>
                </div>
            </div>
        </div>
    `,
    methods:{

        // 動画コンテンツ表示・非表示
        showMedia: function() {
            this.is_show = true;
        },
        hideMedia: function() {
            this.is_show = false;
            this.is_error = false;
            this.is_playing = false;
            this.was_playing = false;
        },

        // 動画読み込み時ハンドラ
        onLoad: function() {
            this.is_loading = true;
        },
        onLoaded: function() {
            this.time = this.start_time;
            this.$refs.media.currentTime = this.start_time;
            this.video_fade(this.start_time);
            this.audio_fade(this.start_time);
            this.is_playing = false;
            this.is_loading = false;
            this.$emit('load', this.$refs.media.duration);
        },

        // エラー時ハンドラ
        onError: function() {
            this.is_error = true;
        },

        // 動画再生可能時ハンドラ
        onCanPlay: function() {
            this.is_error = false;
        },

        // 動画再生時ハンドラ
        onPlay: function() {
            if (this.can_play) {
                this.is_playing = true;
            } else {
                this.pause();
            }
        },

        // 動画停止時ハンドラ
        onPause: function() {
            this.is_playing = false;
        },

        // 再生中動画位置ハンドラ
        onTimeUpdate: function() {
            if (this.can_play) {
                if (this.is_playing) {
                    this.time = this.$refs.media.currentTime;
                }
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
            if (this.can_play) {
                if (this.end_time <= this.time) {
                    this.time = this.start_time;
                }
                this.$refs.media.play();
            }
        },

        // 動画停止
        pause: function() {
            if (this.can_play) {
                this.$refs.media.pause();
            }
        },

        // 動画再生・停止切り替え
        toggle_play: function() {
            if (!this.is_playing) {
                this.play();
            } else {
                this.pause();
            }
        },

        // videoフェードイン・フェードアウト
        video_fade: function(value) {
            if (!this.with_video) {
                this.opacity = 0;
            } else if (value < this.video_fadein_end_time) {
                if (value <= this.start_time) {
                    this.opacity = 0;
                } else {
                    this.opacity = (value - this.start_time) / (this.video_fadein_end_time - this.start_time);
                }
            } else if (this.video_fadeout_start_time < value) {
                if (this.end_time <= value) {
                    this.opacity = 0;
                } else {
                    this.opacity = (this.end_time - value) / (this.end_time - this.video_fadeout_start_time);
                }
            } else {
                this.opacity = 1.00;
            }
        },

        // audioフェードイン・フェードアウト
        audio_fade: function(value) {
            if (!this.with_audio) {
                this.volume = 0;
            } else if (value < this.audio_fadein_end_time) {
                if (value <= this.start_time) {
                    this.volume = 0;
                } else {
                    this.volume = (value - this.start_time) / (this.audio_fadein_end_time - this.start_time);
                }
            } else if (this.audio_fadeout_start_time < value) {
                if (this.end_time <= value) {
                    this.volume = 0;
                } else {
                    this.volume = (this.end_time - value) / (this.end_time - this.audio_fadeout_start_time);
                }
            } else {
                this.volume = 1.00;
            }
        }
    },
    watch: {
        start_time: function(value) {
            if ((this.time < value) && this.can_play) {
                this.time = value;
                this.$refs.media.currentTime = value;
            }

            // video・audioフェードイン・フェードアウト
            this.video_fade(this.time);
            this.audio_fade(this.time);
        },
        end_time: function(value) {
            if ((this.time > value) && this.can_play) {
                this.time = value;
                this.$refs.media.currentTime = value;
            }

            // video・audioフェードイン・フェードアウト
            this.video_fade(this.time);
            this.audio_fade(this.time);
        },
        video_fadein_end_time: function(value) {
            // video・audioフェードイン・フェードアウト
            this.video_fade(this.time);
            this.audio_fade(this.time);
        },
        video_fadeout_start_time: function(value) {
            // video・audioフェードイン・フェードアウト
            this.video_fade(this.time);
            this.audio_fade(this.time);
        },
        audio_fadein_end_time: function(value) {
            // video・audioフェードイン・フェードアウト
            this.video_fade(this.time);
            this.audio_fade(this.time);
        },
        audio_fadeout_start_time: function(value) {
            // video・audioフェードイン・フェードアウト
            this.video_fade(this.time);
            this.audio_fade(this.time);
        },

        // 再生位置制御
        time: function(value) {
            if (this.can_play) {
                if (value < this.start_time) {
                    this.$refs.media.currentTime = this.start_time;
                } else if (value >= this.end_time) {
                    this.pause();
                    this.$refs.media.currentTime = this.end_time;
                } else if (!this.is_playing) {
                    this.$refs.media.currentTime = value;
                }
            }

            // video・audioフェードイン・フェードアウト
            this.video_fade(value);
            this.audio_fade(value);
        },

        // 音量制御
        volume: function(value) {
            this.$refs.media.volume = value;
        }
    }
}
