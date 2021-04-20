import pymongo
import os,sys

class User:
    
    # 链接本地客户端
    __myclient = pymongo.MongoClient("mongodb://localhost:27017")
    # 创建数据库
    __mydb = __myclient["MMKeyDB"]
    # 创建新的集合
    __mycol = __mydb["Users"]
    
    
    def __init__(self, stu_id, 
                 pwd   = "",
                 name  = "",
                 phone = "",
                 email = "",
                 admin = "",
                 event = []):
        # 实例化用户 id
        self.id    = stu_id    # 必须填写
        self.pwd   = pwd   
        self.name  = name 
        self.phone = phone 
        self.email = email 
        self.admin = admin
        self.event = event
        User.PullUser(self)
    
    # 通过学号获取全部用户信息
    def PullUser(self):
        result = self.__mycol.find_one({ "_id": self.id })
        if result:
            self.pwd   = self.pwd   or result['password']
            self.name  = self.name  or result['name']
            self.phone = self.phone or result['phone']
            self.email = self.email or result['email']
            self.adimn = self.admin or result['admin']
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
            return "Plz Set Acc"
        elif self.__mycol.find_one({ "_id": self.id }):
            myquery = {"_id" : self.id}
            self.__mycol.update(myquery,mydict) 
            return "Acc_Updated"
        else:
            self.__mycol.insert_one(mydict) # 上传新的document
            return "Acc_Created"
            
    # 用于更新password
    def PushPwd(self):
        if self.__mycol.find_one({ "_id": self.id }):
            myquery = {"_id":self.id}
            newvalue  = { "$set": { "password": self.pwd } }
            User.mycol.update_one(myquery,newvalue)
            return "Pwd_Updated"
        else:
            return "Acc_Not_Found"
    
    # 注销账户 请谨慎运用此函数！！！！
    def Delete(self):
        User.mycol.delete_one({"_id": self.id})
        return "Deleted"