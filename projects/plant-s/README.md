# Plant-S

## About

This micropython app demonstrates a complete solution to measure moisture and to inform a user about the measured values. It's a [esp32-intro](../../README.md) project.  
The code is an assembly of the fragments from previous projects, especially from [Soil Moisture Sensor](projects/soil-moisture-sensor/README.md), [Playing Audio Files](projects/play-audio/README.md) and [Accessing Files and Folders](projects/filesystem/README.md). See the READMEs for details.

## Hardware

- [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)
- [Soil Moisture Sensor](https://wiki.seeedstudio.com/Grove-Capacitive_Moisture_Sensor-Corrosion-Resistant/)
- [DFPlayer mini](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299)
- Speaker: I found an speaker from a radio clock with 16 Ohm and 0.5 W. It worked fine for me and was not too loud. Nice for development.

## Wiring

| Cable color | ESP32-C3-DevKitC-02 | Soil Moisture Sensor | DFPlayer mini | Speaker   |
| ----------- | ------------------- | -------------------- | ------------- | --------- |
| red         | 3V3 (Pin J1-3)      | VCC                  |               |           |
| black       | GND (Pin J1-1)      | GND                  |               |           |
| blue        | GPIO 0 (Pin J3-2)   | SIG                  |               |           |
| red         | 3V3 (Pin J1-2)      |                      | VCC           |           |
| black       | GND (Pin J1-15)     |                      | GND           |           |
| white       | 6 (J1-8)            |                      | RX            |           |
| blue        | 9 (J1-12)           |                      | TX            |           |
| white       |                     |                      | SPK_1         | Speaker + |
| black       |                     |                      | SPK_2         | Speaker - |

Pin layout for [DFPlayer mini](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299):

Pin layout for [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)

## Getting started

For required software and installation, see [Micropython Setup](../../doc/setup-micropython.md)

## Programming

This code uses a library for logging which stems mostly from [micropython-lib](https://github.com/micropython/micropython-lib/tree/master/python-stdlib/logging)  
The code uses the dfplaymini library from [Playing Audio Files](projects/play-audio/README.md)

## Building

Nothing to build

## Flashing

Copy file to controller with

```PS
ampy -p COM11 put .\src\dfplayerminilib.py
ampy -p COM11 put .\src\logging.py
ampy -p COM11 put .\src\main.py
```

## Running

Code runs automatically when controller is reset.
Observe output via serial connection. (PuTTY)

## Helpful links

See other projects for more details.
