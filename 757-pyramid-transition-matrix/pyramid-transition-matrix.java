class Solution {
    //Aryan

    private boolean DFS(String row, Map<String, List<Character>> map, Map<String,Boolean> memo){
        if (memo.containsKey(row))
            return memo.get(row);
            if (row.length() == 1){
                memo.put(row, true);
                return true;
            }
        int n = row.length();
        for (int i = 0; i < n - 1; i++){
            if (!map.containsKey(row.substring(i, i + 2))){
                memo.put(row, false);
                return false;
            }
        }
        boolean res = buildNext(row, 0, new StringBuilder(), map, memo);
        memo.put(row, res);
        return res;
    }
    private boolean buildNext(String row, int i, StringBuilder curr,  Map<String, List<Character>> map, Map<String, Boolean> memo){
        if (i == row.length() - 1){
            return DFS(curr.toString(), map, memo);
        }
        String pair = row.substring(i, i + 2);
        for (char c : map.get(pair)){
            curr.append(c);
            if (buildNext(row, i + 1, curr, map, memo)){
                return true;
            }
            curr.deleteCharAt(curr.length() - 1);
        }
        return false;
    }
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        Map<String, List<Character>> map = new HashMap<>();
        for (String t : allowed){
            String key = t.substring(0, 2);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(t.charAt(2));
        }
        Map<String, Boolean> memo = new HashMap<>();
        return DFS(bottom, map, memo);
    }

}