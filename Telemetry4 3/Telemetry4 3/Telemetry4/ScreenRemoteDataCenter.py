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


class ScreenRemoteDataCenter:
    g = 0
    W = 0
    H = 0
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
       