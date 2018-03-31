/*
 * Example using a button to control an LED
 * Copyright (c) 2016 Linaro Ltd.
 * SPDX-License-Identifier: BSD-2-Clause
 */
int led_pin = 3; 
 
void setup()
{
        pinMode(led_pin, OUTPUT);
}


void loop()
{

for (int i =0;i<255;i++){
	analogWrite(led_pin, i);
	delay(1);
	//digitalWrite(led_pin, LOW);
	//delay(500);
}

digitalWrite(led_pin, LOW);
//delay(3000);
exit(1);
}
