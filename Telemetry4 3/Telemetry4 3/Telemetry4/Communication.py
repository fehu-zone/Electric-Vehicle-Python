import glob
import json

import serial
import sys
import os


class Communication:
    ser = None
    file = "Config.json"

    def __init__(self):
        self.status = False

    def Serial_isOpen(self):
        if self.ser is None:
            return False
        elif self.ser.isOpen() and self.status:
            return True
        else:

            self.status = False
        return False

    def Serial_Open(self, port, baudrate):
        try:
            while not self.Serial_isOpen():
                self.ser = serial.Serial(port=port, baudrate=baudrate)
                self.status = True
        except:
            self.status = False

    def Serial_Send(self, data):
        try:
            data += '\n'
            self.ser.write(data.encode())
        except:
            self.status = False
            print("Error Serial Send Data Code:104 Class:Communication")

    def Serial_Read(self):
        waiting = self.ser.inWaiting()
        if waiting > 0:
            chars = ""
            while True:
                char = self.ser.read().decode().replace('\r', '').replace('\t', '')

                if char == "\n":
                    return chars
                chars += char

            return chars
        else:
            return None

    def Serial_Close(self):
        if self.ser is not None:
            self.ser.close()
        return True

    def Serial_Port_List(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass

        return result

    def JsonFileSave(self, data, file=None):
        if file is None:
            file = self.file
        f = open(file, 'w+')
        f.write(json.dumps(data))
        f.close()
        return self

    def JsonFileRead(self, file=None):
        if file is None:
            file = self.file
        if os.path.isfile(file):
            f = open(file, 'r+')
            data = f.read()
            f.close()
            if data == "":
                return {}
            else:
                return json.loads(data)
        else:
            return {}

    def Conf_or_User_Question_Port(self, id):
        Conf = self.JsonFileRead()
        PortsList = self.Serial_Port_List()
        port = None
        if (
                (id in Conf.keys()) and
                (Conf[id]['port'] is not None) and
                (Conf[id]['port'] in PortsList)
        ) is False:
            while (port is None) or (
                    (len(PortsList) + 1) < port) or (1 > port):
                port = int(input(id + " Port:"))
            if (len(PortsList) + 1) == port:
                port = None
                baudrate = None
            else:
                port = PortsList[(port - 1)]
                baudrate = int(input(id + " Baudrate:"))
        else:
            port=Conf[id]['port']
            baudrate=Conf[id]['baudrate']
        return {"port": port, "baudrate": baudrate}

    def Serial_Port_Choose(self):
        i = 1
        PortsList = self.Serial_Port_List()
        for port in PortsList:
            print(str(i) + ") " + port)
            i += 1
        print(str(i) + ") Pass")
        Ports = {
            "Bms": self.Conf_or_User_Question_Port('Bms'),
            "Arduino": self.Conf_or_User_Question_Port('Arduino'),
            "Remote": self.Conf_or_User_Question_Port('Remote'),
            "RemoteDataCenter": {"port": None, "baudrate": None}
        }
        if Ports['Bms']['port'] is None and Ports['Arduino']['port'] is None and Ports['Remote']['port'] is None and \
                Ports[
                    'RemoteDataCenter']['port'] is None:
            Ports['RemoteDataCenter'] = self.Conf_or_User_Question_Port('RemoteDataCenter')
        self.JsonFileSave(Ports)
        return Ports
