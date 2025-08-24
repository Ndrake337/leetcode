import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> vectorAnl = new HashMap<Integer, Integer>();
        int[] returnArray = new int[2];
        for(int i = 0; i< nums.length; i++){
            int value = target - nums[i];
            if(vectorAnl.containsKey(value)){
                return new int[]{vectorAnl.get(value), i};
            }
            vectorAnl.put(nums[i], i);

        }
        return returnArray;
    }
}