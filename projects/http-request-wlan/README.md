# Access Internet via WLAN

## About

This micropython app demonstrates how to connect to a WLAN and send a HTTP request. It's a [esp32-intro](../../README.md) project.

## Hardware

- [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)

## Wiring

No wiring required.

## Getting started

For required software and installation, see [Micropython Setup](../../doc/setup-micropython.md)

## Programming

The easiest way to do HTTP requests is to use a module like `urequests` module. There are other modules available, see [PyPi for micropython-urequests](https://pypi.org/project/micropython-urequests/).

When using `urequests`, you might run into memory allocation issues (`Error:  memory allocation failed, allocating 64000 bytes`). This could be solved by using a socket and read the response in chunks from the stream. See [source code of urequests](<[src/urequests.py](https://github.com/pfalcon/pycopy-lib/blob/master/urequests/urequests/__init__.py)>) for an example.

Querying data from the internet requires two major steps:

1. Connect to the WLAN
2. Send the HTTP request

## Building

Nothing to build

## Flashing

Nothing to flash

## Running

Run the app with

```PS
ampy -p COM11 run .\src\wlan-demo.py
```

## Helpful links

None until now.
;-)
