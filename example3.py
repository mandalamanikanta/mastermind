import java.util.ArrayList;
import java.util.Scanner;

class Book {
    String name;

    Book(String name) {
        this.name = name;
    }
}

public class LibrarySystem {
    public static void main(String[] args) {
        ArrayList<Book> books = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("1. Add Book");
            System.out.println("2. View Books");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");

            int choice = sc.nextInt();
            sc.nextLine();

            if (choice == 1) {
                System.out.print("Enter book name: ");
                String name = sc.nextLine();
                books.add(new Book(name));
                System.out.println("Book added!\n");
            } 
            else if (choice == 2) {
                for (Book b : books) {
                    System.out.println("Book: " + b.name);
                }
                System.out.println();
            } 
            else if (choice == 3) {
                System.out.println("Exiting...");
                break;
            } 
            else {
                System.out.println("Invalid choice\n");
            }
        }
        sc.close();
    }
}
