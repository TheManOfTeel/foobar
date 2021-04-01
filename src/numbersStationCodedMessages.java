import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.IntStream;

public class numbersStationCodedMessages {
    public static int[] solution(int[] l, int t) {
        Matches.MatchList = new ArrayList<>();
        Matches.MatchList.add(new int[]{-1, -1});
        Integer[] numbers = Arrays.stream(l).boxed().toArray(Integer[]::new);
        sum_up_recursive(new ArrayList<>(Arrays.asList(numbers)), t, new ArrayList<>());
        return GetIndex(l);
    }

    static void sum_up_recursive(ArrayList<Integer> numbers, int target, ArrayList<Integer> partial) {
        int s = 0;
        for (int x: partial) {
            s += x;
        }
        if (s == target) {
            Matches.MatchList.remove(0);
            Matches.MatchList.add(partial.stream().mapToInt(i -> i).toArray());
        }
        if (s >= target) {
            return;
        }
        for(int i = 0; i < numbers.size(); i++) {
            ArrayList<Integer> remaining = new ArrayList<>();
            int n = numbers.get(i);
            for (int j = i + 1; j < numbers.size(); j++) {
                remaining.add(numbers.get(j));
            }
            ArrayList<Integer> partial_rec = new ArrayList<>(partial);
            partial_rec.add(n);
            sum_up_recursive(remaining, target, partial_rec);
        }
    }

    static int[] GetIndex(int[] l) {
        int[] winningCombo = Matches.MatchList.get(0);
        return new int[]
                {
                        IntStream.range(0, l.length).filter(i -> l[i] == winningCombo[0]).findFirst().orElse(-1),
                        IntStream.range(0, l.length).filter(i -> l[i] == winningCombo[1]).findFirst().orElse(-1)
                };
    }

    public static class Matches {
        public static ArrayList<int[]> MatchList;
    }
}
