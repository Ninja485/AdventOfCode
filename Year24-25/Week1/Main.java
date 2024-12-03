import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> firstArray = new ArrayList<>(Arrays.asList(3,4,2,1,3,3));
        ArrayList<Integer> secondArray = new ArrayList<>(Arrays.asList(4,3,5,3,9,3));
        System.out.println(Week1.day1Problem(firstArray, secondArray));
    }
}
