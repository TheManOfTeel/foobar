import org.junit.jupiter.api.Test;

import java.util.Arrays;

class skippingworkTest {
    @Test
    void solution() {
        int[] x = new int[]{1, 2, 3, 4};
        // System.out.print(skippingwork.solution(new int[]{14, 27, 1, 4, 2, 50, 3, 1}, new int[]{2, 4, -4, 3, 1, 1, 14, 27, 50}));
        // numbersStationCodedMessages.solution(x, 12);
        System.out.print(Arrays.toString(numbersStationCodedMessages.solution(x, 15)));
    }
}