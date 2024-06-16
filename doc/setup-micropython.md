# Setup for MicroPython

## About

This document describes the setup of the Micropython environment for the ESP32 C3 microcontroller. All parameters and file names are documented as they were used when creating this project. They may need to be adjusted to your specific setup since versions can change or the port for your ESP32 C3 may be different.

## Software

Software in this section is required to setup the Micropython environment for the ESP32 C3 microcontroller to use it in a very basic setup from the command line.

With other software the setup and usage might become easier, e.g. using an IDE like Thonny or Visual Studio Code with the Pymakr plugin. This document does not cover these setups.

Additionally you will need a terminal program to connect to the ESP32 C3 via serial connection. For Windows you can use [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) or [Tera Term](https://ttssh2.osdn.jp/index.html.en).

### USB Driver

To connect the ESP32 C3 to your computer, you will need an driver for the USP-to-UART-bridge as described [here](https://docs.espressif.com/projects/esp-idf/en/v5.2.2/esp32c3/get-started/establish-serial-connection.html#connect-esp32-c3-to-pc).  
I used the USB driver from [Silicon Labs](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) which is linked on this page.

### Python

[Python](https://www.python.org/downloads/) is required to execute many tools which are written in Python, e.g. esptool.py. Take care to also install `pip` and add Python to the PATH. Increase max PATH length is recommended.

### esptool

Install esptool with pip from command line. esptool is necessary to flash the esp32 with Micropython.

```PS
pip install esptool
```

### adafruit-ampy

Install [adafruit-ampy](https://pypi.org/project/adafruit-ampy/) from command line. ampy is necessary to copy Micropython files on the esp32.

```PS
pip install adafruit-ampy
```

### Micropython Firmware

Download the latest Micropython firmware for the ESP32 from the [Micropython download page](https://micropython.org/download/). Be sure to download the specific firmware for your microcontroller. For the ESP32 C3, the firmware can be found [here](https://micropython.org/download/ESP32_GENERIC_C3/).

## Configuration

To use Micropython with the ESP32 C3, the Micropython firmware must be flashed to the ESP32. It's recommended to erase the flash before flashing the firmware.

```PS
esptool --port COM11 erase_flash

esptool --chip esp32c3 --port COM11 --baud 460800 write_flash -z 0x0 ESP32_GENERIC_C3-20240222-v1.22.2.bin
```

Now you're done and you can copy your Micropython files to the ESP32 with ampy. For details see examples in [../src](../src).

## Helpful Links

- [Micropython](https://micropython.org/)
- [Micropython Documentation](https://docs.micropython.org/en/latest/)
- [Micropython Tutorial](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- [Micropython Firmware](https://micropython.org/download/)
