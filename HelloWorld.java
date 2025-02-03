// A well-structured Java program to introduce coding style
public class HelloWorld {

    // Main method: The entry point of the program
    public static void main(String[] args) {
        // Print a greeting message
        greetUser("Welcome to the world of Java coding!");
        
        // Perform a simple calculation
        int result = addNumbers(10, 20);
        System.out.println("The sum of 10 and 20 is: " + result);
    }

    // Method to print a greeting message
    public static void greetUser(String message) {
        System.out.println(message);
    }

    // Method to add two numbers and return the result
    public static int addNumbers(int a, int b) {
        return a + b;
    }
}

