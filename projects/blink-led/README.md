# Let it blink

## About

This micropython app demonstrates how to use the `NeoPixel` class to blink the programmalbe onboard LED on a EPS32 C3 micro controller. It's a [esp32-intro](../../README.md) project.

## Hardware

- [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)

## Getting started

For required software and installation, see [Micropython Setup](../../doc/setup-micropython.md)

## Building

Nothing to build

## Flashing

Copy file to controller with

```PS
 ampy -p COM11 -b 115200 put .\main.py
```

## Running

Execution starts automatically when controller is reset.
