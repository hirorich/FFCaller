// 表示形式変換
const formatTime = function(value) {
    let formatted = '--:--:--.---';
    try {
        let date = new Date(value * 1000);
        let HH = date.getUTCHours();
        let mm = ('00' + date.getUTCMinutes()).slice(-2);
        let ss = ('00' + date.getUTCSeconds()).slice(-2);
        let fff = ('000' + date.getUTCMilliseconds()).slice(-3);
        formatted = HH + ':' + mm + ':' + ss + '.' + fff;
    } catch(e) {}
    return formatted;
};
