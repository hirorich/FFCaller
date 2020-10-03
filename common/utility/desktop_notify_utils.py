# ==================================================
# デスクトップ通知部品
# ==================================================

from plyer import notification
from common import app_property
from common.utility import path_utils

# デスクトップ通知
def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_name = app_property.app_name,
        app_icon = path_utils.convert_to_absolute_path(app_property.add_data.icon_ico)
    )
