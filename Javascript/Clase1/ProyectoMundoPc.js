// Mini documentación dentro del archivo para facilitar la lectura.
// Este script crea objetos que representan componentes de una computadora
// y luego genera una orden con varias computadoras.

class Computadora {
    constructor(id, nombre, monitor, raton, teclado, contador) {
        // Propiedades de la computadora
        ((this.id = id),
            (this.nombre = nombre),
            (this.monitor = monitor),
            (this.raton = raton),
            (this.teclado = teclado),
            (this.contador = contador));
    }

    toString() {
        // Devuelve una descripción completa de la computadora
        return `Computadora:
            Id:${this.id}
            nombre:${this.nombre}
            ${this.monitor}
            Raton:${this.raton}
            ${this.teclado}
            Stock:${this.contador}
            `;
    }
}

class Orden {
    constructor(id, computadora, contadorOrdenes) {
        // Una orden contiene un identificador y un arreglo de computadoras
        ((this.id = id),
            (this.computadora = computadora),
            (this.contadorOrdenes = contadorOrdenes));
    }

    agregarcomputadora(computadora) {
        // Se agrega una computadora a la orden
        this.computadora.push(computadora)
        console.log('Computadora Agregada existosamente')
        console.log(computadora)
    }

    mostrarOrden() {
        // Muestra por consola la información de la orden completa
        return (`
        
        Su orden:
        id:${this.id}

        ------------------------------

        ${this.computadora[0]}

        ------------------------------

        ${this.computadora[1]}

        `)
    }
}

class Monitor {
    constructor(id, marca, tamanio, contadorMonitores) {
        // Datos principales del monitor
        ((this.id = id),
            (this.marca = marca),
            (this.tamanio = tamanio),
            (this.contadorMonitores = contadorMonitores));
    }

    toString() {
        // Devuelve la descripción del monitor
        return `Monitor:
                Id: ${this.id}
                Marca:${this.marca}
                Tamaño: ${this.tamanio}
                Stock (Contador): ${this.contadorMonitores}
                `;
    }

    getIdMonitor() { }
}

class Raton {
    constructor(id, contador) {
        // Identificador y stock del ratón
        ((this.id = id), (this.contador = contador));
    }

    toString() {
        // Devuelve la descripción del ratón
        return `Raton
                Id:${this.id}
                Stock(Contador):${this.contador}
                `;
    }
}

class Teclado {
    constructor(id, contador) {
        // Identificador y stock del teclado
        ((this.id = id), (this.contador = contador));
    }

    toString() {
        // Devuelve la descripción del teclado
        return `Teclado
                Id:${this.id}
                Stock(Contador):${this.contador}
                `;
    }
}

class DispositivoDeEntrada {
    constructor(tipo, marca) {
        // Un dispositivo de entrada puede ser ratón o teclado
        ((this.tipo = tipo), (this.marca = marca));
    }

    getTipo(tipo) {
        // Retorna una descripción según el tipo solicitado
        if (tipo == 'Raton') {
            return `Raton
                Tipo:${this.tipo}
                Marca:${this.marca}
                `;
        }
        if (tipo == 'Teclado') {
            return `Teclado
                Tipo:${this.tipo}
                Marca:${this.marca}
                `;
        } else {
            console.log("Error, Porfavor ingresar tipos validos ( Raton o Teclado )");
        }
    }

    setTipo(tipo) {
        // Crea el dispositivo correspondiente y muestra su información
        if (tipo == "Raton") {
            const raton = new Raton(10, 30);
            console.log(raton.toString())
            console.log(`Creado raton existosamente`)
        }
        if (tipo == "Teclado") {
            const teclado = new Teclado(15, 25);
            console.log(teclado.toString())
            console.log(`Creado teclado existosamente`)
        }
        else {
            console.log('Datos incorrectos. Porfavor ingresar Raton o Teclado')
        }
    }
}

// Creación de monitores y muestra de sus datos
const monitor = new Monitor(1, "Lg", "24 pulgadas", 10);
console.log(monitor.toString());

const monitor2 = new Monitor(2, "Samsung", "19 pulgadas", 7);
console.log(monitor.toString());

// Creación de dispositivos de entrada
const raton = new DispositivoDeEntrada('Raton', 'Lg')
const teclado = new DispositivoDeEntrada('Teclado', 'RedDragon')

// Ejemplo de uso de setTipo para crear dispositivos
raton.setTipo('Raton')
teclado.setTipo('Teclado')
teclado.setTipo('camiseta')

// Obtener datos de los dispositivos según su tipo
const datosRaton = raton.getTipo('Raton')
const datosTeclado = teclado.getTipo('Teclado')

// Creación de computadoras con los componentes definidos
const compu1 = new Computadora(100, 'Gamer', monitor, datosRaton, datosTeclado, 1)
console.log(compu1.toString())
const compu2 = new Computadora(101, 'Oficina', monitor2, datosRaton, datosTeclado, 1)
console.log(compu2.toString())

// Construcción de una orden y agregado de las computadoras
const ordenComputadoras = []
const orden = new Orden(1000, ordenComputadoras, 1)
orden.agregarcomputadora(compu1)
orden.agregarcomputadora(compu2)

// Mostrar la orden completa en consola
console.log(orden.mostrarOrden())
