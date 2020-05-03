// マージ・トリム情報
var trim_marge_info=new Vue({
    el:'#trim_marge_info',
    data:{
        input_file_index:0,
        input_file_list:[],
        input_file:{
            input_file_name:'',
            start_time:0,
            trim_duration:0,
            start_frame:1,
            frame_number:1,
            frame_specification_flag:false,
            video_fade_in_duration:0,
            video_fade_out_duration:0,
            audio_fade_in_duration:0,
            audio_fade_out_duration:0
        },
        output_file:{
            overwriting_flag:true,
            output_file_name:'',
            codec_type_combination:1
        }
    },
    methods:{
        convert: function(){
            if (this.input_file_list.length > this.input_file_index) {
                this.input_file_list.splice(this.input_file_index, 1, this.input_file);
            } else {
                this.input_file_list.splice(this.input_file_list.length - 1, 0, this.input_file);
            }
            request={input_file_bean:this.input_file_list, output_file_bean:this.output_file};
            eel.marge_trim(request);
        }, init: function(){
            this.input_file_index=0;
            this.input_file_list=[];
            
            this.input_file.input_file_name=stream_info.format.filename;
            this.input_file.start_time=0;
            this.input_file.trim_duration=stream_info.video_stream.duration;
            this.input_file.start_frame=1;
            this.input_file.frame_number=stream_info.video_stream.nb_frames;
            this.input_file.frame_specification_flag=false;
            this.input_file.video_fade_in_duration=0;
            this.input_file.video_fade_out_duration=0;
            this.input_file.audio_fade_in_duration=0;
            this.input_file.audio_fade_out_duration=0;
            
            this.output_file.overwriting_flag=true;
            this.output_file.output_file_name=converted_filename(stream_info.format.filename);
            this.output_file.codec_type_combination=1;
        }
    }
});

// 変換後ファイル名(デフォルト)取得
function converted_filename(filename) {
    pathlist=filename.split(".");
    filename=pathlist[pathlist.length - 2] + '_converted';
    pathlist[pathlist.length - 2]=filename;
    return pathlist.join(".");
}

// マージ・トリム結果取得
eel.expose(response_marge_trim)
function response_marge_trim(convert_info) {

    // 出力ファイル名
    output_file_name=convert_info['output_file_name'];
    alert(output_file_name)
}
