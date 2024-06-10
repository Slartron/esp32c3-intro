import network
import socket

import esp
esp.osdebug(None)

import gc
gc.collect()

try:
    ap_nic = network.WLAN(network.AP_IF) # create access-point interface
    ap_nic.config(essid='esp32',   authmode=network.AUTH_WPA_WPA2_PSK, password='abcd1234')
    ap_nic.active(True)

    print("Config ", ap_nic.ifconfig())
    print("Active ", ap_nic.active())

    print("Waiting for connection...")

    while (ap_nic.active() == False):
        pass

    print('Connection successful')

    print(ap_nic.ifconfig())

    def web_page():
        html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
        <body><h1>Hello, World!</h1></body></html>"""
        return html

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        print('Content = %s' % str(request))
        response = web_page()
        conn.send(response)
        conn.close()

except Exception as e:
    print('Error: ', e)
