class Computadora {
  constructor(id, nombre, monitor, raton, teclado, contador) {
    ((this.id = id),
      (this.nombre = nombre),
      (this.monitor = monitor),
      (this.raton = raton),
      (this.teclado = teclado),
      (this.contador = contador));
  }
  toString() {
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
    ((this.id = id),
      (this.computadora = computadora),
      (this.contadorOrdenes = contadorOrdenes));
  }
  agregarcomputadora(computadora) {
    this.computadora.push(computadora)
    console.log('Computadora Agregada existosamente')
    console.log(computadora)
  }
  mostrarOrden() {
    return(`
        
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
    ((this.id = id),
      (this.marca = marca),
      (this.tamanio = tamanio),
      (this.contadorMonitores = contadorMonitores));
  }
  toString() {
    return `Monitor:
                Id: ${this.id}
                Marca:${this.marca}
                Tamaño: ${this.tamanio}
                Stock (Contador): ${this.contadorMonitores}
                `;
  }
  getIdMonitor() {}
}

class Raton {
  constructor(id, contador) {
    ((this.id = id), (this.contador = contador));
  }
  toString() {
    return `Raton
                Id:${this.id}
                Stock(Contador):${this.contador}
                `;
  }
}

class Teclado {
  constructor(id, contador) {
    ((this.id = id), (this.contador = contador));
  }
  toString() {
    return `Teclado
                Id:${this.id}
                Stock(Contador):${this.contador}
                `;
  }
}

class DispositivoDeEntrada {
  constructor(tipo, marca) {
    ((this.tipo = tipo), (this.marca = marca));
  }
  getTipo(tipo) {
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
    if (tipo == "Raton") {
      const raton = new Raton(10,30);
      console.log(raton.toString())
      console.log(`Creado raton existosamente`)
    }
    if (tipo == "Teclado") {
      const teclado = new Teclado(15,25);
      console.log(teclado.toString())
      console.log(`Creado teclado existosamente`)
    }
    else{
        console.log('Datos incorrectos. Porfavor ingresar Raton o Teclado')
    }
  }
}

const monitor = new Monitor(1, "Lg", "24 pulgadas", 10);
console.log(monitor.toString());

const monitor2 = new Monitor(2, "Samsung", "19 pulgadas", 7);
console.log(monitor.toString());

const raton = new DispositivoDeEntrada('Raton','Lg')
const teclado = new DispositivoDeEntrada('Teclado','RedDragon')

raton.setTipo('Raton')
teclado.setTipo('Teclado')
teclado.setTipo('camiseta')


const datosRaton= raton.getTipo('Raton')
const datosTeclado = teclado.getTipo('Teclado')

const compu1 = new Computadora(100, 'Gamer', monitor , datosRaton, datosTeclado, 1)
console.log(compu1.toString())
const compu2 = new Computadora(101, 'Oficina', monitor2 , datosRaton, datosTeclado, 1)
console.log(compu2.toString())

const ordenComputadoras = []
const orden = new Orden(1000,ordenComputadoras,1)
orden.agregarcomputadora(compu1)
orden.agregarcomputadora(compu2)

console.log(orden.mostrarOrden())
