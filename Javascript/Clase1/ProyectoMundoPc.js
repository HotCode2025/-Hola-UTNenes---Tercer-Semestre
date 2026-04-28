// Mini documentación dentro del archivo para facilitar la lectura.
// Este script crea objetos que representan componentes de una computadora
// y luego genera una orden con varias computadoras.

class DispositivoDeEntrada {
    constructor(tipo, marca) {
        // Un dispositivo de entrada puede ser ratón o teclado
        this._tipo = tipo, this._marca = marca;
    }

    get tipoEntrada(){
        return this._tipo
    }
    set tipoEntrada(tipo){
        this._tipo=tipo;
    }

     get marca(){
        return this._marca
    }
    set marca(marca){
        this._marca=marca
    }
}

class Raton extends DispositivoDeEntrada{
    static contadorRatones=0;
    constructor(tipo,marca) {
        super(tipo,marca);
        // Identificador y stock del ratón
        this._id = ++Raton.contadorRatones;
    }

     toString() {
        // Devuelve la descripción del raton
        return `Raton
                Id:${this._id}
                Tipo: ${this._tipo},
                Marca: ${this._marca}
                `;
    }
}

class Teclado extends DispositivoDeEntrada{
    static contadorTeclados=0;
    constructor(tipo,marca) {
        super(tipo,marca)
        // Identificador y stock del ratón
        this._id = ++Teclado.contadorTeclados;
    }

    toString() {
        // Devuelve la descripción del teclado
        return `Teclado
                Id:${this._id}
                Tipo: ${this._tipo},
                Marca: ${this._marca}
                `;
    }
}



class Computadora {
    static contadorCompus = 0;
    constructor(nombre, monitor, raton, teclado) {

        // Propiedades de la computadora
            (this._id = ++Computadora.contadorCompus),
            (this._nombre = nombre),
            (this._monitor = monitor),
            (this._raton = raton),
            (this._teclado = teclado)
            
    }

    toString() {
        // Devuelve una descripción completa de la computadora
        return `Computadora:
            Id:${this._id}
            nombre:${this._nombre}
            ${this._monitor}
            Raton:${this._raton}
            ${this._teclado}
            `;
    }
}



class Monitor {
    static contadorMonitores=0;
    constructor(marca, tamanio) {
        // Datos principales del monitor
        (this._id = ++Monitor.contadorMonitores),
        (this._marca = marca),
        (this._tamanio = tamanio)
    }

    toString() {
        // Devuelve la descripción del monitor
        return `Monitor:
                Id: ${this._id}
                Marca:${this._marca}
                Tamaño: ${this._tamanio}
                `;
    }
}

class Orden {
    static contadorOrdenes =0;
    constructor() {
        // Una orden contiene un identificador y un arreglo de computadoras
            this._id = ++Orden.contadorOrdenes,
            this._computadora = []
    }

        agregarComputadora(computadora){
            this._computadora.push(computadora)
        }
        mostrarOrden() {
        // Muestra por consola la información de la orden completa
       if([this._computadora.length == 0]){
         return (`
        
        Su orden:

        ESTA VACIA

        `)
       }else{
         return (`
        
        Su orden:
        id:${this._id}

        ------------------------------

        ${this._computadora[0]}

        ------------------------------

        ${this._computadora[1]}

        `)
       }
    }
}

// Creación de monitores y muestra de sus datos
const monitor1 = new Monitor("Lg","24 pulgadas");
console.log(monitor1.toString());

const monitor2 = new Monitor("Samsung","19 pulgadas");
console.log(monitor2.toString());


const raton1 = new Raton('gamer', ' LG')
const raton2= new Raton('oficina', 'Genius')
const teclado1= new Teclado ('gamer','razr')
const teclado2= new Teclado ('oficina', ' genius')

// Creación de computadoras con los componentes definidos
const compu1 = new Computadora('Gamer', monitor1, raton1, teclado1,)
console.log(compu1.toString())
const compu2 = new Computadora('Oficina', monitor2, raton2, teclado2)
console.log(compu2.toString())

// Construcción de una orden
const orden= new Orden();


// Mostrar la orden completa en consola
console.log(orden.mostrarOrden())

// Argegamos una computadora 
orden.agregarComputadora(compu1)
orden.agregarComputadora(compu2)
// POLIMORFISMO
 console.log('  --------------------  POLIMORFISMO  --------------------  ')
const dispositivos = [ raton1 , teclado1, monitor1]
dispositivos.forEach(dispositivo =>{
    console.log(dispositivo.toString())
})

// La clase ORDEN no deberia estar afeactada, ya que cada dispositivo, tiene sus caracteristicas propias, las cuales son aceptadas por esta, y se adapta a elllas.