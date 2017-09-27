var b = require('bonescript');

var led0 = "USR0";
var led1 = "USR1";
var state = b.LOW;

b.pinMode(led0, 'out');
b.pinMode(led1, 'out');

toggleLED = function() {
 state = state ? b.LOW  : b.HIGH ;
 console.log('Cambia estado:%s', state);
 b.digitalWrite(led0, state);
 b.digitalWrite(led1, ! state);
};

timer = setInterval(toggleLED, 200);

stopTimer = function() {
 clearInterval(timer);
};

setTimeout(stopTimer, 10000);
