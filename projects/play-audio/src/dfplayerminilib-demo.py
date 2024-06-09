# Versuch 2 mit dfplayermini

from dfplayerminilib import Player

from time import sleep



def play():
    print("Playing")
    music.play(2,1)

def getVol():
    vol = music.get_volume()
    print("Volume: {0}".format(vol))

def pause():
    music.pause()
    print("Player paused")

def resume():
    music.resume()
    print("Player resumed")

def stop():
    music.stop()
    print("Player stopped")

print("Player init")

music = Player(pin_TX=6, pin_RX=9)


music.volume(15)
getVol()

play()
sleep(5)

pause()
sleep(2)

music.volume(25)
getVol()

resume()
sleep(5)

stop()