const personal = document.querySelector('#btnPersonal');
const shared = document.querySelector('#btnShared');
const carpetaIcon = document.querySelector('#crearCarpeta');
const documentoIcon = document.querySelector('#crearArchivo');
const notificacionIcon = document.querySelector('#notification');
const perfilIcon = document.querySelector('#perfil');

personal.addEventListener("click",showPersonal);
shared.addEventListener("click",showShared);
carpetaIcon.addEventListener("click", crearCarpeta);
documentoIcon.addEventListener("click", crearArchivo);
notificacionIcon.addEventListener("click", notificaciones);
perfilIcon.addEventListener("click", perfil);

var loc = window.location
var wsStart = 'ws://'; 
if (loc.protocol == 'https:') {
    wsStart = 'wss://';
}

var endpoint = wsStart + loc.host + loc.pathname;
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


function showShared() {
	document.querySelector('#myFiles').style.display = "none";
	document.querySelector('#sharedFiles').style.display = "block";
	personal.style.background = "#2d3436";
	shared.style.background = "#1e272e";

}
function showPersonal() {
	document.querySelector('#myFiles').style.display = "block";
	document.querySelector('#sharedFiles').style.display = "none";
	shared.style.background = "#2d3436";
	personal.style.background = "#1e272e";
}


function crearCarpeta(){
    alert("Crear carpeta");
}

function crearArchivo(){
    alert("Crear archivo");
}

function notificaciones(){
    alert("Notificaciones");
}

function perfil(){
    alert("Perfil");
}