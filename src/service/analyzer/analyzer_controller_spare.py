# ==================================================
# 動画解析のコントロール部品(予備)
# ==================================================

import numpy as np
import cv2

# フレーム数算出
def get_nb_frames(input_file_name):
    video = cv2.VideoCapture()
    
    try:
        video = cv2.VideoCapture(input_file_name)
        return int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    except Exception as e:
        raise e
    finally:
        video.release()
