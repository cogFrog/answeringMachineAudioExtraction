/*This sketch shows the basics of using the W25Q16 library.*/

/*W25Q16 Connections:
 pin 1 to Arduino pin 10 or Atmega328 pin 15 (Chip Select)
 pin 2 to Arduino pin 12 or Atmega328 pin 18 (Master In Slave Out)
 pin 3 to 3.3V (Vdd)
 pin 4 to GND (Vss)
 pin 5 to Arduino pin 11 or Atmega328 pin 17 (Slave in Master Out)
 pin 6 to Arduino pin 13 or Atmega328 pin 19 (Clock)
 pin 7 to 3.3V (Vdd)
 pin 8 to 3.3V (Vdd)
 */
 
#include <SPI.h>
#include <W25Q16.h>

#define NUMPAGES 8192 // number of pages in flash chip

W25Q16 flash;
int page;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  
  // initialize flash chip
  flash.init(10); 
}

void loop() {
  // wait for instruction (page from W25Q16 to dump into serial)
  while (!Serial.available());
  page = Serial.readString().toInt();

  // check that page exists
  if (page >= NUMPAGES || page < 0) {
    Serial.println("Error: Given page number out of range");
    return;
  }

  // dump page into serial
  for (int i = 0; i < 256; i++) {
    printByte(flash.read(page, (uint8_t)i));
  }
  Serial.println();
  
} 

// prints byte, ensuring two digits are used (ie: 12 --> '0C' rather than 'C')
void printByte(int x) {
  if (x < 16) {
    Serial.print('0');
  }
  Serial.print(x, HEX);
}
