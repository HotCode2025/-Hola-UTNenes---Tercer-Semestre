function seleccionarPersonajeJugador() {

    let zuko = document.getElementById("zuko")
    let katara = document.getElementById("katara")
    let aang = document.getElementById("aang")
    let toph = document.getElementById("toph")

    if (zuko.checked) {
        alert("Seleccionaste a Zuko")
    } else if (katara.checked) {
        alert("Seleccionaste a Katara")
    } else if (aang.checked) {
        alert("Seleccionaste a Aang")
    } else if (toph.checked) {
        alert("Seleccionaste a Toph")
    } else {
        alert("Debes seleccionar un personaje")
    }
}

let botonPersonajeJugador = document.getElementById("boton-personaje")
botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador)