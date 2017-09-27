var express = require('express');
var app = express();
var url = require("url");
var b = require('bonescript');
var idx = '/root/pruebaJS/public/index3.html';
var contador = 1
app.use(express.static('public'));


var fs = require('fs'); // this engine requires the fs module
var conta = 1


app.engine('ntl', function (filePath, options, callback) { // define the template engine
  fs.readFile(filePath, function (err, content) {
    if (err) return callback(new Error(err));
    // this is an extremely simple template engine
    var rendered = content.toString().replace('#title#', ''+ options.title +'')
    .replace('#message#', ''+ options.message +'');
    return callback(null, rendered);
  });
});
app.set('views', './views'); // specify the views directory
app.set('view engine', 'ntl'); // register the template engine


b.pinMode('USR0', b.OUTPUT);
b.pinMode('USR1', b.OUTPUT);
b.pinMode('USR2', b.OUTPUT);
b.pinMode('USR3', b.OUTPUT);

var status_actual  = "off" 


app.get('/index', function (req, res) {
  contador++;
  res.sendFile(idx);
});

app.get('/proc', function (req, res) {
        contador++;
	var params = url.parse(req.url,true).query;
	console.log(params);
	var status = params.status 
        console.log('status:%s', status);
if(status != undefined &&  (status =='ON'  || status =='OFF' ) ) {
            status_actual = status.toLowerCase();
            console.log('status_actual:%s', status_actual);
            status = status.toLowerCase();

       } 

  if(status != undefined && status == 'TOG' && status_actual =='on'  ) { 
    status = 'off'
    status_actual ='off'
   }
  if(status != undefined && status == 'TOG' && status_actual =='off' ) { 
      status = 'on' 
      status_actual ='on'
   }


  console.log('status2:%s  status_actual:%s', status,status_actual);
    	if(status =='on' ) {
	b.digitalWrite('USR0', b.HIGH);
	b.digitalWrite('USR1', b.HIGH);
	b.digitalWrite('USR2', b.HIGH);
	b.digitalWrite('USR3', b.HIGH);
    	}


if(status =='off' ) {
	b.digitalWrite('USR0', b.LOW);
	b.digitalWrite('USR1', b.LOW);
	b.digitalWrite('USR2', b.LOW);
	b.digitalWrite('USR3', b.LOW);
    	}
  res.render('index', { title: 'BeagleBone Black', message: status});
 // res.status(200).sendFile(idx);
});

var server = app.listen(5000, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('Example app listening at http://%s:%s', host, port);

});
