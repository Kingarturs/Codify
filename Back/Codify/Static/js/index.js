const personal = document.querySelector('#btnPersonal');
const shared = document.querySelector('#btnShared');
const carpetaIcon = document.querySelector('#crearCarpeta');
const documentoIcon = document.querySelector('#crearArchivo');
const notificacionIcon = document.querySelector('#notification');
const perfilIcon = document.querySelector('#perfil');
const runIcon = document.querySelector('#correr');
const downIcon = document.querySelector('#descargar');
const editorIcon = document.querySelector('#editor');
const compartirIcon = document.querySelector('#compartirIcon');
const eliminarIcon = document.querySelector('#borrar');

personal.addEventListener("click",showPersonal);
shared.addEventListener("click",showShared);
carpetaIcon.addEventListener("click", crearCarpeta);
documentoIcon.addEventListener("click", crearArchivo);
notificacionIcon.addEventListener("click", notificaciones);
perfilIcon.addEventListener("click", perfil);
runIcon.addEventListener("click", enviar);
downIcon.addEventListener("click", descargar);
editorIcon.addEventListener("keyup", actualizar);
compartirIcon.addEventListener("click", ver_compartir);
eliminarIcon.addEventListener("click", eliminacion);

//Nuevo Editor
var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");
$(function() {
    var editor;
    $('.ace_editor').each(function( index ) {
      editor = ace.edit(this);
      editor.setFontSize("14px");
    });
 })

var loc = window.location
var wsStart = 'ws://'; 
if (loc.protocol == 'https:') {
    wsStart = 'wss://';
}

var endpoint = wsStart + loc.host + loc.pathname;
console.log(endpoint)
var socket = new WebSocket(endpoint);

socket.onmessage = function(e){
    var pos = editor.session.selection.toJSON()
    editor.session.setValue("" + editor.session.getValue())
    editor.setValue(e.data);
    editor.session.selection.fromJSON(pos)
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
    document.getElementById("makeCarpeta").style.display = "block";
    $("#makeCarpeta").animate({top:"30%",height: "160px", width: "30%"},250);
}

function crearArchivo(){
    base = document.getElementById("myFiles").children[0].children
    document.getElementById("raiz").innerHTML = "";
    temp = document.createElement("option");
    temp.getAttribute("value", "");
    temp.appendChild(document.createTextNode(""));
    document.getElementById("raiz").appendChild(temp);
    for(var i =0;i<base.length;i++){
        if(base[i].id!=""){
            temp = document.createElement("option");
            temp.getAttribute("value", base[i].id.slice(0,-2));
            temp.appendChild(document.createTextNode(base[i].id.slice(0,-2)));
            document.getElementById("raiz").appendChild(temp);
        }
    }
    document.getElementById("makeArchivo").style.display = "block";
    $("#makeArchivo").animate({top:"30%",height: "300px", width: "30%"},250);
}

function notificaciones(){
    document.getElementById("solicitudes").style.display = "block";
    document.getElementById("solicitudes").children[0].style.display = "block";
    $("#solicitudes").animate({top:"15%",height: "400px", width: "30%"},250);
}

function perfil(){
    Swal.fire({
        title: 'Are you sure?',
        text: "We will miss you 😥!",
        icon: 'warning',
        target: 'body',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, Log Out!',
        allowEscapeKey: true,
      }).then((result) => {
        if (result.value) {
          window.location = "logout";
        }
    })
}

function actualizar(){
    
    tipoMensaje = "1";
    contenido = editor.getValue();
    dict = {
        contenido: contenido,
        nombre: estado,
        dir: dir_estado,
        tipo: tipoMensaje, 
    }
    socket.send(
        JSON.stringify(dict)
        );
    }
    
    function makeArchivo(){
        nombre = $("#makeArchivo").children()[0].value;
    directorio = $("#makeArchivo").children()[1].value;
    tipo = $("#makeArchivo").children()[2].value; 
    $.ajax({
        type:'POST',
        url:'archivo',
        data:{
            nombre: nombre,
            directorio:directorio,
            tipo:tipo
        },
        success:function(data){
            cargar(data);
        },
    });
}
function makeCarpeta(){
    nombre = $("#makeCarpeta").children()[0].value;
    $.ajax({
        type:'POST',
        url:'carpeta',
        data:{
            nombre: nombre
        },
        success:function(data){
            if (typeof(data)=="string"){
                alert("Ya existe esa carpeta");
            }
            else{
                cargar(data);
            }
        },
    });
}
function minMax(a){
    var div = document.getElementById(a);
    for(var i = 0;i < div.children.length;i++){
        if(div.children[i].style.display == "none"){
            div.children[i].style.display = "block";
        }
        else{
            div.children[i].style.display = "none";
        }
    }
}
function cargar(data){
    base = document.getElementById("myFiles")
    base.innerHTML = "";
    div = document.createElement("div");
    div.setAttribute("class", "accordionFiles");
    base.appendChild(div);
    for(key in data){
        if(key != ""){
            
            console.log(data)
            temp = document.createElement("li");
            temp.setAttribute("class","acc-item");
            temp.id = key+"--";
            // temp.setAttribute("onclick", "minMax('"+key+"--')");
            temp2 = document.createElement("div");
            temp2.setAttribute("class", "labels")

            a = document.createElement("a");
            a.appendChild(document.createTextNode(key))
            a.setAttribute("class", "btn");
            a.setAttribute("href", "#" + key + "--");
            temp2.appendChild(a);
            img = document.createElement("img");
            img.setAttribute("src", "../static/img/dots.svg")
            img.setAttribute("class", "svg")
            temp2.appendChild(img);
            temp.appendChild(temp2)

            for(x in data[key]){
                hijo = document.createElement("div");
                hijo.setAttribute("class","submenu");
                hijo.setAttribute("onclick","codigo('"+data[key][x]+"','"+key+"')");
                hijo.appendChild(document.createTextNode(data[key][x]));
                temp.appendChild(hijo);
            }
            div.appendChild(temp);
        }
        else{
            for(x in data[key]){
                temp = document.createElement("div");
                temp.setAttribute("class","submenu2");
                temp.setAttribute("style","display:block");
                temp.appendChild(document.createTextNode(data[key][x]));
                temp.setAttribute("onclick","codigo('"+data[key][x]+"','')");
                div.appendChild(temp);
            }
        }
    }
}

var estado = "";
var dir_estado = "";
var iddd = "";
function codigo(name,dir,id){

    if(name.slice(name.length-2, name.length) == "js"){
        editor.session.setMode("ace/mode/javascript");
    }else{
        editor.session.setMode("ace/mode/python");
    }

    estado = name;
    dir_estado = dir;
    tipoMensaje = "2";
    iddd = id
    $.ajax({
        type:'POST',
        url:'getCodigo',
        data:{
            nombre: name,
            dir:dir,
            codigo: editor.getValue(),
            usuario:id
        },
        success:function(data){
            editor.setValue(data);
            editor.navigateLineEnd();
            editor.focus();
        },
    });
    
    dict = {
        nombre: estado,
        dir: dir_estado,
        tipo: tipoMensaje, 
        usuario:id,
    }
    socket.send(
        JSON.stringify(dict)
        );
        
    }
    
    function enviar(){
        var contenido = editor.getValue();
    $.ajax({
        type:'POST',
        url:'codigo',
        data:{
            codigo: contenido,
            nombre:estado,
            dir:dir_estado,
            lenguaje: estado.slice(estado.length-2, estado.length),
            id: iddd
        },
        success:function(data){
            document.getElementById("consola").textContent = data
        },
    });
}

function descargar(){
    if(dir_estado == ""){
        dirs_estado = "a57f389a2d5e57b02b3f2225814ae13e"
    }
    else{
        dirs_estado = dir_estado
    }
    window.open("descargar/"+estado+"/"+dirs_estado)
    // $.ajax({
        //     type:'POST',
        //     url:'descargar',
        //     data:{
            //         estado:estado,
            //         dir:dir_estado
            //     },
            //     success:function(data){
                //         window.open(data);
                //     },
    // });
}
function ver_compartir(){
    document.getElementById("compartir").style.display = "block";
    $("#compartir").animate({top:"30%",height: "300px", width: "30%"},250);

}

function verificar(){
    $.ajax({
            type:'POST',
            url:'verificar',
        data:{
                nombre:estado,
                dir:dir_estado,
                invitado:$("#compartir").children()[0].value
            },
            success:function(data){
                document.getElementById("verificador").innerHTML = data
                if(data == "existe"){
                    $("#compartir").children()[2].disabled = false;
                }
                else{
                    $("#compartir").children()[2].disabled = true;
                }
                },
            });
}
$("#compartir").children()[2].disabled = true;
function compartir(){
    console.log("compartido");
    $.ajax({
        type:'POST',
        url:'compartir',
        data:{
            nombre:estado,
            dir:dir_estado,
            invitado:$("#compartir").children()[0].value
        },
        success:function(data){

        },
    });
        $("#compartir").children()[2].disabled = true;
        $("#compartir").children()[1].innerHTML = "";
}

function a_soli(ruta,dueno,invitado,id){
    console.log("aceptacion");   
    $.ajax({
        type:'POST',
        url:'aceptacion',
        data:{
            ruta:ruta,
            dueno:dueno,
            invitado:invitado,
            id:id
        },
        success:function(data){

        },
    });
}
function r_soli(id){
    console.log("rechazacion");
    $.ajax({
        type:'POST',
        url:'rechazacion',
        data:{
            id:id,
        },
        success:function(data){

        },
    });
}
function eliminacion(){
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.value) {
            $.ajax({
                type:'POST',
                url:'eliminacion',
                data:{
                    nombre:estado,
                    dir:dir_estado,
                    id:iddd
                },
                success:function(data){
                  location.reload()  
                },
            });



          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
          )
        }
      })
}
//-------- EDITOR ----------------------------------------------------------------------------------------------

// var keywords = [
//     "ASSERT",
//     "AND",
//     "BREAK",
//     "CASE",
//     "CLASS",
//     "CATCH",
//     "CONST",
//     "CONTINUE",
//     "CONSOLE",
//     "DEBUGGER",
//     "DEF",
//     "DEL",
//     "DEFAULT",
//     "DELETE",
//     "DO",
//     "ELIF",
//     "ELSE",
//     "EXPORT",
//     "EXTENDS",
//     "EXEC",
//     "EXCEPT",
//     "FINALLY",
//     "FOR",
//     "FROM",
//     "FUNCTION",
//     "GLOBAL",
//     "IF",
//     "IMPORT",
//     "IN",
//     "INSTANCEOF",
//     "INPUT",
//     "IS",
//     "LAMBDA",
//     "LET",
//     "LOG",
//     "NEW",
//     "NOT",
//     "OR",
//     "PRINT",
//     "RAISE",
//     "RANGE",
//     "RETURN",
//     "SUPER",
//     "SWITCH",
//     "THIS",
//     "THROW",
//     "TRY",
//     "TYPEOF",
//     "VAR",
//     "VOID",
//     "WHILE",
//     "WITH",
//     "YIELD"
//     ];
//     // Keyup event
//     var posicion = 0;
//     var elemento = 0;
//     var simbolo = false;
//     var linea = 0;
    
//     $("#editor").on("keyup", function(e){
//         getLinea();
//         getPuntero();
//         // console.log(linea);
//         if((e.keyCode>47 && e.keyCode<58) || (e.keyCode>64 && e.keyCode<91)){
//             if(this.children.length == 0){
//                 this.textContent = "";
//                 div = document.createElement("div");
//                 div.dataset.linea = 0;
//                 span = document.createElement("span");
//                 span.appendChild(document.createTextNode(e.key));
//                 span.dataset.id = 0;
//                 div.appendChild(span);
//                 this.appendChild(div);
//                 setPuntero(this,0);
//             }
//             procesamiento(this);
//             if(simbolo){
//                 nuevoSpan(this,e.key);
//                 simbolo = false;
//             }
//             // console.log(this.children[linea].children[elemento]);
//             var encontrado = false
//             caracteres = ["",".","("," ",":"];
//             for(var j = 0;j<caracteres.length;j++){
    
//                 for(var i = 0;i<keywords.length;i++){
//                     if(this.children[linea].children[elemento].textContent.toUpperCase() == keywords[i]+caracteres[j]){
//                         this.children[linea].children[elemento].style.color = "#ff3f34";
//                         encontrado = true
//                     }
//                 }
//             }
//                     if(!encontrado){
//                         this.children[linea].children[elemento].style.color = "white";
//                     }
//         }
//         else if(e.keyCode==13){ // Enter
//             ordenar_divs(this);
//             elemento = 0;
//         }
//         else if(e.keyCode==8){ //borrar
//             ordenar_divs(this);
//             if(!encontrado){
//                 this.children[linea].children[elemento].style.color = "white";
//             }
//         }
//         else if (e.keyCode == 32){ // espacio
//             nuevoSpan(this, "\u00a0");
//             simbolo = true;
//         }
    
//         if(e.key == '('){ // ( es el mismo que el 8
//             // noSpan(this,e);
//             // nuevoSpan(this, "(");
//             simbolo = true;
//         }
//         else if(e.key == ")"){// ) es el mismo que el 9
//             noSpan(this,e);
//             // nuevoSpan(this, ")");
//             simbolo = true;
//         }
//         else if(e.key == "."){ //punto es el mismo que :
//             noSpan(this,e);
//             nuevoSpan(this, ".");
//             simbolo = true;
//         }    
//         else if(e.key == ","){//coma el mismo que ;
//             noSpan(this,e);
//             nuevoSpan(this, ",");
//             simbolo = true;
//         }
//         else if(e.key == '"'){//comillas dobles es el mismo que el 2 (bug :'v)
//             // noSpan(this,e);
//             // nuevoSpan(this,'"');
//             // simbolo = true;
//         }
//         else if(e.key == "$"){// $ es el mismo que el 3
//             noSpan(this,e);
//             nuevoSpan(this, "$");
//             simbolo = true;
//         }
//         else if(e.key == "#"){// # es el mismo que el 3
//             noSpan(this,e);
//             nuevoSpan(this, "#");
//             simbolo = true;
//         }
//         else if(e.key == ":"){// : es el mismo que el .
//             noSpan(this,e);
//             nuevoSpan(this, ":");
//             simbolo = true;
//         }
//         else if(e.key == ";"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, ";");
//             simbolo = true;
//         }
//         else if(e.key == "{"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "{");
//             simbolo = true;
//         }
//         else if(e.key == "}"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "}");
//             simbolo = true;
//         }
//         else if(e.key == "["){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "[");
//             simbolo = true;
//         }
//         else if(e.key == "]"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "]");
//             simbolo = true;
//         }
//         else if(e.key == "="){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "=");
//             simbolo = true;
//         }
//         else if(e.key == "!"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "!");
//             simbolo = true;
//         }
//         else if(e.key == "+"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "+");
//             simbolo = true;
//         }
//         else if(e.key == "-"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "-");
//             simbolo = true;
//         }
//         else if(e.key == "*"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "*");
//             simbolo = true;
//         }
//         else if(e.key == "|"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "|");
//             simbolo = true;
//         }
//         else if(e.key == "&"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "&");
//             simbolo = true;
//         }
//         else if(e.key == "%"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "%");
//             simbolo = true;
//         }
//         else if(e.key == "/"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "/");
//             simbolo = true;
//         }
//         else if(e.key == "<"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, "<");
//             simbolo = true;
//         }
//         else if(e.key == ">"){// ; es el mismo que el ,
//             noSpan(this,e);
//             nuevoSpan(this, ">");
//             simbolo = true;
//         }
//     });
//     $("#editor").on("keydown", function(e){
//         if (e.keyCode === 9) { // tab key
//             e.preventDefault();  // this will prevent us from tabbing out of the editor
    
//             // now insert four non-breaking spaces for the tab key
//             var editor = document.getElementById("editor");
//             var doc = editor.ownerDocument.defaultView;
//             var sel = doc.getSelection();
//             var range = sel.getRangeAt(0);
    
//             var tabNode = document.createTextNode("\u00a0\u00a0\u00a0\u00a0");
//             range.insertNode(tabNode);
//             range.setStartAfter(tabNode);
//             range.setEndAfter(tabNode); 
//             sel.removeAllRanges();
//             sel.addRange(range);
//         }
//     });
//     function getLinea() {
//         posicion = window.getSelection();
//         // console.log(posicion.getRangeAt(0).commonAncestorContainer.parentElement.parentElement.getAttribute("data-linea"));
//         linea = parseInt(posicion.getRangeAt(0).commonAncestorContainer.parentElement.parentElement.getAttribute("data-linea"));
//     }
//     function procesamiento(thiss){
//         objeto = thiss.children[linea];
//         // noSpan(objeto);
//     }
//     function ordenar_divs(thiss) {
//         for(var i = 0; i<thiss.children.length;i++){
//             thiss.children[i].dataset.linea = i;
//             for(var j = 0 ; j < thiss.children[i].children.length ; j++){
//                 thiss.children[i].children[j].dataset.id = j;
//             }
//         }
//     }
//     function getEstado(objeto){
//         posicion = window.getSelection().focusOffset;
//         // console.log("objeto "+objeto.getAttribute("data-id")+" en la posicion "+posicion);
//         elemento = parseInt(objeto.getAttribute("data-id"));
//     };
//     function getPuntero(){
//         posicion = window.getSelection();
//         // console.log("objeto "+posicion.getRangeAt(0).commonAncestorContainer.parentElement.getAttribute("data-id")+" en la posicion "+posicion.focusOffset);
//         elemento = parseInt(posicion.getRangeAt(0).commonAncestorContainer.parentElement.getAttribute("data-id"));
//     }
//     function setPuntero(thiss,numero){
//             var sel = window.getSelection();
//             var child = $(thiss).children();
//             var range = document.createRange();
//             range.setStart(child[numero],1);
//             range.collapse(true);
//             sel.removeAllRanges();
//             sel.addRange(range);
//             thiss.focus();
//     }
//     function nuevoSpan(thiss,caracter){
       
//             $(thiss).children()[linea].children[elemento].textContent = $(thiss).children()[linea].children[elemento].textContent.slice(0, -1);
        
//         temp = document.createElement("span");
//         temp.dataset.id = elemento + 1;
//         temp.appendChild(document.createTextNode(caracter));
//         thiss.children[linea].insertBefore(temp,$(thiss).children()[linea].children[elemento+1]);
//         if(elemento < $(thiss).children()[linea].children.length-2){
//                 for(let i = elemento + 2; i<$(thiss).children()[linea].children.length;i++){
//                     // console.log($(thiss).children()[i]);
//                     $(thiss).children()[linea].children[i].dataset.id = i; 
//                     // console.log(i);
//                 }
//         }
//         setPuntero(thiss.children[linea ],elemento+1);
//     }
    
//     function noSpan(thiss){
//         if($(thiss).children().length == 0){
//             console.log(thiss);
//             // $(thiss).html() = "";
//             span = document.createElement("span");
//             span.dataset.id = 0;
//             // span.appendChild(document.createTextNode($(thiss).text()));
//             thiss.appendChild(span);
//             setPuntero(thiss,0);
//         }
//     }
    
//     var xd =document.getElementById("editor");

