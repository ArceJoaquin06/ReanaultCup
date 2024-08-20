let cadena = location.search;
let datos = new URLSearchParams(cadena);
let resultado = {};

for (const [nombre, puntos, valor] of datos) {
    resultado[nombre] = valor;
}

console.log(resultado);

document.getElementById("id").value = resultado["id"]
document.getElementById("nombre").value = resultado["nombre"]
document.getElementById("puntos").value = resultado["puntos"]

function modificar() {
    let id = document.getElementById("id").value
    let nombreForm = document.getElementById("nombre").value
    let ptsForm = document.getElementById("puntos").value

    let equipo = {
        nombre_equipo: nombreForm,
        puntos: ptsForm,
    };
    let url = "http://localhost:3500/footballMirror/" + id;
    let options = {
        body: JSON.stringify(equipo),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    };
    fetch(url, options)
        .then(function () {
            console.log("modificado");
            alert("Registro modificado");
            window.location.href = "./football.html";
        })
        .catch(err => {
            console.error(err);
            alert("Error al Modificar");
        });   
}