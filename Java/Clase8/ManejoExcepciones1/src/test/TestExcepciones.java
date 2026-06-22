package test;

import static aritmetica.Aritmetica.division;
import excepciones.OperacionExcepcion;

public class TestExcepciones {
    public static void main(String[] args) {
       int resultado = 0;
       try{
                 resultado = division(10,0 );
       // Se pueden tener varios catch con distintas excepciones, pero siguiendo el orden jerarquico siempre
       }catch(OperacionExcepcion e){
           System.out.println("Ocurrio un error de tipo OperacionExcepcion");
           System.out.println(e.getMessage());
       }catch (Exception e) {
                    System.out.println("Ocurrio un Error");
                    e.printStackTrace(System.out);// Se conoce como la pila de excepciones
                    System.out.println(e.getMessage());
       }finally{
           System.out.println("Se reviso la division entre cero");
       }
        System.out.println("La variable de resultadotiene como valor: " + resultado);
    }
}

