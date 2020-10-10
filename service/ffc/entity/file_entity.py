# ==================================================
# ffc_dbのエンティティ
# ==================================================

# ファイルエンティティ
class FileEntity():
    def __init__(self):
        self.__file_id = None
        self.__filename = None
        self.__filepath = None
        self.__workpath = None
        self.__webpath = None
    
    @property
    def file_id(self):
        return self.__file_id
    @file_id.setter
    def file_id(self, file_id):
        self.__file_id = int(file_id)
    
    @property
    def filename(self):
        return self.__filename
    @filename.setter
    def filename(self, filename):
        self.__filename = str(filename)
    
    @property
    def filepath(self):
        return self.__filepath
    @filepath.setter
    def filepath(self, filepath):
        self.__filepath = str(filepath)
    
    @property
    def workpath(self):
        return self.__workpath
    @workpath.setter
    def workpath(self, workpath):
        self.__workpath = str(workpath)
    
    @property
    def webpath(self):
        return self.__webpath
    @webpath.setter
    def webpath(self, webpath):
        self.__webpath = str(webpath)
