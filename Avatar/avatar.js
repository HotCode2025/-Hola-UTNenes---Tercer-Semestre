function seleccionarPersonajeJugador() {

    let zuko = document.getElementById("zuko")
    let katara = document.getElementById("katara")
    let aang = document.getElementById("aang")
    let toph = document.getElementById("toph")

    if (zuko.checked) {
        let opt = document.getElementById("heroe-eleccion")
        opt.textContent = "Zuko"
        personajeSeleccionado = true;
    } else if (katara.checked) {
        let opt = document.getElementById("heroe-eleccion")
        opt.textContent = "Katara"
        personajeSeleccionado = true;
    } else if (aang.checked) {
        let opt = document.getElementById("heroe-eleccion")
        opt.textContent = "Aang"
        personajeSeleccionado = true;
    } else if (toph.checked) {
        let opt = document.getElementById("heroe-eleccion")
        opt.textContent = "Toph"
        personajeSeleccionado = true;
    } else {
        alert("Debes seleccionar un personaje")
        personajeSeleccionado = false;
        return;
    }
    let personajeEnemigo = Math.floor(Math.random() * (4 - 1 + 1) + 1);
    if (personajeEnemigo == 1) {
        let opt = document.getElementById("enemigo-eleccion")
        opt.textContent = "Zuko"
    } else if (personajeEnemigo == 2) {
        let opt = document.getElementById("enemigo-eleccion")
        opt.textContent = "Katara"
    } else if (personajeEnemigo == 3) {
        let opt = document.getElementById("enemigo-eleccion")
        opt.textContent = "Aang"
    } else if (personajeEnemigo == 4) {
        let opt = document.getElementById("enemigo-eleccion")
        opt.textContent = "Toph"
    }
}

let botonPersonajeJugador = document.getElementById("boton-personaje")
botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador)

function toggleReglas() {
    let reglasDiv = document.getElementById("reglas-contenedor")
    let botonReglas = document.getElementById("boton-reglas")

    if (reglasDiv.style.display === "none") {
        reglasDiv.style.display = "block"
        botonReglas.textContent = "Ocultar Reglas"
    } else {
        reglasDiv.style.display = "none"
        botonReglas.textContent = "Mostrar Reglas"
    }
}

let botonReglas = document.getElementById("boton-reglas")
botonReglas.addEventListener("click", toggleReglas)

let vidasJugador = 3;
let vidasEnemigo = 3;
let personajeSeleccionado = false;

// Función que genera un ataque aleatorio del enemigo
function generaAtaqueEnemigo() {
    let ataques = ["Patada", "Puño", "Barrida"];
    let indiceAleatorio = Math.floor(Math.random() * ataques.length);
    return ataques[indiceAleatorio];
}

// Función que determina quién gana el combate
function determinarGanador(ataqueJugador, ataqueEnemigo) {
    if (ataqueJugador === ataqueEnemigo) {
        return "empate"; // Si son iguales, no pasa nada
    }

    // Patada > Puño
    if (ataqueJugador === "Patada" && ataqueEnemigo === "Puño") {
        return "jugador";
    }
    // Puño > Barrida
    if (ataqueJugador === "Puño" && ataqueEnemigo === "Barrida") {
        return "jugador";
    }
    // Barrida > Patada
    if (ataqueJugador === "Barrida" && ataqueEnemigo === "Patada") {
        return "jugador";
    }

    return "enemigo"; // Si el enemigo no pierde, el enemigo gana
}

// Función que ejecuta el combate
function ejecutarCombate(ataqueJugador) {
    // Validar que se haya seleccionado un personaje
    if (!personajeSeleccionado) {
        alert("Debes seleccionar un personaje primero");
        return;
    }

    let ataqueEnemigo = generaAtaqueEnemigo();
    let ganador = determinarGanador(ataqueJugador, ataqueEnemigo);

    // Actualizar los elementos HTML con los ataques
    document.getElementById("heroe-eleccion").textContent = ataqueJugador;
    document.getElementById("enemigo-eleccion").textContent = ataqueEnemigo;

    let resultadoDiv = document.getElementById("resultado-combate");

    if (ganador === "empate") {
        resultadoDiv.textContent = "¡EMPATE! Ambos atacaron con " + ataqueJugador;
    } else if (ganador === "jugador") {
        vidasEnemigo--;
        resultadoDiv.textContent = "¡GANASTE! Tu " + ataqueJugador + " venció al " + ataqueEnemigo + " del enemigo. Vidas del enemigo: " + vidasEnemigo;
    } else {
        vidasJugador--;
        resultadoDiv.textContent = "¡PERDISTE! Su " + ataqueEnemigo + " venció a tu " + ataqueJugador + ". Tus vidas: " + vidasJugador;
    }

    // Actualizar las vidas en el HTML
    document.getElementById("vida-jugador").textContent = vidasJugador;
    document.getElementById("vida-enemigo").textContent = vidasEnemigo;

    // Verificar si el juego terminó
    if (vidasJugador === 0) {
        resultadoDiv.textContent += " | ¡JUEGO TERMINADO! El enemigo ganó.";
        deshabilitarBotones();
    } else if (vidasEnemigo === 0) {
        resultadoDiv.textContent += " | ¡JUEGO TERMINADO! ¡Ganaste!";
        deshabilitarBotones();
    }
}

function deshabilitarBotones() {
    document.getElementById("boton-punio").disabled = true;
    document.getElementById("boton-patada").disabled = true;
    document.getElementById("boton-barrida").disabled = true;
}

function ataquePatada() {
    ejecutarCombate("Patada");
}

function ataqueBarrida() {
    ejecutarCombate("Barrida");
}

function ataquePuño() {
    ejecutarCombate("Puño");
}

// Agregar event listeners a los botones
let botonPatada = document.getElementById("boton-patada");
let botonPuño = document.getElementById("boton-punio");
let botonBarrida = document.getElementById("boton-barrida");

botonPatada.addEventListener("click", ataquePatada);
botonPuño.addEventListener("click", ataquePuño);
botonBarrida.addEventListener("click", ataqueBarrida);

// Función para reiniciar el juego
function reiniciarJuego() {
    vidasJugador = 3;
    vidasEnemigo = 3;
    personajeSeleccionado = false;

    // Limpiar selecciones
    document.getElementById("zuko").checked = false;
    document.getElementById("katara").checked = false;
    document.getElementById("aang").checked = false;
    document.getElementById("toph").checked = false;

    // Reiniciar textos
    document.getElementById("heroe-eleccion").textContent = "-";
    document.getElementById("enemigo-eleccion").textContent = "-";
    document.getElementById("resultado-combate").textContent = "Selecciona un personaje y comienza el combate...";

    // Reiniciar vidas
    document.getElementById("vida-jugador").textContent = "3";
    document.getElementById("vida-enemigo").textContent = "3";

    // Habilitar botones
    botonPatada.disabled = false;
    botonPuño.disabled = false;
    botonBarrida.disabled = false;
}

let botonReiniciar = document.getElementById("boton-reiniciar");
botonReiniciar.addEventListener("click", reiniciarJuego);