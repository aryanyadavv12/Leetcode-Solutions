class Solution {
    public int findGCD(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i:nums){
            if(i>max){
                max=i;
            }
            if(i<min){
                min=i;
            }
        }
        int gcd = 1;
        for (int i=1;i<=min;i++){
            if((min%i==0) && (max%i==0))
                gcd=i;
            
        
        }return gcd;
    }
}