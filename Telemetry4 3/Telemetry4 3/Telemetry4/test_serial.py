from Communication import Communication

RemoteDataCenterSerial=Communication()
RemoteDataCenterSerial.Serial_Open("/dev/tty.usbserial-1410",9600)
while 1:
    if RemoteDataCenterSerial.Serial_isOpen():
        serialString = RemoteDataCenterSerial.Serial_Read()
        if serialString is not None and serialString != "":
            print(serialString)
    else:
        print("not found")



_tempSerialString = serialString
                    serialString = serialString.split(':')
                    