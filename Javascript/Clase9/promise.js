
//  ------------------- Primero promesa y luego el objeto  ------------------- 
let expresion = true;

let miPromesa = new Promise( (resolver,rechazar) => { 
    if (expresion){
        resolver ('Resolvió correctamente');
    
    } else{
        rechazar('Se produjo un error');
    }

})

//  ------------------- CASO THEN  ------------------- 
//miPromesa.then(
//    valor => console.log(valor),
//    error => console.log(error)
//);

//  ------------------- CASO CATCH  ------------------- 
//miPromesa
//   .then( valor => console.log(valor))
//   .catch(error => console.log(error));

let promesa = new Promise ( (resolver) => {
    //console.log('Inicio');
    setTimeout(() => resolver ('Saludos desde promesa, callback, función flecha y setTimeout '), 3000) // 3 segunso = 3000 ms
    //console.log('Final');
});


async function miFuncionConPromesa(){
    return 'Saludos desde promesa con async';
}


async function funcionConPromesaYAwait(){
    let miPromesa = new Promise (resolver => {
        resolver('Promesa con await');
    });
    console.log(await miPromesa);
}


//  ------------------- Promesas  ------------------- 
async function funcionConPromesaYAwaitTimeout(){
    let miPromesa = new Promise (resolver => {
        console.log('inicio funcion');
        setTimeout (() => resolver ('Promesa con await y Timeout , se ejecuta al final'), 3000);
        console.log('Final funcion')
    });
    console.log(await miPromesa);
}

//  ------------------- Inicializamos la funcion  ------------------- 
funcionConPromesaYAwaitTimeout();