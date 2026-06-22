package domain;

import java.io.Serializable;

public class Persona implements Serializable{
        // Para que se consideer javaBeans debe implementar : Debe tener constructor vacio, y cada atributo debe ser privado, y cada uno 
       // debe tener sus get y set encapsulados , y un interface que se llama serializable.
      //Serializable : transforma a 0 y 1 nuestro objeto , para poder transferirlo de un servidor a otro
    
    // Atributos  privados : Obligatorio
    private String nombre;
    private String apellido;
    
    // constructor vacio : Obligatorio
    public Persona(){
        // Este constructor no es obligatorio, pero puede tener los que se necesiten , y estos no hace falta q sean vacios
    }
    public Persona(String nombre , String apellido){
        this.nombre= nombre;
        this.apellido=apellido;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return this.apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }
    
}
