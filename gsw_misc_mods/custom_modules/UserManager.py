

class Person:
    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.gender = ''

    def setFname(self, fname):
        self.fname = fname

    def setLname(self, lname):
        self.lname = lname

    def setGender(self, gender):
        self.gender = gender

    def getFname(self):
        return self.fname

    def getLname(self):
        return self.lname

    def getGender(self):
        return self.gender

    def to_string():
        return "Person"


class User(Person):
    def __init__(self):
        super().__init__
        self.email = ''
        self.username = ''

    def setUsername(self, username):
        self.username = username

    def setEmail(self, email):
        self.email = email

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def printUser(self):
        print("\n\tUsername: {}\n\tEmail: {}\n\n".format(
            str(self.username), str(self.email)))

    def to_string():
        return "User"


class Users:
    def __init__(self):
        self.users = dict()

    def addUser(self, user):
        if (self.checkEmailExists(user.email)):
            print("\n\tEmail: {} is already registerd\n".format(user.email))
        elif (self.checkUsernameExists(user.username)):
            print("\n\tUsername: {} is already in use".format(user.username))
        else:
            self.users.update({user.email, user})

    def removeUser(self, email):
        if type(self.users[email]) != None:
            del self.users[email]
        else:
            print("\n\tUser: {} does not exists".format(email))

    def userCount(self):
        return len(self.users)

    def checkEmailExists(self, email):
        return type(self.users[email]) == None

    def checkUsernameExists(self, username):
        for u in self.users:
            user = self.users[u]
            if user.username == username:
                return True
        return False

    def printUsers(self):
        for u in self.users:
            print("\t{}\n".format(str(u)))

    def to_string():
        return "Users"
