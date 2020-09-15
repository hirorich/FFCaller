// コンポーネント定義
const video_info = {
    data: function() {
        return {
            video_stream:{
                index:0,
                codec_type:'',
                codec_name:'',
                codec_long_name:'',
                duration:'',
                bit_rate:'',
                width:0,
                height:0,
                r_frame_rate:'',
                nb_frames:''
            },
            audio_stream:{
                index:0,
                codec_type:'',
                codec_name:'',
                codec_long_name:'',
                duration:'',
                bit_rate:'',
                sample_rate:''
            },
            format:{
                filename:'',
                nb_streams:0,
                duration:'',
                size:''
            }
        }
    },
    template: `
        <div>
            
            <!-- Table Format -->
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
            
            <!-- Table Video Stream, Audio Stream -->
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
                        <td>{{video_stream.width}} x {{video_stream.height}}</td>
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
    `
}
