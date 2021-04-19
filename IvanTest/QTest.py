
# SignInUser
class SignInUser:
    pwwd = 134
    def __init__(self, name, password):
        self.name = name
        self.pwd = password

a = SignInUser('zhaoxulong')
print(a.pwwd)
