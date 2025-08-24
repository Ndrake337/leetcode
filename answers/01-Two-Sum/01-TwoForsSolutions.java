class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int[] returnArray = new int[2];
        boolean valid = true;
        while (valid) {
            for(int j = i + 1; j < nums.length; j++){
                int sum = nums[i] + nums[j];
                if(sum == target){
                    valid = false;
                    returnArray[0] = i;
                    returnArray[1] = j;
                    break;
                }
            }
            i++;
        }
        return returnArray;
    }
}