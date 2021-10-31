#include <Wire.h>
#include <RTC.h>

DS3231 rtc;					// the DS3231 RTC
const int buzzer = 9;		// Buzzer Pin or Relay Pin
const int pushButton = 7;	// The push button to manually ring the bell
int pushButtonVal = LOW;

int currentHours = 0;		// Stores the current hour
int currentMinutes = 0;		// Stores the current minute

//char daysOfTheWeek[7] = {"Sunday", "Monday", "Tuesday", "Wednesday", 
//						"Thursday", "Friday", "Saturday"};

// The Array of bell ringing Hours
const int bellTimingsHours[6] = {6, 7, 8, 9, 10, 11};

// The Array of bell ringing Minutes
const int bellTimingsMinutes[4] = {15, 40, 45, 55};

// Constant length for assurance of correct mapping
const int bellTimingsLen = 12;

// Array of bell ring types => (continued long or n times)
const int bellTypes[bellTimingsLen] = {
	// 0 = long bell
	0, 1, 2, 3, 4, 0, 0, 5, 6, 7, 8, 0
	// depart for assembly, 1, 2, 3, 4 bells
	// lunch begin bell, lunch end bell (and the 5th period bell)
	// 6, 7, 8 bells, then finally, Final Bell!!!
};

// Array of the duration of bell rings in millis
const int bellLongDurations[bellTimingsLen] = {
	3000, 1000, 1000, 1000, 1000, 4000, 4000, 1000, 1000, 1000, 1000, 5000
};

/*
// Old Stuff, don't notice
typedef struct hourMinute {
	int hour;
	int minute;
} hourMinute_t;

hourMinute_t bellTimings[] = {
	{6, 55}, {7, 15}, {7, 45}, {8, 15}, {8, 45}, 
	{9, 15}, {9, 45}, {10, 15}, {10, 45},
	{11, 15}, {11, 45}
};
*/

// 2-dimensional array of the bell timings, in the form of {hour, minute}
// Note that every hour and minute present here is in the array of (bellTimingsHours) and (bellTimingsMinutes), respectively
// Also the length of this array and the arrays of durations and types is same (bellTimingsLen)
// This is done ensure that the mapping between the arrays is correct
const int bellTimings[bellTimingsLen][2] = {
	{6, 55}, {7, 15}, {7, 45}, {8, 15}, {8, 45}, 
	{9, 15}, {9, 40}, {9, 45}, {10, 15}, {10, 45},
	{11, 15}, {11, 45},
};

// This block will run only one time or every time reset button is pressed, when the arduino is powered
void setup() {
	Serial.begin(9600);
	
	if (!rtc.begin()) {
		Serial.println("Couldn't Find RTC");
		while(1);
		
	} else {
		// Set the date and time when the sketch was compiled
		// For the first time only, comment afterwards
		rtc.setDateTime(__DATE__, __TIME__);
		
		// Or setting it absolutely
		// rtc.setDate(2021, 9, 23);
		// rtc.setTime(4, 31, 30);

		Serial.println("Date Time set!");
	}
	
	if (!rtc.isRunning()) {
		Serial.println("RTC Not Running!");
	}

	pinMode(buzzer, OUTPUT);	// Set the buzzer pin to OUTPUT
	pinMode(pushButton, INPUT);	// Set the pushButton pin to INPUT
}

// This block will run until you die or the power goes off...
void loop() {

	pushButtonVal = digitalRead(pushButton);	// Read the pushButton value as either pressed or not pressed

	if (pushButtonVal == HIGH) {
		Serial.println("Push button pressed!");
		if (digitalRead(buzzer) == LOW)
			digitalWrite(buzzer, HIGH);		// If pushButton is pressed and the buzzer is off, turn on the buzzer
	} else {

		if (digitalRead(buzzer) == HIGH)
			digitalWrite(buzzer, LOW);		// If pushButton is not pressed and buzzer is on, turn off the buzzer
	}
	
	// DateTime now = DateTime(rtc.getYear(), rtc.getMonth(), rtc.getDay(), rtc.getHours(), rtc.getMinutes(), rtc.getSeconds());
	// Serial.println(now);

	if (rtc.getWeek() == 1) {	// 1 is sunday, varies from 1 (sunday) to 7 (saturday)
		return;					// Do nothing
	}
	
	currentHours = rtc.getHours();
	currentMinutes = rtc.getMinutes();

	// Info the time to the serial monitor
	Serial.print("Time is ");
	Serial.print(currentHours);
	Serial.print(":");
	Serial.print(currentMinutes);
	Serial.println();
	
	// This means that if (currentHour) is in the array of (bellTimingsHours), i.e. index != -1
	// if index == -1, then the element is not in the array
	if (indexOfInt(bellTimingsHours, 6, currentHours) != -1) {		       // 6 is the length of the bellTimingsHours array
		if (indexOfInt(bellTimingsMinutes, 4, currentMinutes) != -1) {	// 4 is the length of the bellTimingsMinutes array
			// It is bell time !!!
			ringBell();
		}
	}

	delay(5000);	// Wait for 5 seconds before checking again
}

// Used for finding the index of an int element in an const array
int indexOfInt(const int ar[], int len, int elem) {
	for (int i = 0; i < len; ++i)
	{
		if (elem == ar[i]) {
			return i;
		}
	}

	return -1;
}

// Used for finding the index of an array in another 2-dimensional const array with the length of inner array = 2
int indexOfArray(const int ar[][2], int len, int elem[]) {
	for (int i = 0; i < len; ++i)
	{
		if ((elem[0] == ar[i][0]) & (elem[1] = ar[i][1])) {
			return i;
		}
	}

	return -1;
}

// Ring the bell (n) number of times each for (duration) millis with a (pause) millis interval
void ringBell_ntimes(int n = 3, int duration = 1000, int pause = 500) {
	//repeat(n)
		// Start Bell for duration
		// Stop bell for pause

  for (int i = 0; i < n; ++i)
  {
	digitalWrite(buzzer, HIGH);
	delay(duration); // Wait duration millis
	digitalWrite(buzzer, LOW);
	delay(pause); // Wait pause millis
  }
}

// Ring the bell continuously for (duration) millis
void ringBell_long(int duration = 5000) {
	// Start Bell for duration
	// Stop bell

	digitalWrite(buzzer, HIGH);
	delay(duration);
	digitalWrite(buzzer, LOW);
}

// Processes the (currentHour) and (currentMinute) to find the type and duration of the bell to be rang
// Also calls the correct function with the required parameters
void ringBell() {
	int hmArray[2] = {currentHours, currentMinutes};	// Construct an array of (currentHour) and (currentMinute)
	int index = indexOfArray(bellTimings, bellTimingsLen, hmArray);		// get the index of the constructed array in the (bellTimings) array
	int typeOfBell = bellTypes[index];					// get the type of the bell using that index
	int duration = bellLongDurations[index];			// get the duration of the bell using that index

	// Call the correct ringing function with the reuqired params based on the type of bell
	if (typeOfBell == 0) {
		ringBell_long(duration);
	} else {
		ringBell_ntimes(typeOfBell, duration);
	}
}

/* Code by Harsh Narayan Jha and team */
/* Last Updated: 31-10-2021 at 07:18 pm */
