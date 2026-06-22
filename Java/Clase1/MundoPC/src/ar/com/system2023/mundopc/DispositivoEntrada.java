// DispositivoEntrada
package ar.com.system2023.mundopc;

public class DispositivoEntrada {
    
    // Atributos
    private String marca;
    private String tipoEntrada;

    public DispositivoEntrada(String marca, String tipoEntrada) {
        this.marca = marca;
        this.tipoEntrada = tipoEntrada;
    }
// Getters y Setters
    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getTipoEntrada() {
        return tipoEntrada;
    }

    public void setTipoEntrada(String tipoEntrada) {
        this.tipoEntrada = tipoEntrada;
    }
// Metodo toString
    @Override
    public String toString() {
        return "DispositivoEntrada [marca=" + marca + ", tipoEntrada=" + tipoEntrada + "]";
    }

}