// 小数点以下3桁のFloat型に変換
const convertFloat = function(value, digit=3) {
    let work_value = parseFloat(value);
    if (isNaN(work_value)) {
        return NaN;
    } else if (String(work_value) != String(value)) {
        return NaN;
    }

    try {
        let base = Math.pow(10, digit);
        return parseInt(work_value * base) / base;
    } catch(e) {
        return NaN;
    }
};

// フレームから時間を算出
const convertFrameToTime = function(start_frame, end_frame, frame_rate_numer, frame_rate_denom) {
    start_time = (start_frame - 1) * frame_rate_denom / frame_rate_numer;
    end_time = end_frame * frame_rate_denom / frame_rate_numer;
    return {
        start_time: convertFloat(start_time),
        end_time: convertFloat(end_time)
    };
};

// 時間からフレームを算出
const convertTimeToFrame = function(start_time, end_time, frame_rate_numer, frame_rate_denom) {
    start_frame = start_time * frame_rate_numer / frame_rate_denom + 1;
    end_frame = end_time * frame_rate_numer / frame_rate_denom;
    return {
        start_frame: parseInt(start_frame),
        end_frame: parseInt(end_frame)
    };
};
