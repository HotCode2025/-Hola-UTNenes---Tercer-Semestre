package aritmetica;
import excepciones.OperacionExcepcion;
public class Aritmetica {
    public static int  division(int numerador , int denominador ){
        
        //Podemos borrar esta linea de codigo, q la clase OperacionExcepcion
        //extiende a RuntimeException, y no solo a Exception
 
        //throws OperacionExcepcion{ 
        if (denominador == 0 ){
            throw new OperacionExcepcion("Division entre 0");
        }
        return numerador/denominador;
    }
}
