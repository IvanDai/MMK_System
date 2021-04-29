import re

LoginID = '[AB]([0-9]){8}'
RegistId = 'B([0-9]){8}'
Passwd = '([0-9a-zA-Z]){6,16}'

# 登陆系统
def CheckName(username):
    if re.match(LoginID, username):
        return True
    else:
        return False
    # return False

def CheckPassword(passward):
    if re.match(Passwd, passward):
        return True
    if False:
        return False


# 注册系统
def IDmatah(id):
    if re.match(RegistId,id):
        return True
    else:
        return False

def passwardMatch(passward):
    if re.match(Passwd,passward):
        return True
    else:
        return False

# 管理员添加系统
def classRoomID_match(ID):
    ID_pat = 'B[2-4]R[1-4]0[1-9][0-6]'
    if re.match(ID_pat,ID):
        return True
    else :
        return False

def people_match(people):
    a = [n for n in range(300)]
    if int(people) in a:
        return True
    else :
        print(1)
        return False
