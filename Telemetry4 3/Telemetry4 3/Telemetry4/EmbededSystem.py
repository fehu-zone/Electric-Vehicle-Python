import time
from Communication import Communication
from Threads import Threads


class EmbededSystem:
    maxVolt = 4.2
    minVolt = 3.6
    conf = {
        "SpeedTemp": {
            "port": None,
            "baudrate": None
        },
        "Bms": {
            "port": None,
            "baudrate": None
        }
    }
    startTime = time.time()
    Variables = {
        "Data": {
            'watt': None,
            'volt': None,
            'battery': None,
            'batteryTemp': None,
            'amper': 0.0,
            'batteryStatus': None,
            'speedTempStatus': None,
            'speed': None,
            'engineTemp': None,
            'rpm': None,
            'period': None,
            'batteryCells': {}
        }
    }
    SpeedTempSerial = None
    BmsSerial = None
    SpeedTempError = 0
    BmsError = 0

    def __init__(self, globalsVariable, speedTempPort, speedTempBaudrate, bmsPort,
     

    def SpeedTempBackendRead(self, globalsVariable):
      
    def SpeedTempConnection(self):
       
    def EmbededSystemToScreen(self, dataName):
        self.globalsVariable["OneQueue"].put([dataName, self.Variables["Data"][dataName]])
        if (time.time()) - self.startTime >= 0.01:
            self.globalsVariable["TwoQueue"].put(self.Variables["Data"])
            self.startTime = time.time()

    def SpeedTempDataRead(self):
        

    def BmsConnection(self):
       
    def BmsBackendRead(self, globalsVariable):
        
    def BmsDataRead(self):
        
    def batteryVoltToPercent(self):
       
    def batteryTemptoFloat(self, T):
        