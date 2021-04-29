import pymongo
import os,sys
import re
from db_User import *
from db_ClassRoom import *
import datetime
import json

class Event():
    # 链接本地客户端
    __myclient = pymongo.MongoClient("mongodb://localhost:27017")
    # 创建数据库
    __mydb = __myclient["MMKeyDB"]
    # 创建新的集合
    __mycol = __mydb["Events"]

    def __init__(self):
        return

    def TurnDict(self):
        mydict ={ 
            "_id"       : self.id,
            "date"      : self.date,
            "quantuma"  : self.quan  ,   
            "RoomID"    : self.room_id , 
            "UserID"    : self.user_id , 
            "reason"    : self.reason ,
            "status"    : self.status }
        return mydict

    def Add_Event(self,date,quan,room_id,usr_id,reason,status = 0):
        self.id         = self.Form_ID(date,quan,room_id)
        self.date       = date
        self.quan       = quan
        self.room_id    = room_id
        self.user_id    = usr_id
        self.reason     = reason
        self.status     = status

        mydict = self.TurnDict()
        if self.__mycol.find_one({"_id":self.id}):
            print("教室已被占用")
            return False
        else:
            self.__mycol.insert_one(mydict)
            return True
    
    def Approve_Event(self,id):
        self.Pull_Event(id)
        self.status = 1
        self.Replace_Event()
        # usr  = User(self.user_id)
        # room = ClassRoom((self.room_id))
        return

    def Replace_Event(self):
        mydict = self.TurnDict()
        self.__mycol.insert_one(mydict) 

    def Pull_Event(self,id):
        self.id = id
        result = self.__mycol.find_one({"_id":self.id})
        if result:
            self.date = result["date"]
            self.quan = result["quantuma"]
            self.room_id = result["RoomID"]
            self.user_id = result["UserID"]
            self.reason  = result["reason"]
            self.status  = result["status"]
            return True
        else:
            return False

    def Check_Event_User(self,user_ID):
        cursor = self.__mycol.find({"UserID":user_ID})
        if cursor:
            return cursor
        else:
            return False

    def Check_Event(self,room_ID,date,quan):
        if self.__mycol.find_one({"RoomID":room_ID,
                                  "date":date,
                                  "quantuma":quan}):
            return True
        else:
            return False

    def Delete_Event(self,id):
        self.__mycol.delete_one({"_id":id})
        

    def Form_ID(self,date,quan,room_id):
        id = date + "-" + str(quan) + "-" + str(room_id)
        return id
     
    # 用于更新事件状态
    def Update_Event(self,event):
        self.__mycol.insert_one(event) 

    def Update(self):
        # 判断日期是否已经过期
        date = str(datetime.date.today())
        events = self.__mycol.find({"date":{"$lt":date}}) 
        for event in events:
            # temp = json.loads(event)
            # print(event)
            myquery = {"_id":event["_id"]}
            newvalue  = { "$set": { "status": 2} }
            self.__mycol.update_one(myquery,newvalue)
        print("Events Update: Day Expined Updated, Waiting ...")
        # 判断当天是否已经过期
        d = datetime.datetime.now()
        time = d.hour * 100 + d.minute
        if time < 800:
            quant = 0
        elif time < 935:
            quant = 1
        elif time < 1215:
            quant = 2
        elif time < 1520:
            quant = 3
        elif time < 1710:
            quant = 4
        else:
            quant = 10
        events = self.__mycol.find({"date":date})
        for event in events:
            if event["quantuma"] < quant:
                event["status"] = 2
                self.Update_Event(event)
        print("Events All Updated Successful!")
        
if __name__ == "__main__":
    Event().Update()