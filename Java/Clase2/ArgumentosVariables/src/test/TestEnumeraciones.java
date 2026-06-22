
package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

/**
 *
 * @author Sere Olmedo
 */
public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Dia 1: "+Dias.LUNES);
        //indicarDiaSemana(Dias.LUNES);//Las enumeraciones se tratan como cadenas
        //Ahora no se deben utilizar comillas, se accede a traves de el operador de punto
        //System.out.println("Dia 2: "+Dias.MARTES);
        //indicarDiaSemana(Dias.MARTES);
        //Tarea
        //System.out.println("Dia 3: "+Dias.MIERCOLES);
        //indicarDiaSemana(Dias.MIERCOLES);
        //System.out.println("Dia 4: "+Dias.JUEVES);
        //indicarDiaSemana(Dias.JUEVES);
        //System.out.println("Dia 5: "+Dias.VIERNES);
        //indicarDiaSemana(Dias.VIERNES);
        //System.out.println("Dia 6: "+Dias.SABADO);
        //indicarDiaSemana(Dias.SABADO);
        //System.out.println("Dia 7: "+Dias.DOMINGO);
        //indicarDiaSemana(Dias.DOMINGO);
      
        
        //Video 6 - Tarea seguir con los otros continentes 
        System.out.println("Continente No.4: "+Continentes.AMERICA);
        System.out.println("No. de paises en el 4to. continente: "
                +Continentes.AMERICA.getPaises());
        System.out.println("No. de habitantes en el 4to. continente: "
                +Continentes.AMERICA.getHabitantes());
        
        // África
        System.out.println("Continente No.1: " + Continentes.AFRICA);
        System.out.println("No. de paises en el 1er. continente: " 
                + Continentes.AFRICA.getPaises());
        System.out.println("No. de habitantes en el 1er. continente: " 
                + Continentes.AFRICA.getHabitantes());

        // Europa
        System.out.println("Continente No.2: " + Continentes.EUROPA);
        System.out.println("No. de paises en el 2do. continente: " 
                + Continentes.EUROPA.getPaises());
        System.out.println("No. de habitantes en el 2do. continente: " 
                + Continentes.EUROPA.getHabitantes());

        // Asia
        System.out.println("Continente No.3: " + Continentes.ASIA);
        System.out.println("No. de paises en el 3er. continente: " 
                + Continentes.ASIA.getPaises());
        System.out.println("No. de habitantes en el 3er. continente: " 
                + Continentes.ASIA.getHabitantes());


        // Oceanía
        System.out.println("Continente No.5: " + Continentes.OCEANIA);
        System.out.println("No. de paises en el 5to. continente: " 
                + Continentes.OCEANIA.getPaises());
        System.out.println("No. de habitantes en el 5to. continente: " 
                + Continentes.OCEANIA.getHabitantes());
    }
    //Video 4 parte 1: Pruebas de enum, con la creación de enum Continentes
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            //Tarea: Agregar todos los dias de la semana
            //Tambien hay que agregar el default en el switch
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            //case DOMINGO:
               // System.out.println("Septimo dia de la semana");
               // break;
                
            default:
                //Se ejecutará si por alguna razón el valor no es ninguno de los anteriores
                System.out.println("Día no válido o no encontrado.");
                break;
        }
    }
}
