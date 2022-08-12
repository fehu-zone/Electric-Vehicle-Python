
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN   8
#define CSN_PIN 7



const uint64_t pipe = 0xE8E8F0F0E1LL;

RF24 radio(CE_PIN, CSN_PIN);

String  data;
void setup()
{
  Serial.begin(9600);
  delay(1000);
  radio.begin();
  radio.openWritingPipe(pipe);
  radio.setDataRate(RF24_250KBPS);
  radio.setPALevel(RF24_PA_MAX);
  radio.stopListening();
}


void loop()
{

  if(Serial.available()){
    data=Serial.readStringUntil('\n')+"0";
    int str_len = data.length();
    char char_data[str_len];
    data.toCharArray(char_data, str_len);
    radio.write( &char_data, sizeof(char_data) );

  }

}