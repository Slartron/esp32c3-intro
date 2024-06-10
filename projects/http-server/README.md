# ESP32-C3 as Web Server

## About

This micropython app demonstrates how to setup a web server on an ESP32-C3 and serve HTTP requests. It's a [esp32-intro](../../README.md) project.

## Hardware

- [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)

## Wiring

No wiring required.

## Getting started

For required software and installation, see [Micropython Setup](../../doc/setup-micropython.md)

## Programming

See example code in [src](./src/) folder. The code is from [Programming an Access Point](https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/).

## Building

Nothing to build

## Flashing

Copy file to controller with

```PS
 ampy -p COM11 put .\src\wlan-ap-demo.py boot.py
```

ATTENTION: Any existing `boot.py` will be overwritten. To backup the existing `boot.py` file and to restore it, use the following commands:

```PS
# backup
 ampy -p COM11 get boot.py boot.py.bak
# restore
 ampy -p COM11 put boot.py.bak boot.py
```

## Running

Running the app with `ampy run...` did not work. Before I was able to connect to the access point I received the following error:
`ampy.pyboard.PyboardError: timeout waiting for first EOF reception`

## Helpful links

- [Programming an Access Point](https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/))
