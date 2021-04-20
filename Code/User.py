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
                 password = "Ab123456+",
                 name  = "None",
                 phone = "None",
                 email = "None",
                 event = []):
        
        self.id    = stu_id    # 必须填写
        self.pwd   = password  # 必须填写
        self.name  = name
        self.phone = phone
        self.email = email
        self.event = event
    
    # 通过学号获取全部用户信息
    def PullUser(self):
        result = self.__mycol.find_one({ "_id": self.id })
        if result:
            self.pwd   = result['password']
            self.name  = result['name']
            self.phone = result['phone']
            self.email = result['email']
            self.event = result['event']
            return self
        else:
            return "Not Found"
    
    def TurnDict(self):
        mydict = {
            "_id"      : self.id ,
            "password" : self.pwd,
            "name"     : self.name,
            "phone"    : self.phone,
            "email"    : self.email,
            "event"    : self.event}
        return mydict
    
    # 用于在数据库中创建或修改用户信息
    def PushUser(self):
        mydict = User.TurnDict(self)
        if self.__mucol.find_one({ "_id": self.id }):
            myquery = {"_id" : self.id}
            User.mycol.update(myquery,mydict) 
            return "Acc_Updated"
        else:
            User.mycol.insert_one(mydict) # 上传新的document
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
