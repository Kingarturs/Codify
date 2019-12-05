function socketDocumento(doc){
    var loc = window.location
    var wsStart = 'ws://'; 
    if (loc.protocol == 'https:') {
        wsStart = 'wss://';
    }

    var endpoint = wsStart + loc.host + loc.pathname + doc;
    var socket = new WebSocket(endpoint);

    socket.onmessage = function(e){
        console.log("message", e);
    }
    socket.onopen = function(e){
        console.log("open", e);
    }
    socket.onerror = function(e){
        console.log("error", e);
    }
    socket.onclose = function(e){
        console.log("close", e);
    }
}

