function poste() {
    yourUrl = ""
    value = "OLOCO"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", yourUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        function: value
    }));
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            alert(xhr.response);
        }
    }
}

function PegaLista() {
    yourUrl = ""
    value = "getLista"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", yourUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        function: value
    }));
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            document.getElementById("listapecas").innerHTML = xhr.response
        }
    }
}

function PegaListaSingle() {
    yourUrl = ""
    value = "getListaSingle"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", yourUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        function: value
    }));
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            document.getElementById("listapecas").innerHTML = xhr.response
        }
    }
}

function aoba() {
    alert("aoba")
}

function login() {
    idOperador1 = document.getElementById("idOperador1").value
    if (idOperador1 != '') {
        window.location.replace("/operador.html");

    } else {
        console.log("id nulo")
        alert("ID invalido")
    }
}

function salvaLista(numlista) {

    console.log(numlista)
    var listaString = $("#formLista").serializeArray()


    yourUrl = ""
    value = "salvaLista"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", yourUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        function: value,
        dados: listaString
    }));
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            document.getElementById("listapecas").innerHTML = xhr.response
        }
    }
}

function salvaListaSingle() {

    var listaString = $("#formLista").serializeArray()


    yourUrl = ""
    value = "salvaListaSingle"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", yourUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        function: value,
        dados: listaString
    }));
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            document.getElementById("listapecas").innerHTML = xhr.response
        }
    }
}


function relatorioFinal() {
    yourUrl = ""
    value = "relatorioFinal"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", yourUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        function: value
    }));
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            //document.getElementById("status").innerHTML = xhr.response
        }
    }
}