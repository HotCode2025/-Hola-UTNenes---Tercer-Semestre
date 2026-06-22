// Cada torre es un array. Los números representan el tamaño del disco.
// El disco más grande es el 3, el más chico es el 1.

var torres = [
  [3, 2, 1],  // Torre A empieza con todos los discos
  [],         // Torre B vacía
  []          // Torre C vacía
];

var torreSeleccionada = null;  // Guarda qué torre fue clickeada primero
var cantMovimientos = 0;

var colores = ["#e74c3c", "#3498db", "#2ecc71"];  // Un color por disco

// Se ejecuta al cargar la página
mostrarTorres();

function seleccionarTorre(indice) {

  // Si no hay ninguna torre seleccionada todavía
  if (torreSeleccionada === null) {

    // Verificamos que la torre no esté vacía
    if (torres[indice].length === 0) {
      mostrarMensaje("Esa torre está vacía. Elegí otra.");
      return;
    }

    torreSeleccionada = indice;
    mostrarMensaje("Torre " + nombreTorre(indice) + " seleccionada. Ahora elegí el destino.");
    marcarSeleccionada(indice);

  } else {

    // Si hacemos clic en la misma torre, cancelamos
    if (torreSeleccionada === indice) {
      torreSeleccionada = null;
      mostrarMensaje("Selección cancelada.");
      mostrarTorres();
      return;
    }

    // Intentamos mover el disco
    var desde = torreSeleccionada;
    var hasta  = indice;
    torreSeleccionada = null;

    if (esMovimientoValido(desde, hasta)) {
      moverDisco(desde, hasta);
    } else {
      mostrarMensaje("Movimiento inválido: no podés poner un disco grande sobre uno chico.");
      mostrarTorres();
    }
  }
}

function esMovimientoValido(desde, hasta) {
  var discoOrigen = torres[desde][torres[desde].length - 1];  // Tope de la torre origen

  // Si la torre destino está vacía, siempre es válido
  if (torres[hasta].length === 0) {
    return true;
  }

  var discoDestino = torres[hasta][torres[hasta].length - 1]; // Tope de la torre destino

  // Solo es válido si el disco que movemos es más chico
  return discoOrigen < discoDestino;
}

function moverDisco(desde, hasta) {
  var disco = torres[desde].pop();   // Sacamos el disco de la torre origen
  torres[hasta].push(disco);         // Lo ponemos en la torre destino

  cantMovimientos++;
  document.getElementById("contador").textContent = cantMovimientos;

  // Mostramos el movimiento en consola (para el profe)
  console.log("Movimiento " + cantMovimientos + ": Disco " + disco + " de Torre " + nombreTorre(desde) + " a Torre " + nombreTorre(hasta));
  console.log("  Estado -> A: [" + torres[0] + "] | B: [" + torres[1] + "] | C: [" + torres[2] + "]");

  mostrarTorres();
  verificarGanador();
}

function verificarGanador() {
  // Ganamos si todos los discos están en la Torre C
  if (torres[2].length === 3) {
    mostrarMensaje("¡Ganaste en " + cantMovimientos + " movimientos! 🎉");
    console.log("¡Juego terminado! Movimientos usados: " + cantMovimientos);
  } else {
    mostrarMensaje("Buen movimiento. Seguí jugando.");
  }
}

function mostrarTorres() {
  for (var i = 0; i < 3; i++) {
    var torreEl = document.getElementById("torre-" + i);
    torreEl.innerHTML = "";  // Limpiamos la torre en pantalla
    torreEl.classList.remove("seleccionada");

    // Dibujamos cada disco de la torre
    for (var j = 0; j < torres[i].length; j++) {
      var tamano = torres[i][j];
      var disco = document.createElement("div");
      disco.classList.add("disco");
      disco.style.width = (tamano * 30) + "px";
      disco.style.backgroundColor = colores[tamano - 1];
      disco.textContent = tamano;
      torreEl.appendChild(disco);
    }
  }
}

function marcarSeleccionada(indice) {
  mostrarTorres();
  document.getElementById("torre-" + indice).classList.add("seleccionada");
}

function nombreTorre(indice) {
  var nombres = ["A", "B", "C"];
  return nombres[indice];
}

function mostrarMensaje(texto) {
  document.getElementById("mensaje").textContent = texto;
}

function reiniciar() {
  torres = [
    [3, 2, 1],
    [],
    []
  ];
  torreSeleccionada = null;
  cantMovimientos = 0;
  document.getElementById("contador").textContent = 0;
  mostrarMensaje("Juego reiniciado. Seleccioná una torre para empezar.");
  mostrarTorres();
  console.log("--- Juego reiniciado ---");
}