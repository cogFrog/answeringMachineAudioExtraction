# answeringMachineAudioExtraction
An attempt to extract and play audio from desoldered W25Q16 taken from an answering machine

## Purpose
My family accidentally erased the messages from their answering machine, including several messages of enormous sentimental value. In many cases, these erase operations simply deallocate space in flash storage rather than actually overwriting it with 1's. As such, I had them immediately power off the device and ship it to me. After identifying a W25Q25 as the likely home of the audio recordings, early tests showed that most pages in the storage chip contained actual data. Thus, I started this project to save the data on my PC and attempt to play it. If this goes well, I can go on to extract the lost messages.

## Hardware

### Bill of Materials:
- Arduino Nano: (https://store.arduino.cc/products/arduino-nano)
- Adafruit TXB0108 breakout board: (https://www.adafruit.com/product/395)
- Adafruit SMT Breakout PCB for SOIC-8: (https://www.adafruit.com/product/1212)
- Breadboard + wire
- W25Q16 chip desoldered from answering machine

### Hardware Photo
COMING SOON

### System Schematic
COMING SOON

## Dependancies
This project utilizes the following libraries:
- W25Q16 Library (https://github.com/derekevans/W25Q16)
- PySerial (https://pypi.org/project/pyserial/)
- PyAudio (https://pypi.org/project/PyAudio/)
