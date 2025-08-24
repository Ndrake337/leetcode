import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> vectorAnl = new HashMap<Integer, Integer>();
        int[] returnArray = new int[2];
        for(int i = 0; i< nums.length; i++){
            int value = target - nums[i];
            for(int j : vectorAnl.keySet()){
                if(vectorAnl.get(j) == value){
                    returnArray[0] = j;
                    returnArray[1] = i;
                    return returnArray;
                }
            }
            vectorAnl.put(i,nums[i]);

        }
        return returnArray;
    }
}