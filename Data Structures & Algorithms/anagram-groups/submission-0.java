public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> res=new HashMap<>();
        for(String s:strs){
            char sorted[]=s.toCharArray();
            Arrays.sort(sorted);
            String key=new String(sorted);
            res.putIfAbsent(key,new ArrayList<>());
            res.get(key).add(s);

        }
        return new ArrayList<>(res.values());
    }
}