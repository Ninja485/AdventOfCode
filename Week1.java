import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class Week1 {
    public int day1Problem(ArrayList<Integer> firstList, ArrayList<Integer> secondList) {
        int result = 0;
        int minFirst,minSecond;
        for (int i = 0; i < firstList.size(); i++) {
            minFirst = Collections.min(firstList);
            minSecond = Collections.min(secondList);
            result += Math.abs(minFirst - minSecond);
            firstList.remove(minFirst);
            secondList.remove(minSecond);
        }
        return result;
    }
}
