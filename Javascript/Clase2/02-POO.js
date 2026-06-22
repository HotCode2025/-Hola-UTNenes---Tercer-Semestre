//Video 3: Repasamo la sobreescritura ahora en JavaScript

class Empleado {
    constructor(nombre, sueldo) {
        this._sueldo = sueldo;
    }

    obtenerDetalles() {
        return `Empleado: nombre: ${this._nombre};
        Sueldo: ${this._sueldo}`;
    }
}

class Gerente extends Empleado {
    constructor(nombre, sueldo, departamento) {
        super(nombre, sueldo);
        this._departamento = departamento;
    }

    //Agregamos la sobreescritura del método obtenerDetalles
    obtenerDetalles() {
        return `Gerente: ${super.obtenerDetalles()} depto: ${this._departamento}`;
    }
}

let gerente1 = new Gerente("cARLOS", 5000, "Sistemas");
console.log(gerente1);//Objeto de la clase hija

let empleado1 = new Empleado("Juan", 3000);
console.log(empleado1);//Objeto de la clase padre