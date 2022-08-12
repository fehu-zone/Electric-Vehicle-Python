#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN   8
#define CSN_PIN 7


const uint64_t pipe = 0xE8E8F0F0E1LL;


RF24 radio(CE_PIN, CSN_PIN);


void setup()
{
  Serial.begin(9600);
  delay(500);
  radio.begin();
  radio.openReadingPipe(1, pipe);
  radio.setDataRate(RF24_250KBPS);
  radio.setPALevel(RF24_PA_MAX);
  radio.startListening();
}


void loop()
{

  if ( radio.available() )
  {
    char data[100];
    radio.read( &data, sizeof(data) );
    Serial.println(data);
  }


}