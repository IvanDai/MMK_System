import pymongo
import os,sys
import re


class ClassRoom:
    # 链接本地客户端
    __myclient = pymongo.MongoClient("mongodb://localhost:27017")
    # 创建数据库
    __mydb = __myclient["MMKeyDB"]
    # 创建新的集合
    __mycol = __mydb["ClassRoom"]

    # 判断是否输入id或是输入name，如果有输入则转译
    def Name2Id(room_id,name):
        bool_n  = bool(re.match("教\d{1}-\d{3}",name))
        bool_id = bool(re.match("B\d{1}R\d{3}",room_id))
        if not (bool_id or bool_n):
            return False
        elif bool_n:
            room_id = "B" + name[1] + "R" + name[3:6]
        else:
            name = "教" + room_id[1] + "-" + room_id[3:6]

        return room_id,name

    def __init__(self,
                 room_id  = "",
                 name     = "",
                 seats = 0,
                 key_id   = "",
                 event    = []):

        if not(ClassRoom.Name2Id(room_id,name)):
            self.WrongFlag = 1
        else:
            self.id,self.name = ClassRoom.Name2Id(room_id,name)
            self.seats    = seats
            self.key_id   = key_id
            self.event    = event
            ClassRoom.PullClassroom(self)

    def PullClassroom(self):
        result = self.__mycol.find_one({ "_id": self.id })
        if result:
            self.name  = self.name  or result['name']
            self.seats = self.seats or result['seats']
            self.key_id= self.key_id or result['key_id']
            self.event = self.event or result['event']
            return self
        else:
            return False

    def TurnDict(self):
        mydict = {
            "_id"      : self.id ,
            "name"     : self.name,
            "seats"    : self.seats,
            "key_id"    : self.key_id,
            "event"    : self.event}
        return mydict

    def PushClassroom(self):
        mydict = User.TurnDict(self)
        if self.__mycol.find_one({ "_id": self.id }):
            myquery = {"_id" : self.id}
            self.__mycol.update(myquery,mydict)
            return "Acc_Updated"
        else:
            self.__mycol.insert_one(mydict) # 上传新的document
            return "Acc_Created"
    
    def AllClassroom(self):
        cursor = self.__mycol.find()
        # __import__('ipdb').set_trace()
        if cursor:
            # index = []
            # for doc in cursor:
            #     print(doc)
            #     temp = [doc['_id'],doc['name'],doc['seats'],doc['event']]
            #     index.append(temp)
            return cursor
        else:
            return False

    # 删除教室记录
    def Delete(self):
        User.mycol.delete_one({"_id": self.id})
        return "Deleted"

if __name__ == '__main__':
    index = ClassRoom().AllClassroom()
    for i in index:
        print(i)
