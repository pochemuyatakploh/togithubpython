import subprocess
import traceback

from kivy.uix.relativelayout import RelativeLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.button import Button
from threading import Thread
from kivy.clock import Clock
import threading
from PyQt5 import QtBluetooth
Window.size = (480,853)
mutex = threading.Lock()


list = ['arrow-top-left','arrow-up-bold-outline','arrow-top-right','arrow-left-bold-outline','car-light-dimmed','arrow-right-bold-outline','arrow-bottom-left','arrow-down-bold-outline','arrow-bottom-right']

class Container(BoxLayout):

    def __init__(self):
        super().__init__()
        self.tr1 = Thread(target=self.devices())
        self.tr1.start()
        self.sock.connected.connect(self.connectedToBluetooth)
        self.layout = RelativeLayout(size =(300, 300))

        self.ctrl = MDIconButton(icon = str(list[0]), pos = (50,50))


        #self.ctrl.bind(on_press=self._on_press)
        #self.ctrl.bind(on_release=self._on_release)
        self.layout.add_widget(self.ctrl)

        self.add_widget(self.layout, index = 1)


    def devices(self):
        self.sock = QtBluetooth.QBluetoothSocket(QtBluetooth.QBluetoothServiceInfo.RfcommProtocol)
        port = 1
        self.sock.connectToService(QtBluetooth.QBluetoothAddress("98:D3:39:30:02:80"), port)

    def connectedToBluetooth(self):
        self.sock.write('1'.encode())
        print("done!")


class mainapp(MDApp):
    def build(self):
        c = Container()
        return c


if __name__ == '__main__':
    mainapp().run()
