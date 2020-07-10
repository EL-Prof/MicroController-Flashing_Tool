'''
Created on Jun 5, 2020

@author: elProf
'''
import sys
from PyQt5 import QtWidgets
from GUI import Ui_Form
from PyQt5.Qt import QFileDialog
from FlashingMngr import FlashingMngr
from PyQt5.QtWidgets import QMessageBox
import serial.tools.list_ports
from ComMngr import ComMngr

def openHexFile(self):
    fileName = QFileDialog.getOpenFileName(filter ="hex Files (*.hex)" , directory = ".")
    ui.pathText.setText(fileName[0])

def show_msg(title, icon, text):
    msg_box = QMessageBox()
    msg_box.setIcon(icon)
    msg_box.setText(text)
    msg_box.setWindowTitle(title)
    msg_box.exec_()

def dispatch_flashing():
    mngr = FlashingMngr(ui_obj= ui , com_mngr_obj= ComMngr(str(ui.comPortText.text()) ) )
    status, msg = mngr.start_flashing()
            
    if (status == 'NOK'):
        show_msg('Error', QMessageBox.Critical, msg)    
    
    else:
        show_msg('Done!', QMessageBox.Information, 'Flashing completed successfully')    

    
def startFlashing(self):
    
    ui.progressBar.setValue(0)
    if(ui.comPortText != None):     
        if(ui.pathText.text() != None):       
            dispatch_flashing()

        else:
            show_msg('Error', QMessageBox.Critical, 'Please specify Hex File path')
    else:
        show_msg('Error', QMessageBox.Critical, 'Please specify COM PORT')        

def get_port():
#     import serial.tools.list_ports   # import serial module
    comPorts = list(serial.tools.list_ports.comports())    # get list of all devices connected through serial port
    for port in comPorts:
        if('Prolific USB-to-Serial Comm Port' in str(port)):
            ui.comPortText.setText(port.device)
            return
    
    show_msg('Not found!', QMessageBox.Warning, "com port can't be detected")   
        

    



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.loadButton.clicked.connect(openHexFile)
    ui.detectButton.clicked.connect(get_port)
    ui.startButton.clicked.connect(startFlashing)
    sys.exit(app.exec_())
