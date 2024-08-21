let cadena = location.search;
let datos = new URLSearchParams(cadena);
let resultado = {};

for (const [nombre, valor] of datos) {
    resultado[nombre] = valor;
}

console.log(resultado);

document.getElementById("id").value = resultado["id"];
document.getElementById("puntos_equipo").value = resultado["puntos_equipo"];
document.getElementById("partidos_ganados").value = resultado["partidos_ganados"];

function modificar() {
    let id = document.getElementById("id").value;
    let ptsForm = document.getElementById("puntos_equipo").value;
    let partidosGanadosForm = document.getElementById("partidos_ganados").value;

    let equipo = {};

    if (ptsForm) {
        equipo.puntos_equipo = ptsForm;
    }

    if (partidosGanadosForm) {
        equipo.partidos_ganados = partidosGanadosForm;
    }

    let url = "http://localhost:3500/update/" + id;
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
            window.location.href = "./football";
        })
        .catch(err => {
            console.error(err);
            alert("Error al Modificar");
        });
}

document.addEventListener('DOMContentLoaded', function() {
    cargarEquipos();
});

function cargarEquipos() {
    fetch('/obtener_equipos')
        .then(response => response.json())
        .then(data => {
            let select = document.getElementById("nombre");
            data.forEach(function(equipo) {
                let option = document.createElement("option");
                option.value = equipo.nombre_equipo;
                option.text = equipo.nombre_equipo;
                select.add(option);
            });
        })
        .catch(error => console.error("Error al cargar los equipos:", error));
}

function buscarIdPorNombre() {
    let nombre = document.getElementById("nombre").value;
    if (nombre) {
        fetch(`/buscar_id?nombre=${encodeURIComponent(nombre)}`)
            .then(response => response.json())
            .then(data => {
                if (data.id) {
                    document.getElementById("id").value = data.id;
                } else {
                    document.getElementById("id").value = "No encontrado";
                }
            })
            .catch(error => console.error("Error al buscar el ID:", error));
    } else {
        document.getElementById("id").value = "";
    }
}