from Screen import Screen
from ScreenRemoteDataCenter import ScreenRemoteDataCenter
from EmbededSystem import EmbededSystem
from Remote import Remote
from RemoteDataCenter import RemoteDataCenter
from Communication import Communication
from queue import Queue


class Main():
    globalsVariable = {}

    def __init__(self):
        self.globalsVariable["Screen"] = Screen
        self.globalsVariable["ScreenRemoteDataCenter"] = ScreenRemoteDataCenter
        self.globalsVariable["EmbededSystem"] = EmbededSystem
        self.globalsVariable["Remote"] = Remote
        self.globalsVariable["RemoteDataCenter"] = RemoteDataCenter
        self.globalsVariable["OneQueue"] = Queue()
        self.globalsVariable["TwoQueue"] = Queue()
        self.globalsVariable['Ports'] = {
            "Bms": {
                "port": None,
                "baudrate": None
            },
            "Arduino": {
                "port": None,
                "baudrate": None
            },
            "Remote": {
                "port": None,
                "baudrate": None
            },
            "RemoteDataCenter": {
                "port": None,
                "baudrate": None
            },
        }
        self.globalsVariable['Ports'] = Communication().Serial_Port_Choose()
        if self.globalsVariable['Ports']['Bms']['port'] is not None or self.globalsVariable['Ports']['Arduino'][
            'port'] is not None:
            self.globalsVariable["EmbededSystem"] = self.globalsVariable["EmbededSystem"](self.globalsVariable,
                                                                                          self.globalsVariable['Ports'][
                                                                                              'Arduino']['port'],
                                                                                          self.globalsVariable['Ports'][
                                                                                              'Arduino']['baudrate'],
                                                                                          self.globalsVariable['Ports'][
                                                                                              'Bms']['port'],
                                                                                          self.globalsVariable['Ports'][
                                                                                              'Bms']['baudrate'])
        if self.globalsVariable['Ports']['Remote']['port'] is not None:

            self.globalsVariable["Remote"] = self.globalsVariable["Remote"](self.globalsVariable,self.globalsVariable['Ports']['Remote']['port'],self.globalsVariable['Ports']['Remote']['baudrate'])

        if self.globalsVariable['Ports']['RemoteDataCenter']['port'] is not None:
            self.globalsVariable["RemoteDataCenter"] = self.globalsVariable["RemoteDataCenter"](self.globalsVariable,
                                                                                                self.globalsVariable[
                                                                                                    'Ports'][
                                                                                                    'RemoteDataCenter'][
                                                                                                    'port'],
                                                                                                self.globalsVariable[
                                                                                                    'Ports'][
                                                                                                    'RemoteDataCenter'][
                                                                                                    'baudrate'])
            self.globalsVariable["ScreenRemoteDataCenter"](self.globalsVariable)

        elif self.globalsVariable['Ports']['Bms']['port'] is not None or self.globalsVariable['Ports']['Arduino'][
            'port'] is not None:
            self.globalsVariable["Screen"](self.globalsVariable)


if __name__ == '__main__':
    Main()
