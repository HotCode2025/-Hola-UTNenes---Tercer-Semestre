package domain;

public class EjercicioInstanceOf1 extends Empleado{
    private String departamento;

    public EjercicioInstanceOf1(String nombre, double sueldo, String departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }

    //Sobreescribimos el metodo
    @Override
    public String obtenerDetalles() {
        return super.obtenerDetalles()+", Departamento: "+this.departamento;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }
}
