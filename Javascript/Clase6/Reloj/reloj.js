// Funcion que usamos para tomar los datos
const datos = () => {

    // Es importante que date este aca, asi actualiza cada 1000ms, sino se queda con su unica actualiazcion
const date = new Date();


const fecha = date.toLocaleDateString("es-AR");
// Convertimos los datos en string, y con padStart , le damos una longitud de 2, y si esto no se cumple, le agrega el 0
const hora = String(date.getHours()).padStart(2,'0');
const minutos = String(date.getMinutes()).padStart(2,'0');
const segundos = String(date.getSeconds()).padStart(2,'0');

// Tomamlos los elementos del documento, y usamos dos funciones que al final tienen el mismo resultado
// para asi actualizar la hora
document.getElementById("fecha").innerHTML = fecha;
document.getElementById('hora').textContent = ` ${hora} : ${minutos} :${segundos} horas`;
};

// Inicializamos la funcion
datos();


// La actualizamos cada 1000ms, asi va en tiempo real
setInterval(datos , 1000);


