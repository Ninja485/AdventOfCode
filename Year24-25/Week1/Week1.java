import java.util.ArrayList;
import java.util.Collections;

public class Week1 {
    public static int day1Problem(ArrayList<Integer> firstList, ArrayList<Integer> secondList) {
        int result = 0;
        Integer minFirst,minSecond;
        while(!firstList.isEmpty()){
            minFirst = Collections.min(firstList);
            minSecond = Collections.min(secondList);
            result += Math.abs(minFirst - minSecond);
            firstList.remove(minFirst);
            System.out.println(firstList);
            secondList.remove(minSecond);
            System.out.println(secondList);
        }
        return result;
    }
}