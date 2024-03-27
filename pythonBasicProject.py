class User:
    def __init__(self,name,roll,mail,password):
        self.name=name
        self.roll=roll
        self.mail=mail
        self.password=password
        self.logged_in=False
class Enter:
    def __init__(self):
        self.users =[]
    def Register(self,name,roll,mail,password):
        newUser=User(name,roll,mail,password)
        for user in self.users:
            if user.roll==roll:
                print("User already Exist")
                return
        else:
            self.users.append(newUser)
            print("Registration Successfull")
            return
    def Login(self,roll,password):
        for user in self.users:
            if user.roll==roll and user.password!=password:
                print("Incorrect Password")
                return
            elif user.roll==roll and user.password==password:
                user.logged_in=True
                print("Login Successful")
                return
        print("User not found")
    def viewProfile(self,roll):
        for user in self.users:
            if user.roll==roll:
                if user.logged_in:
                    print(f"Name: {user.name}")
                    print(f"Roll: {user.roll}")
                    print(f"Mail: {user.mail}")
                    return
                else:
                    print("Please Login to view Profile")
                    return
        print("User not Found")
        return
    def logout(self,roll):
        for user in self.users:
            if user.roll==roll:
                user.logged_in=False
                print("Logout Successful")
                return
        print("User not Found")
        return
start=Enter()
while True:
    choose=input("Registration or Login or View Profile or Logout or Exit: ")
    if choose=="Registration":
        n=input("Name: ")
        r=input("Roll No: ")
        m=input("Mail:")
        p=input("Password: ")
        start.Register(n,r,m,p)
    elif choose=="Login":
        r=input("Roll No: ")
        p=input("Password: ")
        start.Login(r,p)
    elif choose=="View Profile":
        r=input("Roll: ")
        start.viewProfile(r)
    elif choose=="Logout":
        r=input("Roll: ")
        start.logout(r)
    elif choose=="Exit":
        break


