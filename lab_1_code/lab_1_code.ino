#include <Servo.h>

int incoming_message=0;
int counter=0;
int horizontal_angle_track=170;
int vertical_angle_track=0;
int horizontal_increment=5;
int vertical_increment=3;

Servo horizontal_servo;
Servo vertical_servo;

void setup() {                
  // initialize the digital pin as an output.
  pinMode(A5, INPUT);    
  Serial.begin(9600); 
  horizontal_servo.attach(7);
  vertical_servo.attach(8);
  //myservo.write(90);
}

// the loop routine runs over and over again forever:
void loop() {
  
  //Sends data only when it is received
  if (Serial.available()>0){
    
    incoming_message=Serial.read();
    
    if (incoming_message=='1'){ //Moves to the right
      //Serial.print("I'm about to wait");
      //delay(1000);
      horizontal_angle_track=horizontal_angle_track-horizontal_increment;
      horizontal_servo.write(horizontal_angle_track);
      //Serial.print ("I just moved the IR Sensor 1 unit to the right\r\n");
    }
    
    if (incoming_message=='2'){ //Moves to the left
      horizontal_angle_track=horizontal_angle_track+horizontal_increment;
      horizontal_servo.write(horizontal_angle_track);
      //Serial.print ("I just moved the IR Sensor 1 unit up\r\n");
    }
    
    if (incoming_message=='3'){ //Moves the servo up
      vertical_angle_track=vertical_angle_track+vertical_increment;
      vertical_servo.write(vertical_angle_track);
      //Serial.print ("I just moved the IR Sensor 1 unit to the left\r\n");
    }
    
    if (incoming_message=='4'){ //Moves the servo down
      vertical_angle_track=vertical_angle_track-vertical_increment;
      vertical_servo.write(vertical_angle_track);
      //Serial.print ("I just moved the IR Sensor 1 unit down\r\n");
    }

    if (incoming_message=='5'){ //Moves sensor all the way left
      //delay(500);
      horizontal_angle_track=170;
      horizontal_servo.write(horizontal_angle_track);
      //Serial.print ("I just moved the IR Sensor all the way to the left\r\n");
    }

    if (incoming_message=='6'){ //Moves sensor to the lowest possible vertical angle setting
      vertical_angle_track=0;
      vertical_servo.write(vertical_angle_track);
      //delay(1000); 
    }

    if (incoming_message=='7'){
      delay(500);
      int reading = analogRead(A5);
      Serial.println(reading);
      //delay(1000); 
    }
    
    if (incoming_message=='8'){
      delay(500);
      int reading = analogRead(A5);
      Serial.println(reading);
      //delay(1000); 
    }
}
}
