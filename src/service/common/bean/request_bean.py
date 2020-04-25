# ==================================================
# リクエストBean
# ==================================================

# ==================================================
# リクエストBean
# ==================================================
class RequestBean:
    
    def __init__(self):
        self.__service_request_bean = ''
        
    
    # サービスリクエストBean
    def get_service_request_bean(self):
        return self.__service_request_bean
    def set_service_request_bean(self, service_request_bean):
        self.__service_request_bean = service_request_bean
    

