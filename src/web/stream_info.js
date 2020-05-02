// 対象動画ファイル名
var input_info=new Vue({
    el:'#input_info',
    data:{
        filename:''
    },
    methods:{
        analyze: function(){
            filename=this.filename;
            eel.analyze(filename);
            this.filename='';
        }
    }
});

// 動画情報
var stream_info=new Vue({
    el:'#stream_info',
    data:{
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
        audio_stream:[
            {
                index:0,
                codec_type:'',
                codec_name:'',
                codec_long_name:'',
                duration:'',
                bit_rate:'',
                sample_rate:''
            }
        ],
        format:{
            filename:'',
            nb_streams:0,
            duration:'',
            size:''
        }
    }
});

// サーバ処理失敗時
eel.expose(get_server_error_msg)
function get_server_error_msg(msg) {
    alert(msg);
}

// 動画解析結果取得
eel.expose(response_analyzer)
function response_analyzer(analyze_info) {

    // 映像ストリーム情報
    video_info=analyze_info['video'];
    video_stream={
        index:video_info['index'],
        codec_type:video_info['codec_type'],
        codec_name:video_info['codec_name'],
        codec_long_name:video_info['codec_long_name'],
        duration:video_info['duration'],
        bit_rate:video_info['bit_rate'],
        width:video_info['width'],
        height:video_info['height'],
        r_frame_rate:video_info['r_frame_rate'],
        nb_frames:video_info['nb_frames']
    }
    stream_info.video_stream=video_stream

    // 音声ストリーム情報
    audio_info_list=analyze_info['audio'];
    stream_info.audio_stream=[];
    audio_info_list.forEach(function(audio_info){
        audio_stream={
            index:audio_info['index'],
            codec_type:audio_info['codec_type'],
            codec_name:audio_info['codec_name'],
            codec_long_name:audio_info['codec_long_name'],
            duration:audio_info['duration'],
            bit_rate:audio_info['bit_rate'],
            sample_rate:audio_info['sample_rate']
        }
        stream_info.audio_stream.splice(stream_info.audio_stream.length, 0, audio_stream);
    });

    // フォーマット情報
    format_info=analyze_info['format'];
    format={
        filename:format_info['filename'],
        nb_streams:format_info['nb_streams'],
        duration:format_info['duration'],
        size:format_info['size']
    }
    stream_info.format=format
}
