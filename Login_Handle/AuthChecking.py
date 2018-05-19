import connectSql as _connect
import HashingPassword

def LoginCheck(account, password):
    password = HashingPassword.hashSafe(password)

    db = _connect.Connect_To_CloudSQL('UserData')
    cursor = db.cursor()
    cursor.execute("SELECT EXISTS(select * from user where username = %s AND password = %s)" ,
        (account , password,))
    result = cursor.fetchall()
    for row in result:
        if row[0] == 1:
            return True
        else:
            return False