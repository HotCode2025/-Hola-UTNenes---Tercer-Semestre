function nReinas(n) {
    let tablero = new Array(n).fill(null).map(() => new Array(n).fill("X"));
    let solucionesEncontradas = 0;
    let soluciones = [];

    // Función para verificar si es seguro colocar reina en una posición
    function esSeguro(fila, columna) {
        // Revisar la fila
        for (let j = 0; j < n; j++) {
            if (tablero[fila][j] === "R") {
                return false;
            }
        }

        // Revisar la columna
        for (let i = 0; i < n; i++) {
            if (tablero[i][columna] === "R") {
                return false;
            }
        }

        // Revisar diagonal arriba-izquierda
        for (let i = fila - 1, j = columna - 1; i >= 0 && j >= 0; i--, j--) {
            if (tablero[i][j] === "R") {
                return false;
            }
        }

        // Revisar diagonal arriba-derecha
        for (let i = fila - 1, j = columna + 1; i >= 0 && j < n; i--, j++) {
            if (tablero[i][j] === "R") {
                return false;
            }
        }

        // Revisar diagonal abajo-izquierda
        for (let i = fila + 1, j = columna - 1; i < n && j >= 0; i++, j--) {
            if (tablero[i][j] === "R") {
                return false;
            }
        }

        // Revisar diagonal abajo-derecha
        for (let i = fila + 1, j = columna + 1; i < n && j < n; i++, j++) {
            if (tablero[i][j] === "R") {
                return false;
            }
        }

        return true;
    }

    // Función recursiva para resolver el problema
    function resolver(fila) {
        // Si llegamos al final, encontramos una solución
        if (fila === n) {
            solucionesEncontradas++;
            soluciones.push(tablero.map(fila => [...fila])); // Guardar una copia de la solución
            return;
        }

        // Intentar colocar una reina en cada columna de la fila actual
        for (let columna = 0; columna < n; columna++) {
            if (esSeguro(fila, columna)) {
                // Colocar la reina
                tablero[fila][columna] = "R";

                // Pasar a la siguiente fila
                resolver(fila + 1);

                // Retroceso: quitar la reina
                tablero[fila][columna] = "X";
            }
        }
    }

    // Iniciar la resolución
    resolver(0);

    // Mostrar resultados
    console.log(`Total de soluciones encontradas: ${solucionesEncontradas}`);

    if (soluciones.length > 0) {
        // Seleccionar una solución aleatoria
        const indiceAleatorio = Math.floor(Math.random() * soluciones.length);
        console.log(`\nSolución #${indiceAleatorio + 1} (al azar):`);
        soluciones[indiceAleatorio].forEach(fila => {
            console.log(fila.join(" "));
        });
    }

    return solucionesEncontradas;
}

// Ejecutar para n=8
nReinas(8);
