//npm install socket.io
//npm install python-shell
var connect = require('connect');
var serveStatic = require('serve-static');
var server = connect().use(serveStatic(__dirname)).listen(8080, function(){
    console.log('Server running on 8080...');
});

// Chargement de socket.io
var io = require('socket.io').listen(server);

var PythonShell = require('python-shell');
var lastProjet = '';
var optionsCreatefile = {
    mode: 'text',
    args: ['repoGit']
};
var optionsAnalysefile = {
    mode: 'text',
    args: ['days']
};

// Quand un client se connecte, on le note dans la console
io.sockets.on('connection', function (socket) {
    console.log('Un client est connecté !');
	//http://ourcodeworld.com/articles/read/286/how-to-execute-a-python-script-and-retrieve-output-data-and-errors-in-node-js
	socket.on('message', function (message) {
		var arguments = message.split(';')
		console.log("Execution script python " + arguments[0] + " on " + arguments[1] + " days.")
		optionsCreatefile.args[0] = arguments[0];
		optionsAnalysefile.args[0] = arguments[1];
		console.log(optionsCreatefile.args);
		console.log(optionsAnalysefile.args)
		
		if (lastProjet != arguments[0]) {
			PythonShell.run('Recolte_info_repo_git.py',optionsCreatefile, function (err, results) {
			  if (err) throw err;
			  console.log('results: %j', results);
			  console.log('finished recolte info');
			  console.log('run analyse data');
				PythonShell.run('analyse_data.py', optionsAnalysefile, function (err, results) {
					if (err) throw err;
					console.log('results: %j', results);
					socket.emit('message', 'fileCreated');
					console.log('finished analyse data');
				});

			});
		} else {
			console.log('run analyse data');
			PythonShell.run('analyse_data.py', optionsAnalysefile, function (err, results) {
				if (err) throw err;
				console.log('results: %j', results);
				socket.emit('message', 'fileCreated');
				console.log('finished analyse data');
			});
		}
		
		lastProjet = arguments[0];
		
	});
	
});

server.listen(49160);


