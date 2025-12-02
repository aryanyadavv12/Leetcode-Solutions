class Solution {
    int MOD = (int)1e9+7;
    public int countTrapezoids(int[][] points) {
        Map<Integer,List<Integer>> map=new HashMap<>();
        for(int point[]:points){
            int a=point[0];
            int b=point[1];
            map.putIfAbsent(b,new ArrayList<>());
            map.get(b).add(a);
        }
        long sum=0,total=0;
        for(int num:map.keySet()){
            long s = (long)map.get(num).size();
            total+=(s*(s-1)/2);
        }
        long ans=0;
        for(int num:map.keySet()){
            long s = (long)map.get(num).size();
            long curr=(long)(s*(s-1)/2);
            total-=curr;
            ans=ans+(curr*total)%MOD;
            ans%=MOD;
        }
        return (int)ans;
    }
}