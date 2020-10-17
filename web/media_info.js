// コンポーネント定義
const media_info_component = {
    data: function() {
        return {
            file: {
                filepath: '-'
            },
            format: {
                nb_streams: 0,
                duration: '-',
                size: '-'
            },
            video_stream: {
                index: '-',
                codec_type: '-',
                codec_name: '-',
                codec_long_name: '-',
                duration: '-',
                bit_rate: '-',
                width: 0,
                height: 0,
                r_frame_rate: '-',
                nb_frames: '-'
            },
            audio_stream: {
                index: '-',
                codec_type: '-',
                codec_name: '-',
                codec_long_name: '-',
                duration: '-',
                bit_rate: '-',
                sample_rate: '-'
            }
        }
    },
    computed: {
        window_size: function() {
            let window_size = '-';
            try {
                let width = parseInt(this.video_stream.width);
                let height = parseInt(this.video_stream.height);
                if (width > 0 && height > 0) {
                    window_size = String(width) + ' x ' + String(height);
                }
            } catch(e) {}
            return window_size;
        }
    },
    template: `
        <div>
            <div class="bg-light">{{file.filepath}}</div>
            <table class="table table-striped table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th>nb_streams</th>
                        <th>duration</th>
                        <th>size</th>
                    </tr>
                </thead>
                <tbody v-cloak>
                    <tr>
                        <td>{{format.nb_streams}}</td>
                        <td>{{format.duration}}</td>
                        <td>{{format.size}}</td>
                    </tr>
                </tbody>
            </table>
            <table class="table table-striped table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th>項目</th>
                        <th>映像</th>
                        <th>音声</th>
                    </tr>
                </thead>
                <tbody v-cloak>
                    <tr>
                        <th>index</th>
                        <td>{{video_stream.index}}</td>
                        <td>{{audio_stream.index}}</td>
                    </tr>
                    <tr>
                        <th>codec_type</th>
                        <td>{{video_stream.codec_type}}</td>
                        <td>{{audio_stream.codec_type}}</td>
                    </tr>
                    <tr>
                        <th>codec_name</th>
                        <td>{{video_stream.codec_name}}</td>
                        <td>{{audio_stream.codec_name}}</td>
                    </tr>
                    <tr>
                        <th>codec_long_name</th>
                        <td>{{video_stream.codec_long_name}}</td>
                        <td>{{audio_stream.codec_long_name}}</td>
                    </tr>
                    <tr>
                        <th>duration</th>
                        <td>{{video_stream.duration}}</td>
                        <td>{{audio_stream.duration}}</td>
                    </tr>
                    <tr>
                        <th>bit_rate</th>
                        <td>{{video_stream.bit_rate}}</td>
                        <td>{{audio_stream.bit_rate}}</td>
                    </tr>
                    <tr>
                        <th>width x height</th>
                        <td>{{window_size}}</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <th>r_frame_rate</th>
                        <td>{{video_stream.r_frame_rate}}</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <th>nb_frames</th>
                        <td>{{video_stream.nb_frames}}</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <th>sample_rate</th>
                        <td>-</td>
                        <td>{{audio_stream.sample_rate}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    `,
    methods: {
        set_media_info: function(info) {

            try {
                this.file.filepath = info.file.filepath;
            } catch(e) {
                this.file.filepath = '-';
            }

            try {
                this.format.nb_streams = info.format.nb_streams;
            } catch(e) {
                this.format.nb_streams = 0;
            }

            try {
                this.format.duration = info.format.duration;
            } catch(e) {
                this.format.duration = '-';
            }

            try {
                this.format.size = info.format.size;
            } catch(e) {
                this.format.size = '-';
            }

            try {
                this.video_stream.index = info.video_stream.stream.stream_index;
            } catch(e) {
                this.video_stream.index = '-';
            }

            try {
                this.video_stream.codec_type = info.video_stream.stream.codec_type;
            } catch(e) {
                this.video_stream.codec_type = '-';
            }

            try {
                this.video_stream.codec_name = info.video_stream.stream.codec_name;
            } catch(e) {
                this.video_stream.codec_name = '-';
            }

            try {
                this.video_stream.codec_long_name = info.video_stream.stream.codec_long_name;
            } catch(e) {
                this.video_stream.codec_long_name = '-';
            }

            try {
                this.video_stream.duration = info.video_stream.stream.duration;
            } catch(e) {
                this.video_stream.duration = '-';
            }

            try {
                this.video_stream.bit_rate = info.video_stream.stream.bit_rate;
            } catch(e) {
                this.video_stream.bit_rate = '-';
            }

            try {
                this.video_stream.width = info.video_stream.video.width;
            } catch(e) {
                this.video_stream.width = 0;
            }

            try {
                this.video_stream.height = info.video_stream.video.height;
            } catch(e) {
                this.video_stream.height = 0;
            }

            try {
                this.video_stream.r_frame_rate = info.video_stream.video.r_frame_rate;
            } catch(e) {
                this.video_stream.r_frame_rate = '-';
            }

            try {
                this.video_stream.nb_frames = info.video_stream.video.nb_frames;
            } catch(e) {
                this.video_stream.nb_frames = '-';
            }

            try {
                this.audio_stream.index = info.audio_stream.stream.stream_index;
            } catch(e) {
                this.audio_stream.index = '-';
            }

            try {
                this.audio_stream.codec_type = info.audio_stream.stream.codec_type;
            } catch(e) {
                this.audio_stream.codec_type = '-';
            }

            try {
                this.audio_stream.codec_name = info.audio_stream.stream.codec_name;
            } catch(e) {
                this.audio_stream.codec_name = '-';
            }

            try {
                this.audio_stream.codec_long_name = info.audio_stream.stream.codec_long_name;
            } catch(e) {
                this.audio_stream.codec_long_name = '-';
            }

            try {
                this.audio_stream.duration = info.audio_stream.stream.duration;
            } catch(e) {
                this.audio_stream.duration = '-';
            }

            try {
                this.audio_stream.bit_rate = info.audio_stream.stream.bit_rate;
            } catch(e) {
                this.audio_stream.bit_rate = '-';
            }

            try {
                this.audio_stream.sample_rate = info.audio_stream.audio.sample_rate;
            } catch(e) {
                this.audio_stream.sample_rate = '-';
            }
        }
    }
}
