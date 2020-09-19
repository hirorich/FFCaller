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
