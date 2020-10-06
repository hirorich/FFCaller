# ==================================================
# ffprobeを用いた動画解析
# ==================================================

import numpy as np
import cv2

# フレーム数算出
def get_nb_frames(workpath):
    video = cv2.VideoCapture()
    
    try:
        video = cv2.VideoCapture(workpath)
        return int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    except Exception as e:
        raise e
    finally:
        video.release()
