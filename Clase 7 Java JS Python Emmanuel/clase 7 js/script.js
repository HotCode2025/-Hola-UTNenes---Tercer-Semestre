let tablero = [];
let N;

function iniciar(){
    N = parseInt(document.getElementById("n").value);
    tablero = [];
    for(let i=0;i<N;i++){
        tablero.push(new Array(N).fill(0));
    }
    resolver(0);
    dibujar();
    mostrarPosiciones();
}

function esSeguro(fila,col){

    for(let i=0;i<col;i++)
        if(tablero[fila][i]==1)
            return false;
    for(let i=fila,j=col;i>=0 && j>=0;i--,j--)
        if(tablero[i][j]==1)
            return false;
    for(let i=fila,j=col;i<N && j>=0;i++,j--)
        if(tablero[i][j]==1)
            return false;
    return true;
}

function resolver(col){

    if(col>=N)
        return true;
    for(let fila=0;fila<N;fila++){
        if(esSeguro(fila,col)){
            tablero[fila][col]=1;
            if(resolver(col+1))
                return true;
            tablero[fila][col]=0;
        }
    }

    return false;
}

function dibujar(){

    let div=document.getElementById("tablero");
    div.innerHTML="";
    div.style.gridTemplateColumns= `repeat(${N}, 60px)`;
    for(let i=0;i<N;i++){
        for(let j=0;j<N;j++){
            let c=document.createElement("div");
            c.className="casilla "+((i+j)%2==0?"blanca":"negra");
            if(tablero[i][j]==1)
                c.innerHTML="♛";
            div.appendChild(c);
        }
    }
}

function mostrarPosiciones(){

    let lista=document.getElementById("posiciones");
    lista.innerHTML="";
    for(let i=0;i<N;i++){
        for(let j=0;j<N;j++){
            if(tablero[i][j]==1){
                let li=document.createElement("li");
                li.textContent="Reina -> Fila: "+i+" Columna: "+j;
                lista.appendChild(li);
            }

        }

    }

}