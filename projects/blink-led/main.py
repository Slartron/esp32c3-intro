import machine, neopixel, time

np = neopixel.NeoPixel(machine.Pin(8), 2)

while True:
    # Red
    np[0] = (10, 0, 0)
    np.write()
    time.sleep(1)
    # Green
    np[0] = (0, 10, 0)
    np.write()
    time.sleep(1)
    # Blue
    np[0] = (0, 0, 10)
    np.write()
    time.sleep(1)
    # White (short flash)
    np[0] = (20, 20, 20)
    np.write()
    time.sleep(0.07)
    # Off
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)