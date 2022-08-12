import time
from datetime import datetime
from Communication import Communication
from Threads import Threads


class RemoteDataCenter:
    conf = {
        "RemoteDataCenter": {
            "port": None,
            "baudrate": None
        }
    }
    Variables = {
        "Data": {
            'watt': None,
            'volt': None,
            'battery': None,
            'batteryTemp': None,
            'amper': None,
            'batteryStatus': None,
            'speedTempStatus': None,
            'speed': None,
            'engineTemp': None,
            'rpm': None,
            'period': None,
            'batteryCells': {}
        }
    }
    RemoteDataCenterSerial = None
    startTime = time.time()
    error = 0

    def __init__(self, globalsVariable, RemoteDataCenterPort, RemoteDataCenterBaudrate):
        

    def RemoteDataCenterBackendRead(self, globalsVariable):
       
    def RemoteDataCenterConnection(self):
        
    def RemoteDataCenterToScreen(self, dataName):
       
    def RemoteDataCenterDataRead(self):
        
        except Exception as e:
            
    def logSaved(self, serialString):
        