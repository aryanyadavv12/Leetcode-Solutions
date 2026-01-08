class Solution {
    //Aryan
    private int m , n;
    int[][] memo;
    public int maxDotProduct(int[] nums1, int[] nums2) {
        m = nums1.length;
        n = nums2.length;

        memo = new int[m][n];
        for(int[] mem : memo){
            Arrays.fill(mem, -100000000);
        }

        return solve(nums1, nums2, 0, 0);
    }

    private int solve(int[] nums1, int[] nums2, int i, int j){
        if(i >= m || j >= n) return -100000000;
        if(memo[i][j] != -100000000) return memo[i][j];

        int product = nums1[i] * nums2[j];

        memo[i][j] = Math.max(product, Math.max(product + solve(nums1, nums2, i+1, j+1), Math.max(solve(nums1, nums2, i, j+1), solve(nums1, nums2, i+1, j))));
        
        return memo[i][j];
    }
}