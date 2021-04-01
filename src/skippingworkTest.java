import org.junit.jupiter.api.Test;

class skippingworkTest {
    int[] x = {13, 5, 6, 2, 5};
    int[] y = {5, 2, 5, 13};

    @Test
    void solution() {
        System.out.print(skippingwork.solution(new int[]{14, 27, 1, 4, 2, 50, 3, 1}, new int[]{2, 4, -4, 3, 1, 1, 14, 27, 50}));
    }
}