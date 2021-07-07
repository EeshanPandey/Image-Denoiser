var express = require('express'); 
var bodyParser = require('body-parser'); 
var request = require('request-promise'); 
const multer = require('multer');
const upload = multer({dest: __dirname + '/public/images'});
var app = express(); 
app.set("view engine", "ejs");
app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: false })); 
app.use(express.static('public'));
 

app.get('/', function(req,res){
    res.render('index.ejs')
})


app.post('/postdatatoflask', upload.single('photo'), (req, res) => {
    if(req.file) {
        //res.json(req.file);
        img = req.file.originalname;
        var name = req.body.name;
        console.log(name)
        console.log(img)
        res.redirect('/postdatatoflask');
    }
    else throw 'error';
});

app.get('/postdatatoFlask', async function (req, res) { 
    var data = { // this variable contains the data you want to send 
        data1: "hello", 
        data3: 133
    } 
 
    var options = { 
        method: 'POST', 
        uri: 'http://localhost:5000/postdata', 
        body: data, 
        json: true // Automatically stringifies the body to JSON 
    }; 
     
    var returndata; 
    var sendrequest = await request(options) 
    .then(function (parsedBody) { 
        console.log(parsedBody); // parsedBody contains the data sent back from the Flask server 
        returndata = parsedBody; // do something with this data, here I'm assigning it to a variable. 

    }) 
    .catch(function (err) { 
        console.log(err); 
    }); 
    
    res.render("show.ejs", {returndata: returndata});
 

    //res.send(returndata); 
}); 
  
if (app.listen(3000)){
    console.log("Started on 3000");
}; 