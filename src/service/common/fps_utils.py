# ==================================================
# fps共通部品
# ==================================================

import numpy as np

# 秒->フレーム換算
# a [秒] => ceiling(a * fps) + 1 [フレーム]
def sec_to_frame(sec, fps):
    splited_fps = fps.split('/')
    numerator_fps = int(splited_fps[0])
    denominator_fps = int(splited_fps[1])
    
    frame = np.ceil(sec * numerator_fps / denominator_fps) + 1
    return int(frame)

# フレーム->秒換算
# b [フレーム] => floor(N * (a - 1) / fps)/ N [秒]
def frame_to_sec(frame, fps):
    splited_fps = fps.split('/')
    numerator_fps = int(splited_fps[0])
    denominator_fps = int(splited_fps[1])
    
    digit_number = np.power(10, 3)
    sec = np.floor((frame - 1) * denominator_fps / numerator_fps * digit_number) / digit_number
    return float(sec)

