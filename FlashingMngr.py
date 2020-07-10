'''
Created on Jun 5, 2020

@author: elProf
'''

from intelhex import IntelHex
from  ComMngr import *
from t import bin_data


class FlashingMngr(object):

    def __init__(self, ui_obj , com_mngr_obj):
        self.hex_file = ui_obj.pathText.text()
        self.com_mngr = com_mngr_obj
        self.ui = ui_obj
    def parse_hex_file(self): 
        try:               
            hex_obj = IntelHex()                     # create empty object
            hex_obj.fromfile(self.hex_file,format='hex')             # load from hex
            #Parse hex file to binary array
            bin_data = hex_obj.tobinarray()
            #Padding the hex data with 0xFF 
            #consider Page size = 128Byte
            padding_size = 128 - (len(bin_data)%128)
            bin_data.extend([0xff]*padding_size)
            self.bin_data = bin_data.tolist()    
        except:
            return 'NOK' , 'Error in parsing File'
        else:
            return 'OK'

    def send_programming_session(self):
        try:                  
            prog_session = [0x10] + [0x03]
            state = self.com_mngr.comMngr_initialize()
            if(state != 'OK'):
                raise state
            
            state = self.com_mngr.comMngr_send_data(prog_session)
            if(state != 'OK'):
                raise state 
            
            state , response = self.com_mngr.comMngr_receive_int_data(length = 1)
            if(state == 'OK') :
                assert(response == 0x50)
            else:
                raise state
                
        except AssertionError:
            return 'NOK' , 'response NOK, expected 0x50, received ' + hex(response)
            
        except Exception as e :
            return 'NOK' , str(e)
        
        self.ui.progressBar.setValue(20)
        return 'OK'
        
    def request_download(self):
        try :            
            code_size = len(self.bin_data).to_bytes(2, byteorder='big')
            request_download = [0x34] + list(code_size)
            state = self.com_mngr.comMngr_send_data(request_download)
            if(state !='OK'):
                raise state
            
            state , response = self.com_mngr.comMngr_receive_int_data(length = 1)
            if(state == 'OK'):
                assert(response == 0x74)
            else:
                raise  state
                
        except AssertionError:
            return 'NOK' , 'response NOK, expected 0x74, received ' + hex(response)
        
        except Exception as e :
            return 'NOK' , str(e)
         
        self.ui.progressBar.setValue(40)   
        return 'OK'

    def transfer_data(self):
        block_size = 128      
        try :            
            for start in range(0 , len(self.bin_data) , block_size):
                end = start + block_size
                if end > len(self.bin_data):
                    end = len(self.bin_data)
                transfer_data = [0x36] + self.bin_data[start:end]
                state = self.com_mngr.comMngr_send_data(transfer_data)
                if(state !='OK'):
                    raise state
                
                state , response = self.com_mngr.comMngr_receive_int_data(length = 1)
                if(state == 'OK'):
                    assert(response == 0x76)
                else:
                    raise state
                
        except AssertionError:
            return 'NOK' , 'response NOK, expected 0x76, received ' + hex(response)
        
        except Exception as e :
            return 'NOK' , str(e)
        
        self.ui.progressBar.setValue(60) 
        return 'OK'  
    
    def request_transfer_exit(self):        
        try:                
            state = self.com_mngr.comMngr_send_data([0x37])
            if(state != 'OK'):
                raise state
            
            state , response = self.com_mngr.comMngr_receive_int_data(length = 1)
            if(state == 'OK'):    
                assert(response == 0x77)
            else:
                raise state
            
        except AssertionError:
            return 'NOK' , 'response NOK, expected 0x77, received ' + hex(response)
        
        except Exception as e :
            return 'NOK' , str(e)       
        
        self.ui.progressBar.setValue(80) 
        return 'OK'
    
    def check_crc(self):
        try:
            crc16 = 0xFFFF
            for byte in self.bin_data:
                crc16 ^= byte;
                for i in range (8):
                    if (crc16 & 1):
                        crc16 = (crc16 >> 1) ^ 0xA001;
                    else:
                        crc16 = (crc16 >> 1)
            crc16 = list(crc16.to_bytes(2, byteorder='big'))
            
            crc_req = [0x31] + crc16
            state = self.com_mngr.comMngr_send_data(crc_req)
            if(state != 'OK'):
                raise state
            
            state , response = self.com_mngr.comMngr_receive_int_data(length = 1)
            if(state == 'OK'):
                assert(response == 0x71)
            else:
                raise state    
        except AssertionError:
            return 'NOK' , 'response NOK, expected 0x71, received ' + hex(response)
        
        except Exception as e :
            return 'NOK' , str(e)       
        
        self.ui.progressBar.setValue(100) 
        return 'OK'
      
    flashing_seq = {
        0: 'parse_hex_file',
        1: 'send_programming_session',
        2: 'request_download',
        3: 'transfer_data' ,
        4: 'request_transfer_exit' ,
        5: 'check_crc'
        }

    def seq_handler(self , step):
        method_name =self.flashing_seq.get(step,lambda :'Invalid')
        method=getattr(self,method_name,lambda :'Invalid')
        
        return method()
            
    def start_flashing(self):      
        for step in range (0,len(self.flashing_seq)):    
            state , msg = self.seq_handler(step) 
            print('step ' , step , 'is ' , state)
            if(state == 'NOK'):
                return state , msg
        
        return 'OK' , 'Download Completed!'            