import os
import pyexcel
from netmiko import ConnectHandler



def retv_excel(par): #par = path
    d = {}
    records = pyexcel.iget_records(file_name=par)
    for record in records:
        d.update( { record['hostname'] : record{'driver'

def main():
    file_location = "/home/student/usopen/host_list.csv"

    entry = retv_excel(file_location)

def login_router(dev_type, dev_ip, dev_un, dev_pw)
    try:
        open_connection = ConnectHandler(device_type=dev_type,
            \ ip=dev_ip, username=dev_un, password=dev_pw
        return True
    except:
        return False
#ping check the router
#login check the router
#determin if interfaces in use are up
#
    print('**********begin SSH vhecking************')
    for x in entry.keys():
        #can we log in? this grabs switch, device type, login, password
        if login_router(str(entry[x]), x, "admin", "alta2"):
            print(connectionup)
        else:
            print(connection down)
main()
