'''
Created on Jun 6, 2020

@author: elProf
'''
import serial

class ComMngr(object):


    def __init__(self, com_port):
        self.com_port = com_port
    
    
    def comMngr_initialize(self):
        try:
            self.com_port = serial.Serial(port = self.com_port,  baudrate=9600  , timeout = 5, 
                                           parity = serial.PARITY_NONE  , stopbits = serial.STOPBITS_ONE , 
                                           bytesize = serial.EIGHTBITS)
                                          
        except Exception as e:
            return e
        
        return 'OK'
    
    def comMngr_send_data(self , data):
        #Append len of data in the first byte
        try:
            data.insert(0 , len(data))
            self.com_port.write(data)
            return 'OK'
        except Exception as e:
            return e
    
    def comMngr_receive_int_data(self , length):
        try:         
            data = int.from_bytes(self.com_port.read(length),'big')         
            return 'OK' , data
        except Exception as e:
            return e
    