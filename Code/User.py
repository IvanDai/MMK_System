import pymongo
import os,sys
import numpy as np
import pandas as pd

class User:
    org_pwd   = "Ab123456+"
    org_name  = "None"
    org_phone = "None"
    org_email = "None"
    org_event = []    # 用于存储借用事件[eventID]

    # 链接本地客户端
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    # 创建数据库
    mydb = myclient["MMKeyDB"]
    # 创建新的集合
    mycol = mydb["Users"]

    def __init__(self, stu_id,
                 password = org_pwd,
                 name  = org_name,
                 phone = org_phone,
                 email = org_email,
                 event = org_event):
        self.id    = stu_id    # 必须填写
        self.pwd   = password  # 必须填写
        self.name  = name
        self.phone = phone
        self.email = email
        self.event = event

    # 用于在数据库中创建或修改用户信息
    def PushAll(self):
        mydict = {
            "_id"      : self.id ,
            "password" : self.pwd,
            "name"     : self.name,
            "phone"    : self.phone,
            "email"    : self.email,
            "event"    : self.event}

        if User.mycol.find_one({ "_id": self.id }):
            myquery = {"_id" : self.id}
            User.mycol.update(myquery,mydict)
            return "Acc_Updated"
        else:
            User.mycol.insert_one(mydict) # 上传新的document
            return "Acc_Created"

    # 用于更新password
    def PushPwd(self):
        if User.mycol.find_one({ "_id": self.id }):
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
