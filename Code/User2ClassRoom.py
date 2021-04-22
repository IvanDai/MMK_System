import pymongo
import os,sys
import re
import random

class User2ClassRoom:
    # 链接本地客户端
    __myclient = pymongo.MongoClient("mongodb://localhost:27017")
    # 创建数据库
    __mydb = __myclient["MMKeyDB"]
    # 创建新的集合
    __mycol = __mydb["User2ClassRoom"]

    # 判断是否输入id或是输入name，如果有输入则转译

    def __init__(self,
                 room_id    = "",
                 user_id    = "",
                 status     = ""):

        self._id    = room_id
        self.user_id    = user_id
        self.status     = status
        
        User2ClassRoom.PullUC(self)

    def PullUC(self):
        result = self.__mycol.find_one({ "_id": self._id })
        if result:
            self._id    = self._id  or result['_id']
            self.user_id    = self.user_id  or result['user_id']
            self.status     = self.status   or result['status']
            return self
        else:
            return False


    def TurnDict(self):
        mydict = {
            '_id'   : self._id,
            'user_id'   : self.user_id,
            'status'    : self.status} 
        return mydict
    # 有则更新，无则创建
    def PushUC(self):
        mydict = self.TurnDict()
        if self.__mycol.find_one({ "_id": self._id }):
            myquery = {"_id" : self._id}
            self.__mycol.update_one(myquery,{'$set':mydict})
            return "Acc_Updated"
        else:
            self.__mycol.insert_one(mydict) # 上传新的document
            return "Acc_Created"

    def ShowAll(self):
        allCol = self.__mycol.find()
        return allCol

    # 删除教室记录
    def Delete(self):
        self.mycol.delete_one({"_id": self.id})
        return "Deleted"

if __name__ == '__main__':
    r = User2ClassRoom('B2R1012','B18011929',1).PushClassroom()