package domain;

public class Gerente extends Empleado {

    private String departamento;

    public Gerente(String nombre, double sueldo, String departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }

    @Override
    public String obtenerDetalles() {
        return super.obtenerDetalles() + ", Departamento: " + departamento;
    }

    @Override
    public String toString() {
        return "Gerente{" + "departamento=" + departamento + '}' + super.toString();
    }

    public String getDepartamento() {
        return departamento;
    }
}
