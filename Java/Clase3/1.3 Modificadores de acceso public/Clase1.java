public class Clase1 {
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor atributo protected";

    public Clase1(){
        System.out.println("Constructor public");
    }

    public Clase1(String tipo){
        System.out.println("Constructor " + tipo);
    }

    public void metodoPublico(){
        System.out.println("Método public");
    }
}
