// 小数点以下3桁のFloat型に変換
const convertFloat = function(value) {
    let work_value = parseFloat(value);
    if (isNaN(work_value)) {
        return NaN;
    } else if (String(work_value) != String(value)) {
        return NaN;
    }

    try {
        return parseInt(work_value * 1000) / 1000;
    } catch(e) {
        return NaN;
    }
};

// フレームから時間を算出
const convertFrameToTime = function(frame, frame_rate_denom, frame_rate_numer) {
    return (frame - 1) * frame_rate_denom / frame_rate_numer;
};
