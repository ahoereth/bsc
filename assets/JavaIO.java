import java.util.Scanner;
public class JavaIO {
  public static void main(String[] argv) {
    Scanner in = new Scanner(System.in);
    System.out.print("Your name: ");
    String name = in.nextLine();
    System.out.println("Hello " + name);
  }
}
