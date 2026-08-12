class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numsList = new HashSet<>();
        HashMap<Integer, Set<Integer>> map = new HashMap<>();
        int cCount = 0;
        for(int i = 0; i < nums.length; i++) {
            numsList.add(nums[i]);
        }
        int i = 0;
        while(!numsList.isEmpty()) {
            int j = 0;
            while(numsList.contains(nums[i]+j)) {
                map.computeIfAbsent(nums[i], k -> new HashSet<>()).add(nums[i]+j);
                numsList.remove(nums[i] + j);
                j++;
            }
            //
            j = 1;
            while(numsList.contains(nums[i]-j)) {
                System.out.println(numsList);
                System.out.println(map);
                map.get(nums[i]).add(nums[i]-j);
                numsList.remove(nums[i] - j);
                j++;
            }
            if(map.get(nums[i]) != null && map.get(nums[i]).size() > cCount) {
                cCount = map.get(nums[i]).size();
            }
            i++;
        }
        return cCount;
    }
}
