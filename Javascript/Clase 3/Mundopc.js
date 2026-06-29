//Mini documentación dentro del archivo para facilitar la lectura.
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

    usar(){
        return `RATON LISTO PARA PRENDER`
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
    
    usar(){
        return `TECLADO LISTO PARA PRENDER`
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
    usar(){
        return `
            COMPUTADORA USADA:
            Raton: ${this._raton.usar()}
            Teclado: ${this._teclado.usar()}
            Monitor: ${this._monitor.usar()}
            `
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

    usar(){
        return `MONITOR LISTO PARA PRENDER`
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

// ─────────────────────────────────────────────────────────────────────────────
// CLASE ORDEN — ¿qué pasa con el polimorfismo acá?
//
// Orden NO sabe ni le importa si lo que guarda es una compu gamer, de oficina
// o cualquier otro subtipo de Computadora que exista en el futuro.
// Solo llama a usar() y cada objeto responde según su propia implementación.
//
// Eso es polimorfismo: un mismo mensaje (usar()) produce comportamientos
// distintos según el tipo real del objeto que lo recibe.
// ─────────────────────────────────────────────────────────────────────────────
class Orden {
    static contadorOrdenes = 0;
    constructor() {
        // Una orden contiene un identificador y un arreglo de computadoras
        this._id = ++Orden.contadorOrdenes;
        this._computadora = [];
    }

    agregarComputadora(computadora) {
        this._computadora.push(computadora);
    }

    // POLIMORFISMO en acción:
    // forEach recorre la lista sin conocer el tipo concreto de cada elemento.
    // Raton, Teclado, Monitor y Computadora responden a usar() cada uno a su manera.
    reconocer() {
        console.log('----------- POLIMORFISMO EN ORDEN --------------');
        this._computadora.forEach((compu) => {
            // compu puede ser cualquier Computadora; usar() delega en sus componentes
            console.log(compu.usar());
        });
    }

    mostrarOrden() {
        // Bug original: if([expr]) siempre es truthy porque crea un array no vacío.
        // Correcto: comparar directamente la longitud del arreglo.
        if (this._computadora.length === 0) {
            return `Su orden (id:${this._id}) está VACÍA.`;
        }

        let resultado = `\nSu orden | id: ${this._id}\n${'─'.repeat(30)}\n`;
        // Bug original: forEach no retorna nada, nunca se mostraba en el template literal.
        // Correcto: acumular el resultado en una variable y retornarla.
        this._computadora.forEach((computadora, i) => {
            resultado += `\n[${i + 1}] ${computadora.toString()}`;
        });
        return resultado;
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

// Argegamos una computadora 

orden.agregarComputadora(compu1)
orden.agregarComputadora(compu2)



// DEMOSTRACIÓN DE POLIMORFISMO
//
// Esta función recibe un arreglo heterogéneo: puede contener objetos de tipo
// Raton, Teclado, Monitor o Computadora mezclados.
// Llama a usar() en cada uno sin importar qué tipo sea.
//
// Por qué funciona: todas las clases implementan usar() con su propia lógica.
// La función no necesita if/switch para distinguir tipos → eso ES polimorfismo.
//
// ¿Qué pasa con Orden?
// Orden hace lo mismo pero sólo con Computadoras. Al agregar demostrarPolimorfismo
// vemos que el concepto aplica igual a cualquier objeto que comparta la interfaz usar().
function demostrarPolimorfismo(dispositivos) {
    console.log('\n========= DEMOSTRACIÓN DE POLIMORFISMO =========');
    dispositivos.forEach((dispositivo, i) => {
        // constructor.name devuelve el nombre real de la clase en tiempo de ejecución
        console.log(`[${i + 1}] ${dispositivo.constructor.name} → ${dispositivo.usar()}`);
    });
    console.log('=================================================\n');
}

// Arreglo con instancias de DISTINTAS clases mezcladas
// Raton, Teclado, Monitor y Computadora responden al mismo método usar()
// pero cada uno lo hace diferente → polimorfismo
const todosLosDispositivos = [raton1, teclado1, monitor1, compu1, raton2, teclado2, monitor2, compu2];
demostrarPolimorfismo(todosLosDispositivos);

// orden.reconocer() también demuestra polimorfismo: llama usar() en cada Computadora
// sin saber qué tipo concreto de Computadora es cada elemento de la lista
orden.reconocer();

console.log(orden.mostrarOrden());