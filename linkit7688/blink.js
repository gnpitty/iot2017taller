var m = require('mraa');
var ledState = true;
var myLed = new m.Gpio(44); // GPIO44 is the Wi-Fi LED
myLed.dir(m.DIR_OUT);


function periodicActivity() {
myLed.write(ledState ? 1 : 0);
ledState = !ledState;
setTimeout(periodicActivity, 60);
}


periodicActivity();

