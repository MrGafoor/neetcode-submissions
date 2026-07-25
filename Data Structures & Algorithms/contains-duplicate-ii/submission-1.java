
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> windows=new HashSet<>();
        int l=0;
        for(int r=0;r<nums.length;r++){
            if ((r-l)>k){
                windows.remove(nums[l]);
                l+=1;
            }
            if (windows.contains(nums[r])){
                return true;
            }
            windows.add(nums[r]);

        }
    return false;
    }
}