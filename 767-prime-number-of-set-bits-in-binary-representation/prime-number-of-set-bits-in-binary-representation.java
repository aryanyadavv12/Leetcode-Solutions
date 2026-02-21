import java.util.*;

class Solution {
    //Aryan
    public boolean hasPrimeSetBits(int n) {
        Set<Integer> primes = new HashSet<>(
            Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19)
        );

        int setBits = 0;
        for (int i = 0; i < 20; i++) {
            if ((n & (1 << i)) != 0) {
                setBits++;
            }
        }

        return primes.contains(setBits);
    }

    public int countPrimeSetBits(int left, int right) {
        int ans = 0;
        for (int i = left; i <= right; i++) {
            if (hasPrimeSetBits(i)) {
                ans++;
            }
        }
        return ans;
    }
}