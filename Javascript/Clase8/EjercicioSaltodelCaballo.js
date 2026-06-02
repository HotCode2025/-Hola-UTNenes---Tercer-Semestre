/*
El problema consiste en encontrar un recorrido donde el caballo visite todas las casillas
del tablero exactamente una vez.

Características:
- Tablero 8x8
- Comienza en (0,0)
- Debe recorrer 64 casillas
- Utiliza Backtracking (vuelta atrás)

Funcionamiento:

El caballo prueba movimientos válidos. Si un camino falla, vuelve atrás y prueba otro
hasta encontrar la solución.
*/

// Tamaño tablero 8x8. Creamos la constante N que guarda el número 8.
const N = 8;

// Creamos tablero vacío. Se llena con -1 porque significa: casilla todavía no visitada
let tablero = Array(N)
.fill()
.map(() => Array(N).fill(-1));

// Movimientos posibles del caballo
// movX y movY trabajan juntos

const movX = [2,1,-1,-2,-2,-1,1,2];

const movY = [1,2,2,1,-1,-2,-2,-1];


// Verificar si el movimiento sirve (debe estar dentro del tablero y no debe haber sido visitada)

function esValido(x,y){

    return(

    x >= 0 &&          // no salir izquierda
    y >= 0 &&          // no salir arriba
    x < N &&           // no salir derecha
    y < N &&           // no salir abajo
    tablero[x][y] == -1 // casilla libre

    );

}


// Función principal Backtracking
// x,y → posición actual
// salto → número movimiento actual

function caballo(x,y,salto){

    // Si recorrió todas las casillas termina el problema

    if(salto == N*N){

        return true;

    }

    // Probar los 8 movimientos

    for(let i=0;i<8;i++){

        // Calcula nueva posición
        let nx = x + movX[i];

        let ny = y + movY[i];

        // Si sirve el movimiento 
        if(esValido(nx,ny)){


            // Guarda movimiento

            tablero[nx][ny] = salto;


            // Mostrar movimientos en consola

            console.log(

                "Salto",
                salto,
                "->",
                "(" + nx + "," + ny + ")"

            );

            // Seguir buscando solución (recursividad)

            if(

                caballo(
                    nx,
                    ny,
                    salto+1
                )

            ){

                return true;

            }

            // Backtracking:
            // borrar movimiento
            // volver atrás
            // probar otro camino

            tablero[nx][ny] = -1;

        }

    }

    // Ningún movimiento funcionó
    return false;

}


// Posición inicial indicada por el profesor: (0,0)

tablero[0][0] = 0;

// Ejecutar algoritmo

if(

    caballo(
        0,
        0,
        1
    )

){

    console.log("\nSOLUCIÓN:\n");

    console.table(tablero);

}

else{

    console.log(
        "No existe solución"
    );

}