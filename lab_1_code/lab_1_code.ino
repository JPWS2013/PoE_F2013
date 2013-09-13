

void setup() {                
  // initialize the digital pin as an output.
  pinMode(A5, INPUT);    
  Serial.begin(9600); 
}

// the loop routine runs over and over again forever:
void loop() {
  int reading = analogRead(A5);
  Serial.println(reading);
  delay(1000); 
}

