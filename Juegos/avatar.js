function seleccionarPersonajeJugador() {

    let zuko = document.getElementById("zuko")
    let katara = document.getElementById("katara")
    let aang = document.getElementById("aang")
    let toph = document.getElementById("toph")

    if (zuko.checked) {
        let opt=document.getElementById("heroe-eleccion")
        opt.textContent="Zuko"
    } else if (katara.checked) {
        let opt=document.getElementById("heroe-eleccion")
        opt.textContent="Katara"
    } else if (aang.checked) {
        let opt=document.getElementById("heroe-eleccion")
        opt.textContent="Aang"
    } else if (toph.checked) {
        let opt=document.getElementById("heroe-eleccion")
        opt.textContent="Toph"
    } else {
    alert ("Debes seleccionar un personaje")

    }
    let personajeEnemigo=Math.floor(Math.random()*(4-1+1)+1);
     if (personajeEnemigo==1) {
        let opt=document.getElementById("enemigo-eleccion")
        opt.textContent="Zuko"
    } else if (personajeEnemigo==2) {
        let opt=document.getElementById("enemigo-eleccion")
        opt.textContent="Katara"
    } else if (personajeEnemigo==3) {
        let opt=document.getElementById("enemigo-eleccion")
        opt.textContent="Aang"
    } else if (personajeEnemigo==4) {
        let opt=document.getElementById("enemigo-eleccion")
        opt.textContent="Toph"
    } 
}

let botonPersonajeJugador = document.getElementById("boton-personaje")
botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador)

