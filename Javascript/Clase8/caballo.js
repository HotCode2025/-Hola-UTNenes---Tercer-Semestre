const N = 8;

// Tablero vacío
let tablero = Array(N).fill().map(() => Array(N).fill(-1));

// Movimientos del caballo
const movX = [2,1,-1,-2,-2,-1,1,2];
const movY = [1,2,2,1,-1,-2,-2,-1];

// Verificar si el movimiento es válido
function esValido(x,y){
    return (
        x >= 0 &&
        y >= 0 &&
        x < N &&
        y < N &&
        tablero[x][y] === -1
    );
}

// Orden de movimientos
function siguienteMovimientos(x,y){
    let opciones = [];
    for(let i=0;i<8;i++){
        let nx = x + movX[i];
        let ny = y + movY[i];
        if(esValido(nx,ny)){
            let count = 0;
            for(let j=0;j<8;j++){
                let ex = nx + movX[j];
                let ey = ny + movY[j];
                if(esValido(ex,ey)) count++;
            }
            opciones.push({nx,ny,count});
        }
    }
    opciones.sort((a,b) => a.count - b.count);
    return opciones;
}

// Backtracking
function caballo(x,y,salto){
    if(salto === N*N) return true;

    for(let {nx,ny} of siguienteMovimientos(x,y)){
        tablero[nx][ny] = salto;
        if(caballo(nx,ny,salto+1)) return true;
        tablero[nx][ny] = -1; // backtrack
    }
    return false;
}

// Definimos la posición inicial
tablero[0][0] = 0;

// Ejecucion
if(caballo(0,0,1)){
    console.log("\nSOLUCIÓN:\n");
    console.table(tablero);
} else {
    console.log("No existe solución");
}
