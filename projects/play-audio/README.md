# Soil Moisture Sensor

## About

This micropython app demonstrates how to play audio files.

## Hardware

- [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)
- [DFPlayer mini](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299)
- [Speaker] TODO!

## Wiring

For the following, keep in mind that RX and TX should be crossed. RX on the ESP32 should be connected to TX on the DFPlayer mini and vice versa!
Wiring for RX/TX was difficult to me because I didn't knew, which pins on the ESP32-C3 could or should be used for RX and TX. I found out, that the pins RX (J3-9) and TX (J3-10) were not working for UART1.

First I tried the dfplayer package from Redoxcode.I did some testing and for me the following combinations worked for sending commands but not for reading data from the DFPlayer:

| TX on ESP32 | RX on ESP32 | UART  |
| ----------- | ----------- | ----- |
| 6 (J1-8)    | 9 (J1-12)   | UART1 |
| 10 (J3-7)   | 9 (J1-12)   | UART1 |

I observed, that GPIO 10 as TX works for many cases, even when I used another pin in my code as TX, e.g. `df=DFPlayer(uart,tx_pin_id==6,rx_pin_id=9)` which seems pretty strange to me. Additionally I observed some strange behaviour, which was independent of the wiring: other pins were working in my code, when one pin once was working. For example, when I used GPIO 7, 8, 9 as TX after wiring pin 6 and using pin 6 in my code theses pins worked. Very confusing, but perhaps the reason is, that the UART should have been deinitialized before using another pin. I didn't test this.

Here is the rest of the wiring:

| Cable color    | DFPlayer mini | ESP32-C3-DevKitC-02 | Speaker   |
| -------------- | ------------- | ------------------- | --------- |
| red            | VCC           | 3V3 (Pin J1-2)      |           |
| black          | GND           | GND (Pin J1-15)     |           |
| grey or white  | RX            | see table above     |           |
| purple or blue | TX            | see table above     |           |
| white          | SPK_1         |                     | Speaker + |
| black          | SPK_2         |                     | Speaker - |

For pins see [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html)

## Getting started

For required software and installation, see [Micropython Setup](../../doc/setup-micropython.md)

Additionally, one of the following packages is required:

- [DFPlayer Mini library from Redoxcode](https://pypi.org/project/micropython-dfplayer)

You will need a micro SD card with a FAT16 or FAT32 file system. There are different descriptions about the naming conventions for the audio files. I used the following structure:

```PS
/root
    /01
        001.mp3
        002.mp3
        003.mp3
    /02
        001.mp3
        002.mp3
        003.mp3
    /03
        001.mp3
        002.mp3
        003.mp3
```

## Building

Nothing to build

## Flashing

Copy files and folders to controller with

```PS
ampy -p COM11 put .\src\dfplayer
```

## Running

Run the app with

```PS
ampy -p COM11 -b 115200 run .\src\dfplay-demo1.py
```

## Helpfull links

- [Extended explanation for DFPlayer mini (German)](https://www.elektronik-kompendium.de/sites/praxis/bauteil_dfplayer-mini.htm)
