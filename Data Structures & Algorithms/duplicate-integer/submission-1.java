class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        for(int i = 1; i < nums.length; i++) {
            if(nums[i-1]==nums[i]) {
                return true;
            }
        }
        return false;
        // BRUTE FORCE SOLUTION N^2, 1
        // for(int i = 0; i < nums.length; i++) {
        //     for(int j = i+1; j < nums.length;j++) {
        //         if(nums[i] == nums[j]) {
        //             return true;
        //         }
        //     }
        // }
        // return false;
    }
}
