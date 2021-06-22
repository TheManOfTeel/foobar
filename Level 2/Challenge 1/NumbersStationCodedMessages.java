public class NumbersStationCodedMessages {
    public static int[] solution(int[] l, int t) {
        int[] arr = new int[2];
        int i, j, sum = 0;
        for (i = 0; i < l.length; i++) {
            for (j = i; j < l.length; j++) {
                sum += l[j];
                if (sum == t) {
                    arr[0] = i;
                    arr[1] = j;
                    return arr;
                }
            }
            sum = 0;
        }
        arr[0] = -1;
        arr[1] = -1;
        return arr;
    }
}
