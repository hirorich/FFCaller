# ==================================================
# システム日付
# ==================================================

from datetime import datetime
from common import app_property

class _SysDateTime:
    
    # システム日付設定
    def __init__(self):
        now = datetime.now()
        
        # 日付指定
        sys_date = now
        try:
            # プロパティから日付取得(書式：YYYY/mm/dd)
            prop_date = app_property.system_date
            sys_date = datetime.strptime(prop_date, '%Y/%m/%d')
        except:
            pass
        
        # 時間指定
        sys_time = now
        try:
            # プロパティから時間取得(書式：HH:MM:SS)
            prop_time = app_property.system_time
            sys_time = datetime.strptime(prop_time, '%H:%M:%S')
        except:
            pass
        
        # システム日付指定
        self.__system_datetime = datetime(
            year = sys_date.year, month = sys_date.month, day = sys_date.day,
            hour = sys_time.hour, minute = sys_time.minute, second = sys_time.second,
            microsecond = now.microsecond
        )
        
        # システム日付と実日付の差分を算出
        self.__diff_datetime = now - self.__system_datetime
    
    # システム日付
    @property
    def system_datetime(self):
        return self.__system_datetime
    
    # システム処理日付
    @property
    def now(self):
        return datetime.now() - self.__diff_datetime

import sys
sys.modules[__name__] = _SysDateTime()
