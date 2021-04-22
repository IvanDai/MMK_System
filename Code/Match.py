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