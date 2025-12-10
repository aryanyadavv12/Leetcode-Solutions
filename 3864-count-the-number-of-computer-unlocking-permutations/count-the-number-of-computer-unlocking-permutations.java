class Solution {
    public int countPermutations(int[] complexity) {
        int n = complexity.length;
        final int mod = 1000000007;
        for (int i = 1; i < n; i++){
            if (complexity[i] <= complexity[0]){
                return 0;
            }
        }
        long res = 1;
        for (int i = 1; i < n; i++){
            res = (res * i) % mod;
        }
        return (int)res;
    }
}