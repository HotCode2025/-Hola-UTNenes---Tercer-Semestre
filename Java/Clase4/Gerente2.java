package domain;

public class Gerente2 extends Empleado{
    private final String departamento;

    public Gerente2(String nombre, double sueldo, String departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }

    //Sobreescribimos el metodo
    @Override
    public String obtenerDetalles() {
        return super.obtenerDetalles()+", Departamento: "+this.departamento;
    }
}