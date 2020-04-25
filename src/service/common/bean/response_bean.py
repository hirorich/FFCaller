# ==================================================
# レスポンスBean
# ==================================================

# ==================================================
# レスポンスBean
# ==================================================
class ResponseBean:
    
    def __init__(self):
        self.__service_response_bean = None
        
    
    # サービスレスポンスBean
    def get_service_response_bean(self):
        return self.__service_response_bean
    def set_service_response_bean(self, service_response_bean):
        self.__service_response_bean = service_response_bean
    
    # 辞書型に変換
    def parse_to_dict(self):
        bean_dict = dict()
        if self.__service_response_bean is not None:
            bean_dict['service_response'] = self.__service_response_bean.parse_to_dict()
        
        return bean_dict

