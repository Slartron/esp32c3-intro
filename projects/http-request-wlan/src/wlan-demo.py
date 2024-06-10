try:
    # Step 1: Connect to the WLAN
    import network
    import time

    # commented out to provoke an error during execution as a reminder to provice the correct values
    # ssid = '<YOUR SSID>'
    # password = '<YOUR PASSWORD>'

    sta_nic = network.WLAN(network.STA_IF) # important to create STATION interface
    sta_nic.active(True)

    print("Config ", sta_nic.ifconfig())
    print("Active ", sta_nic.active())
    print("Status ", sta_nic.status())
    print()

    print("Connect to WLAN:", ssid)
    if not sta_nic.isconnected():
        sta_nic.connect(ssid, password)
        print("Waiting for connection...")
        while not sta_nic.isconnected():
            time.sleep(1)

    print("Config ", sta_nic.ifconfig())
    print("Active ", sta_nic.active())
    print("Status ", sta_nic.status())
    print()



    # Step 2: Send the HTTP request
    import urequests

    print("Send HTTP request...")
    url = 'https://raw.githubusercontent.com/Slartron/esp32c3-intro/main/README.md'
    response = urequests.get(url)
    print(str(response.text, 'utf8'), end='')
    response.close()

except Exception as e:
    print('Error: ', e)