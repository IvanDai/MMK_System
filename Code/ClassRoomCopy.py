import pymongo
import os,sys
import re
import random

class ClassRoom:
    # 链接本地客户端
    __myclient = pymongo.MongoClient("mongodb://localhost:27017")
    # 创建数据库
    __mydb = __myclient["MMKeyDB"]
    # 创建新的集合
    __mycol = __mydb["ClassRoom_test"]

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

    # 将id转换为name
    def Id2Name(self,room_id):
        if room_id :
            name = "教" + room_id[1] + "-" + room_id[3:6]
            return room_id,name
        else:
            return '',''
    def __init__(self,
                 room_id  = "",
                 seats    = "",
                 status   = 0,
                 event    = []):

        DuringList = ['8:00~9:35',
                      '9:50~11:25',
                      '13:45~15:20',
                      '15:35~17:10',
                      '18:30~21:00']
        
        
        
        if not(self.Id2Name(room_id)):
            self.WrongFlag = 1
        else:
            self.id,self.name = self.Id2Name(room_id)
            self.seats    = seats
            self.during   = DuringList[int(self.id[-1])] if self.id else ''
            self.status    = status
            self.event    = event
            ClassRoom.PullClassroom(self)

    def PullClassroom(self):
        result = self.__mycol.find_one({ "_id": self.id })
        if result:
            self.name   = self.name      or result['name']
            self.seats  = self.seats     or result['seats']
            self.during = self.during    or result['during']
            self.status = self.status    or result['status']
            self.event  = self.event     or result['event']
            return self
        else:
            return False

    def TurnDict(self):
        mydict = {
            "_id"      : self.id ,
            "name"     : self.name,
            "seats"    : self.seats,
            "during"   : self.during,
            "status"   : self.status,
            "event"    : self.event}
        return mydict
    
    # 有则更新，无则创建
    def PushClassroom(self):
        mydict = self.TurnDict()
        if self.__mycol.find_one({ "_id": self.id }):
            myquery = {"_id" : self.id}
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
    # 先pull 再update
    for i in range(2,5):
        for j in range(1,4):
            for k in range(1,10):
                # 座位按房间号用2取余
                if k % 2 == 0:
                    seats = 80
                else:
                    seats = 180
                for n in range(0,5):
                    id = 'B'+str(i)+'R'+str(j)+str(k).zfill(2)+str(n)
                    ClassRoom(id,seats=seats).PushClassroom()