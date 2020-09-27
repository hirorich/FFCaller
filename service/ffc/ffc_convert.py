# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

from decimal import Decimal, ROUND_FLOOR

# フレームから時間に変換
def frame_to_time(start_frame, end_frame, r_frame_rate):
    r_frame_rate_numer = int(r_frame_rate.split('/')[0])
    r_frame_rate_denom = int(r_frame_rate.split('/')[1])
    
    start_time = _to_float(Decimal(start_frame - 1) * r_frame_rate_denom / r_frame_rate_numer)
    end_time = _to_float(Decimal(end_frame) * r_frame_rate_denom / r_frame_rate_numer)
    
    return start_time, end_time

# 時間からフレームに変換
def time_to_frame(start_time, end_time, r_frame_rate):
    r_frame_rate_numer = int(r_frame_rate.split('/')[0])
    r_frame_rate_denom = int(r_frame_rate.split('/')[1])
    
    start_frame = _to_int(Decimal(start_time) * r_frame_rate_numer / r_frame_rate_denom) + 1
    end_frame = _to_int(Decimal(end_time) * r_frame_rate_numer / r_frame_rate_denom)
    
    return start_frame, end_frame

# 小数点以下3桁に変換
def _to_float(value):
    return float(Decimal(value).quantize(Decimal('0.001'), rounding=ROUND_FLOOR))

# 整数に変換
def _to_int(value):
    return int(Decimal(value).quantize(Decimal('1'), rounding=ROUND_FLOOR))
