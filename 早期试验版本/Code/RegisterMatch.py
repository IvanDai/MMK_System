import re

# 注册程序

# 1. 账号字符串匹配检查
# 2. 密码格式匹配
IDpat = 'B([0-9]){8}'
Passpat = '([0-9a-zA-Z]){6,16}'

# 检查用户ing是否符合格式
def IDmatah(id):
    if re.match(IDpat,id):
        return True
    else:
        return False

# 检查密码是否符合格式
def passwardMatch(passward):
    if re.match(Passpat,passward):
        return True
    else:
        return False