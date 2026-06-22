
package mundopc;

import ar.com.system2023.mundopc.*;

public class mundoPC {
    public static void main(String[] args) {

       
        Monitor monitorHP = new Monitor("HP", 13);
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");//Importar la clase
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadora1 = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);

        //Creamos otros objetos de diferente marca
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadora2 = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);

        //Orden1 hasta 10
        Computadora computadora3 = new Computadora("Computadora Samsung",
                new Monitor("Samsung", 32), new Teclado("USB", "Samsung"), new Raton("USB", "Samsung"));

        Computadora computadora4 = new Computadora("Computadora Razer",
                new Monitor("Razer", 27), new Teclado("Bluetooth", "Razer"), new Raton("Bluetooth", "Razer"));

        Computadora computadora5 = new Computadora("Computadora Dell",
                new Monitor("Dell", 29), new Teclado("USB", "Dell"), new Raton("USB", "Dell"));

        Computadora computadora6 = new Computadora("Computadora Acer",
                new Monitor("Acer", 21), new Teclado("Bluetooth", "Acer"), new Raton("Bluetooth", "Acer"));

        Computadora computadora7 = new Computadora("Computadora Lenovo",
                new Monitor("Lenovo", 27), new Teclado("Bluetooth", "Lenovo"), new Raton("Bluetooth", "Lenovo"));

        Computadora computadora8 = new Computadora("Computadora Gigabyte",
                new Monitor("Gigabyte", 27), new Teclado("Bluetooth", "Gigabyte"), new Raton("Bluetooth", "Gigabyte"));

        Computadora computadora9 = new Computadora("Computadora Apple",
                new Monitor("Apple", 24), new Teclado("Bluetooth", "Apple"), new Raton("Bluetooth", "Apple"));

        Computadora computadora10 = new Computadora("Computadora MSI",
                new Monitor("MSI", 27), new Teclado("Bluetooth", "MSI"), new Raton("Bluetooth", "MSI"));

        // Inicializamos ordenes
        Orden orden1 = new Orden();
        Orden orden2 = new Orden();

        orden1.agregarComputadora(computadora1);
        orden1.agregarComputadora(computadora2);
        orden1.agregarComputadora(computadora3);
        orden1.agregarComputadora(computadora4);
        orden1.agregarComputadora(computadora5);
        orden1.agregarComputadora(computadora6);
        orden1.agregarComputadora(computadora7);
        orden1.agregarComputadora(computadora8);
        orden1.agregarComputadora(computadora9);
        orden1.agregarComputadora(computadora10);

        // Computadora para orden2
        Computadora computadorasVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonHP);
        orden2.agregarComputadora(computadorasVarias);

        orden1.mostrarOrden();
        orden2.mostrarOrden();

    }
}
