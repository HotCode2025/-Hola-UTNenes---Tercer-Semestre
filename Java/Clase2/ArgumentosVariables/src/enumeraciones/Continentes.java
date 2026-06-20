package enumeraciones;

/**
 *
 * @author Sere Olmedo
 */
public enum Continentes {
    AFRICA(54, "1.2 billones"),
    EUROPA(50, "1.1 billones"),
    ASIA(49, "1.9 millones"),
    AMERICA(35, "150.2 millones"),
    OCEANIA(14, "1.2 billones");

    private final int paises;
    private final String habitantes;

    // Constructor con los dos parámetros bien definidos
    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }

    // Método Get para países
    public int getPaises() {
        return this.paises;
    }
    
    // Método Get para habitantes 
    public String getHabitantes() {
        return this.habitantes;
    }
}