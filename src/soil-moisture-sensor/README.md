# Soil Moisture Sensor

## About

This micropython app demonstrates how to read data from a soil moisture sensor.

## Hardware

- [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)
- [Soil Moisture Sensor](https://wiki.seeedstudio.com/Grove-Capacitive_Moisture_Sensor-Corrosion-Resistant/)

## Wiring

| Soil Moisture Sensor | ESP32-C3-DevKitC-02 |
| -------------------- | ------------------- |
| VCC                  | 3V3 (Pin J1-2)      |
| GND                  | GND (Pin J1-15)     |
| SIG                  | GPIO 0 (Pin J3-2)   |

For pins see [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)

## Getting started

For required software and installation, see [Micropython Setup](../../doc/setup-micropython.md)

## Building

Nothing to build

## Flashing

Copy file to controller with

```PS
 ampy -p COM11 -b 115200 put .\main.py
```

# Running
