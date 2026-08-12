class Solution {
    public int[] productExceptSelf(int[] nums) {
        int sizeOfList = nums.length;
        int[] mainList = new int[sizeOfList];
        int[] preList = new int[sizeOfList];
        int[] postList = new int[sizeOfList];
        postList[sizeOfList-1] = 1;
        preList[0] = 1;
        for(int i = 1; i < sizeOfList; i++) {
            postList[sizeOfList-i-1] = nums[sizeOfList-i] * postList[sizeOfList-i];
        }
        for(int i = 1; i < sizeOfList; i++) {
            preList[i] = nums[i-1] * preList[i-1];
            mainList[i] = preList[i] * postList[i];
        }
        mainList[0] = preList[0] * postList[0];
        System.out.println(preList);
        return mainList;
        //Sliding approach
        // int sizeOfList = nums.length;
        // int[] mainList = new int[sizeOfList];
        // for(int i = 0; i < sizeOfList; i++) {
        //     mainList[i] = 1;
        //     for(int j = 1; j <= sizeOfList-1; j++) {
        //         mainList[i] *= nums[(i+j)%(sizeOfList)];
        //     }
        // }
        // return mainList;
    }
}  
