
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
function imprimir ( tipo) { //recibe un variable de tipo empleado o gerente
        console.log( tipo.obtenerDetalles()) //se ejecuta el método de la clase que se le pase

        if (tipo instanceof Gerente) {
            console.log("Es un objeto de la clase Empleado");

    }
    else if (tipo instanceof Empleado) {
        console.log ("Es un objeto de la clase Gerente");
        console.log( tipo._departamento) ;
    }

    else if ( tipo instanceof Object) {
        console.log("Es un objeto de la clase Object");
    }

let gerente1 = new Gerente("cARLOS", 5000, "Sistemas");
console.log(gerente1);//Objeto de la clase hija

let empleado1 = new Empleado("Juan", 3000);
console.log(empleado1);//Objeto de la clase padre

imprimir( gerente1 );//Polimorfismo
imrpmir( empleado1 );//Polimorfismo
}

