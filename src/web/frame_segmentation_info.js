// フレーム分割情報
var frame_segmentation_info=new Vue({
    el:'#frame_segmentation_info',
    data:{
        input_file:{
            input_file_name:'',
            start_time:0,
            trim_duration:0,
            start_frame:1,
            frame_number:1,
            frame_specification_flag:false,
        },
        output_file:{
            convert_mode:2,
            overwriting_flag:true,
            output_file_name:'',
            codec_type_combination:1
        }
    },
    methods:{
        convert: function(){
            reqest={input_file_bean:this.input_file, output_file_bean:this.output_file};
            alert('frame_segmentation_info');
        }, init: function(){
            this.input_file.input_file_name=stream_info.format.filename;
            this.input_file.start_time=0;
            this.input_file.trim_duration=stream_info.video_stream.duration;
            this.input_file.start_frame=1;
            this.input_file.frame_number=stream_info.video_stream.nb_frames;
            this.input_file.frame_specification_flag=false;
            
            this.output_file.convert_mode=1;
            this.output_file.overwriting_flag=true;
            this.output_file.output_file_name=stream_info.format.filename;
            this.output_file.codec_type_combination=1;
        }
    }
});
