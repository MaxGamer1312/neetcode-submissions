class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        for(int i = 0; i < nums.length-1; i++) {
            for(int j = nums.length-1; j > i; j--) {
                for(int r = i+1; r < j; r++) {
                    if(nums[i] + nums[j] == -nums[r]) {
                        ArrayList<Integer> tempResult = new ArrayList<>();
                        tempResult.add(nums[i]);
                        tempResult.add(nums[j]);
                        tempResult.add(nums[r]);
                        Collections.sort(tempResult);
                        if(!result.contains(tempResult)) {
                            result.add(tempResult);
                        }
                    }
                }
            }
        }

        return result;
    }
}
