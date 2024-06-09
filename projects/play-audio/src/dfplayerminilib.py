## Credits to lavron
## https://raw.githubusercontent.com/lavron/micropython-dfplayermini

import time
from machine import UART

IDLE = 0
PAUSED = 1
PLAYING = 2


class Player:
    def __init__(self, pin_TX, pin_RX):
        self.uart = UART(1, 9600)
        self.uart.init(9600, bits=8, parity=None, stop=1, tx=pin_TX, rx=pin_RX)

    def send_cmd(self,cmd,param1=0,param2=0):
        out_bytes = bytearray(10)
        out_bytes[0]=126        # start byte
        out_bytes[1]=255        # version
        out_bytes[2]=6          # length
        out_bytes[3]=cmd        # command
        out_bytes[4]=0          # feedback
        out_bytes[5]=param1     # parameter 1
        out_bytes[6]=param2     # parameter 2
        out_bytes[9]=239        # end byte
        checksum = 0
        for i in range(1,7):
            checksum=checksum+out_bytes[i]
        out_bytes[7]=(checksum>>7)-1
        out_bytes[7]=~out_bytes[7]
        out_bytes[8]=checksum-1
        out_bytes[8]=~out_bytes[8]
        self.uart.write(out_bytes)
        # after each command give the module some time to process
        time.sleep(0.5)

    def send_query(self,cmd,param1=0,param2=0):
        retry=3
        while (retry > 0):
            self.flush()
            self.send_cmd(cmd,param1,param2)
            in_bytes = self.uart.read()
            # give the module some time (don't know if this is REALLY necessary)
            time.sleep(0.5)
            if not in_bytes: #timeout
                return -1
            # debugging code
            # for i in range(len(in_bytes)):
            #     print("raw - i: {0} value: {1}".format(i,in_bytes[i]))
            if (in_bytes[3] == 64): # error
                retry = retry - 1
            elif len(in_bytes)==10 and in_bytes[1]==255 and in_bytes[9]==239 and in_bytes[3]==cmd:
                return in_bytes[6]
        return in_bytes
    
    def flush(self):
        self.uart.flush()
        if self.uart.any():
            self.uart.read()

    # playback

    def stop(self):
        self.send_cmd(22,0,0)

    def play(self,folder,file):
        self.stop()
        self.send_cmd(15,folder,file)

    def pause(self):
        self.send_cmd(14)

    def resume(self):
        self.send_cmd(13)

    # volume control

    def volume(self,vol):
        self.send_cmd(6,0,vol)

    def volume_down(self):
        self.send_cmd(5)

    def volume_up(self):
        self.send_cmd(4)
        
    # module

    def reset(self):
        self.send_cmd(12)

    # queries

    # 66 - 0x42 - status
    # 67 - 0x43 - volume
    # 68 - 0x44 - eq
    # 69 - 0x45 - playback mode

    def get_status(self):
        in_bytes = self.send_query(66)
        return in_bytes
    
    def get_volume(self):
        in_bytes = self.send_query(67)
        return in_bytes
    
    def get_equalizer(self):
        in_bytes = self.send_query(68)
        return in_bytes
    
    def get_playbackmode(self):
        in_bytes = self.send_query(69)
        return in_bytes