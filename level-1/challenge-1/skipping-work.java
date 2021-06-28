import java.util.stream.IntStream;

public class SkippingWork {
    public static int solution(int[] x, int[] y) {
        for (int numberToMatch : x) {
            boolean contains = IntStream.of(y).anyMatch(j -> j == numberToMatch);
            if (!contains) {
                return numberToMatch;
            }
        }

        for (int numberToMatch : y) {
            boolean contains = IntStream.of(x).anyMatch(j -> j == numberToMatch);
            if (!contains) {
                return numberToMatch;
            }
        }

        return 0;
    }
}
