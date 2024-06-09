# Versuch 1 mit DFPlayer
import time
from dfplayer import DFPlayer

def read(uart, tx_pin = None, rx_pin = None):
    try:
        print("Using UART {0}, tx {1} rx {2}".format(uart, tx_pin, rx_pin))
        time.sleep(0.8)
        df=DFPlayer(uart,tx_pin_id=tx_pin,rx_pin_id=rx_pin)
        time.sleep(0.2)

        print("Set volume to 12")
        df.volume(12)
        time.sleep(0.2)

        # print("Play 01/001.mp3")
        # df.play(1,1)
        # time.sleep(4)

        print("Play 2/001.mp3")
        df.play(2,1)
        time.sleep(6)

        df.stop()
        time.sleep(0.2)

        print("Read volume", df.get_volume())
        time.sleep(0.2)

        print("Folder 01", df.get_files_in_folder(1))
        time.sleep(0.2)

        print("Folder 02", df.get_files_in_folder(2))
        time.sleep(0.2)
    
    except Exception as e:
        print("Error: ", e)

try:
    for i in range(0, 4):
        time.sleep(1)
        print("Waiting", i)
    #read(0)
    # read(uart=1)                      # ok
    # read(uart=1,tx_pin=9, rx_pin=10)  # -
    # read(uart=1,tx_pin=12, rx_pin=7)  # ok
    # read(uart=1,tx_pin=7, rx_pin=12)  # ok

    #read(0,21,20)
    #read(1,21,20)

    # It was found that the combination of TX 10 and RX 9 works
    # Based on this, further investigation will be done to determine which combinations work

    # Investigate RX-Pin
    # read(uart=1,tx_pin=10, rx_pin=1)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=2)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=3)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=4)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=5)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=6)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=7)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=8)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=10)  # -
    # read(uart=1,tx_pin=10, rx_pin=11)  # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=12)  # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=13)  # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=14)  # err
    # read(uart=1,tx_pin=10, rx_pin=15)  # err
    # read(uart=1,tx_pin=10, rx_pin=16)  # err
    # read(uart=1,tx_pin=10, rx_pin=17)  # err
    # read(uart=1,tx_pin=10, rx_pin=18)  # err
    # read(uart=1,tx_pin=10, rx_pin=19)  # err
    # read(uart=1,tx_pin=10, rx_pin=20)  # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=21)  # blk

    # Investigate TX-Pin
    # read(uart=1,tx_pin=1, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=2, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=3, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=4, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=5, rx_pin=9)   # Sound yes - Read no
    read(uart=1,tx_pin=6, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=7, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=8, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=9, rx_pin=9)   # Sound yes - Read no
    # read(uart=1,tx_pin=10, rx_pin=9)  # Sound yes - Read no
    # read(uart=1,tx_pin=11, rx_pin=9)  # Sound yes - Read no
    # read(uart=1,tx_pin=12, rx_pin=9)  # Sound yes - Read no
    # read(uart=1,tx_pin=13, rx_pin=9)  # Sound yes - Read no
    # read(uart=1,tx_pin=14, rx_pin=9)  # err
    # read(uart=1,tx_pin=15, rx_pin=9)  # err
    # read(uart=1,tx_pin=16, rx_pin=9)  # err
    # read(uart=1,tx_pin=17, rx_pin=9)  # err
    # read(uart=1,tx_pin=18, rx_pin=9)  # err
    # read(uart=1,tx_pin=19, rx_pin=9)  # err
    # read(uart=1,tx_pin=20, rx_pin=9)  # Sound yes - Read no
    # read(uart=1,tx_pin=21, rx_pin=9)  # blk
except Exception as e:
    print("Error: ", e)


# df.volume(25)
# print("Volume set")
# time.sleep(0.2)
# #play file ./01/001.mp3
# df.play(1,1)
# print("Playing track 1")