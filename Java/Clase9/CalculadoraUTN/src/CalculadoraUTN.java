import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        var entrada = new Scanner(System.in);
        while(true){
            System.out.println("************ Aplicacion Calculadora *****************");
            mostrarMenu();
            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {

                    var resultado = ejecutarOperacion(operacion, entrada);


                    System.out.println("Resultado = " + resultado);

                } else if (operacion == 5) {
                    System.out.println("Saliendo...");
                    break;
                } else {
                    System.out.println("Opcion invalida");
                }
                }catch(NumberFormatException e){
                    System.out.println("Ocurrio un error: " + e.getMessage());
                    System.out.println("Error: ingrese solo numeros enteros de 1 a 5");
                }catch(ArithmeticException e){
                    System.out.println("Error: " + e.getMessage());
                }

            // Fin try
            //Imprimimos salto de linea
            System.out.println();
        } // Fin ciclo while
    } // Fin main
    private static void mostrarMenu(){
        //Mostramos el menu
        System.out.print("""
                1.  Suma
                2.  Resta
                3.  Multiplicacion
                4.  Division
                5.  Salir
                """);
        System.out.print("Operacion a realizar: ");
    } // Fin metodo mostrarMenu
    private static double ejecutarOperacion(int operacion , Scanner entrada){
        System.out.print("Ingrese el primer valor: ");
        var operando1 = Integer.parseInt(entrada.nextLine());
        System.out.print("Ingrese el segundo valor: ");
        var operando2 = Integer.parseInt(entrada.nextLine());

            return switch (operacion) {
                case 1 -> operando1 + operando2;
                case 2 -> operando1 - operando2;
                case 3 -> operando1 * operando2;
                case 4 -> (double) operando1 / operando2;
                default -> throw new IllegalStateException("Operacion inesperada: " + operacion);
            };
    }//Fin metodo ejecutarOperacion
}// Fin clase


