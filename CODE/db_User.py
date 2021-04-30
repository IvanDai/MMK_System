import pymongo
import os,sys
import re
import socket


class User:
    
    # 链接本地客户端
    __myclient = pymongo.MongoClient("mongodb://localhost:27017",serverSelectionTimeoutMS = 30)
    # 创建数据库
    __mydb = __myclient["MMKeyDB"]
    # 创建新的集合
    __mycol = __mydb["Users"]

     
    
    def __init__(self, 
                 stu_id= "", 
                 pwd   = "",
                 name  = "",
                 phone = "",
                 email = "",
                 admin = 0,
                 event = []):

        from PyQt5.QtWidgets import QMessageBox
        # 实例化用户 id
        self.id    = stu_id    # 必须填写
        self.pwd   = pwd   
        self.name  = name 
        self.phone = phone 
        self.email = email 
        self.admin = admin
        self.event = event
        if self.db_connect():
            self.PullUser(self)

    def db_connect(self): 
        #connecting to a DB in mongoDB 
        try: 
            self.__myclient.admin.command("ping") 
            # print("Connection Successful!") 
            return True 
        except: 
            print("Please check your connection") 
            return False

    # 通过学号获取全部用户信息
    def PullUser(self, id=""):
        if id:
            result = self.__mycol.find_one({ "_id": self.id }) 
        else:
            result = self.__mycol.find_one({ "_id": self.id })
        if result:
            self.pwd   = self.pwd   or result['password']
            self.name  = self.name  or result['name']
            self.phone = self.phone or result['phone']
            self.email = self.email or result['email']
            self.admin = self.admin or result['admin']
            self.event = self.event or result['event']
            return self
        else:
            return False
    
    def TurnDict(self):
        mydict = {
            "_id"      : self.id ,
            "password" : self.pwd,
            "name"     : self.name,
            "phone"    : self.phone,
            "email"    : self.email,
            "admin"    : self.admin,
            "event"    : self.event}
        return mydict
    
    # 用于在数据库中创建或修改用户信息
    def PushUser(self):
        mydict = User.TurnDict(self)
        if not self.pwd :
            print("请设置密码")
            return False
        elif self.__mycol.find_one({ "_id": self.id }):
            myquery = {"_id" : self.id}
            self.__mycol.update(myquery,mydict) 
            print("用户信息已更新")
            return True
        else:
            self.__mycol.insert_one(mydict) # 上传新的document
            print("用户已创建")
            return True
            
    # 用于更新password
    def PushPwd(self):
        if self.__mycol.find_one({ "_id": self.id }):
            myquery = {"_id":self.id}
            newvalue  = { "$set": { "password": self.pwd } }
            User.__mycol.update_one(myquery,newvalue)
            return "Pwd_Updated"
        else:
            return "Acc_Not_Found"
    
    # 注销账户 请谨慎运用此函数！！！！
    def Delete(self):
        self.__mycol.delete_one({"_id": self.id})
        return "Deleted"

    def Pull_All_User(self):
        cursor = self.__mycol.find({})
        return cursor
