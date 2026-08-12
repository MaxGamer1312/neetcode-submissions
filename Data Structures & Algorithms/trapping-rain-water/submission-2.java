class Solution {
    public int trap(int[] height) {
        if(height.length == 1) {
            return 0;
        }
        int L = 0;
        int R = height.length - 1;
        int totalArea = 0;
        int maxNum = 0;
        while(L < R) {
            int currMinNum = Math.min(height[L],height[R]);
            int currMaxNum = Math.max(height[L],height[R]);
            System.out.println(maxNum * (R-L));
            if(currMinNum >= maxNum) {
                totalArea += (currMinNum * (R-L) - maxNum * (R-L));
                maxNum = currMinNum;
            }
            if(height[R] > height[L]) {
                totalArea-=height[L];
                L++;
            }
            else {
                totalArea-=height[R];
                R--;
            }
        }
        return totalArea;
    }
}
