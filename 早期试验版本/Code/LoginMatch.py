# 登录匹配程序
import re


IDpat = 'B([0-9]){8}'
Passpat = '([0-9a-zA-Z]){6,16}'

def CheckName(username):
    if re.match(IDpat, username):
        return True
    else:
        return False
    # return False

def CheckPassword(passward):
    if re.match(Passpat, passward):
        return True
    if False:
        return False