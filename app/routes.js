var PythonShell = require('python-shell'),
    request = require("request");
module.exports = function(app){
    app.post("/start",function(req,res){
        console.log("entered");
	console.log(req.body);
        var options = {
            args:[
                req.body.ip,
                req.body.prt,
                req.body.ttl
            ]
        }
        var pyshell = new PythonShell('./IPSpoofTest.py',options);
	pyshell.on('message',function(message){
		console.log(message);
	})
        pyshell.on('close',function(message){
            console.log("done");
            res.json({});
        })
    })
}
