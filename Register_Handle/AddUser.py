import connectSql as _connect
import HashingPassword

def SameUserCheck(account):
    db = _connect.Connect_To_CloudSQL('userData')
    cursor = db.cursor()
    cursor.execute("SELECT EXISTS(select * from user where username = %s)" ,
        (account,))
    result = cursor.fetchall()
    for row in result:
        if row[0] == 1: #Have same account name
            return False
        else:
            return True

def InsertUser(account, password):
    password = HashingPassword.hashSafe(password)

    db = _connect.Connect_To_CloudSQL('userData')
    cursor = db.cursor()
    cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)" ,
        (account, password,))
    db.commit()