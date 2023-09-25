const PORT = 8168

// npm install ws
let WebSocketServer = require('ws').Server;

let wss = new WebSocketServer({
     port: PORT 
    });

wss.on('connection', function (ws) {
    console.log('Client Connected.');
    ws.on('message', function (msg) {
        wss.clients.forEach(function each(client) {
            //console.log(client)
            client.send(msg);
        });
    });
});