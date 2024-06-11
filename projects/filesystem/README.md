# Accessing Files and Folders on the ESP32-C3

## About

This micropython app demonstrates how to explore the filesystem and how to read and write files. It's a [esp32-intro](../../README.md) project.

## Hardware

- [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)

## Wiring

No wiring required.

## Getting started

For required software and installation, see [Micropython Setup](../../doc/setup-micropython.md)

## Programming

Handling files and directories is done with the `os` module and works similar to other systems and programming languages.

Observation: I experienced with timestamps and discovered has no real time clock. That means it's necessary to adjust the onboard RTC to the current time, every time the board is powered up. This is could be done with the `ntptime` module. This is remembering to my first computer in the 80s. ;-)

## Building

Nothing to build

## Flashing

Nothing to flash

## Running

Run the app with

```PS
ampy -p COM11 run .\src\filesys-demo.py
```

## Helpful links

None until now.
;-)
