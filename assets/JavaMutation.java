import java.util.ArrayList;
class JavaMutation {
  static final ArrayList<Integer> arr = new ArrayList<Integer>();
  static int take(ArrayList<Integer> arr, int key) {
    return arr.remove(key);
  }
  public static void main(String[] argv) {
    arr.add(1); arr.add(2);
    // arr: [1, 2]
    arr.set(0, 3);
    // arr: [3, 2]
    int got = take(arr, 1);
    // arr: [3], got: 2
  }
}


// Unveränderbare Daten sind genau das, was der Name sagt: Sie können nicht verändert werden. Der verbreitete Ansatz ist meist genau das Gegenteil, Datenstrukturen sind Instanzen von Objekten und Funktionen manipulieren diese direkt. In der Java-Klasse in Listing @lst:mutable_java werden zwei verschiedene dieser Veränderungen dargestellt: In Zeile 8, wird ein Wert der Klassenvariable `arr` direkt verändert mit eindeutigem Ergebnis. Zusätzlich wird in Zeile 10 `arr` an die Methode `take` übergeben, welche einen Wert entfernt und zurück gibt. Nur anhand des Methodenkopfes hätte man allerdings auch erwarten können, dass die übergebene Objekt nicht verändert wird. Dies könnte für hierauf folgenden Code zu unerwartetem Problemen führen.

// Interessant hierbei ist auch, dass die Klassenvariable `arr` als `final` definiert wurde. Eine so definierte Variable wird oft auch als Konstante bezeichnet, was bei angehenden Programmierer schnell für Verwirrung sorgen kann. `final` bedeutet hierbei nicht, dass der Wert unverändert bleibt, sondern die Referenz. Die Variable `arr` beinhaltet also garantiert immer eine Referenz auf das selbe Objekt, dieses Objekt kann allerdings verändert werden.
