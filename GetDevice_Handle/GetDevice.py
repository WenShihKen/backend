import connectSql as _connect
import time

def getAllDevice(username):

    db = _connect.Connect_To_CloudSQL('userDevice')
    cursor = db.cursor()

    sql_string = "select * from {}".format(username)

    cursor.execute(sql_string)
    result = cursor.fetchall()

    YourDevice = []
    for row in result:
        YourDevice.append(row[1])

    db.close()
    return getDeviceInformation(YourDevice)

def getDeviceInformation(YourDevice):

    DeviceInformation = dict()
    
    for device_name in YourDevice:
        db = _connect.Connect_To_CloudSQL('sensorData')
        cursor = db.cursor()

        sql_string = "select * from {} where data_id=(SELECT MAX(data_id) FROM {})".format(device_name, device_name)

        cursor.execute(sql_string)

        GetRecentData = cursor.fetchone()

        DeviceInformation[device_name] = GetRecentData

        db.close()
    
    return DeviceInformation