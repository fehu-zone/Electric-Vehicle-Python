
//Hall Effect - Start
int hallsensor = 2;                
volatile byte counter;
unsigned int r=56;
float pi=3.1415926536;
unsigned long passedtime;
//Hall Effect - End
//LM35 - Start
const int analogPin = A1;
float sensorDeger = 0.0;
float sicaklikDeger = 0.0;
//LM35 - End
//Hall Effect - Start
void updateCounter(){counter++;}
//Hall Effect - End
void setup(){
  Serial.begin(9600);
  //LM35 - Start
  pinMode(analogPin, INPUT);
  //LM35 - End
  //Hall Effect - Start
  attachInterrupt(digitalPinToInterrupt(hallsensor), updateCounter, RISING);
  //Hall Effect - End 
  //Response - Start
  counter = 0;
  passedtime = 0;
  /*String response= "";
  response += "Devir";
  response += ",";
  response += "RPM";
  response += ",";
  response += "HIZ";
  response += ",";
  response += "SICAKLIK";
  response += ";";
  Serial.println(response);*/
  //Response - End
 }
 void loop()
 {
  delay(500);
  
  //Hall Effect - Start
  detachInterrupt(digitalPinToInterrupt(hallsensor)); 
  float rpm=0,speeds=0,counters=0;
   rpm = ((60000.0)/(millis() - passedtime))*(counter/6.0);
  
  speeds=rpm*r*0.001885;
  
  counters=counter;
  counter = 0;
  passedtime = millis();
  //Hall Effect - End
  //LM35 - Start
  sensorDeger = analogRead(analogPin);
  sicaklikDeger = ((sensorDeger/1023.0)*5000.0) / 10.0;
  //LM35 - End
  //Response - Start
  String response= "";
  response.concat(counters);
  response += ",";
  response.concat(rpm);
  response += ",";
  response.concat(speeds);
  response += ",";
  response.concat(sicaklikDeger);
  response += ";";
  Serial.println(response);
  //Response - End
  //Hall Effect - Start
  attachInterrupt(digitalPinToInterrupt(hallsensor), updateCounter, RISING);
  //Hall Effect - End
 }
