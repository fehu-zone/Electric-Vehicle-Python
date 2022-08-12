from PIL import ImageTk, Image

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import os

from Threads import Threads


class Screen:
    g = 0
    W = 800
    H = 480
    CanvasItemList = {}
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

    def resource_path(self, relative_path):

       

    def __init__(self, globalsVariable):
        

    def ImageGridToPx(self, row, col, img, rows=24, cols=24, line=0):
        

    def TextGridToPx(self, row, col, TextPt, len, rows=24, cols=24, line=0):
        

    def oneScreen(self):
        

    def twoScreen(self):
        

        Speed = self.ImageGridToPx(12, 8, "/Speed/0.png")
        

        Rpm = self.ImageGridToPx(12, 20, "/Rpm/1.png")
        

        BatteryTemp = self.ImageGridToPx(3, 4, "/BatteryTemp/0-50.png")
        

        BatteryPercent = self.ImageGridToPx(3, 12, "/BatteryPercent/0-20.png")
        
        EngineTemp = self.ImageGridToPx(3, 20, "/EngineTemp/0-50.png")
        
        BatteryWatt = self.ImageGridToPx(21, 3, "/BatteryWatt/1.png")
        
        BatteryVolt = self.ImageGridToPx(21, 9, "/BatteryVolt/1.png")
       

        BatteryCurrent = self.ImageGridToPx(21, 15, "/BatteryCurrent/1.png")
        

        BatteryConnection = self.ImageGridToPx(21, 19, "/BatteryConnection/1.png")
        
        EngineConnection = self.ImageGridToPx(21, 23, "/EngineConnection/1.png")
        
        self.Threads('ScreenUpdateData', self.updateData, (self.globalsVariable,))
        self.Threads.Run_Function(self.Threads, 'ScreenUpdateData')
        print("Screen Actived Class:Screen")
        root.mainloop()

    def updateData(self, globalsVariable):
        
        while 1:
            
    def editBatteryPercent(self, percent: int = 0):
        

    def editBatteryTemp(self, temp: int = 0):
        

    def editRpm(self, rpm: int = 0):
       

    def editSpeed(self, speed: int = 0):
       

    def editEngineTemp(self, temp: int = 0):
        

    def editWatt(self, watt):
       
    def editAmper(self, amper):
       

    def editBatteryCells(self, cells):
        
    def editEngineStatus(self, status):
        

    def editBatteryStatus(self, status):
        

    def editVolt(self, volt):
       