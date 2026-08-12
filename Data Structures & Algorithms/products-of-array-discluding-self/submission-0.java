class Solution {
    public int[] productExceptSelf(int[] nums) {
        int sizeOfList = nums.length;
        int[] mainList = new int[sizeOfList];
        for(int i = 0; i < sizeOfList; i++) {
            mainList[i] = 1;
            for(int j = 1; j <= sizeOfList-1; j++) {
                mainList[i] *= nums[(i+j)%(sizeOfList)];
            }
        }
        return mainList;
    }
}  
