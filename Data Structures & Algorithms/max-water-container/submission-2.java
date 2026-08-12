class Solution {
    public int maxArea(int[] heights) {
        int i = 0;
        int j = heights.length - 1; 
        int totalArea = 0;
        while(i<j) {
            int currentArea = Math.min(heights[i], heights[j]) * (j-i);
            if(totalArea < currentArea){
                totalArea = currentArea;
            }
            if(heights[i] > heights[j]) {
                j--;
            }
            else{
                i++;
            }
        }
        return totalArea;
        //Basic Solution
        // int maxArea = 0;
        // for(int i = 0; i < heights.length-1; i++) {
        //     int totalArea = 0;
        //     for(int j = i+1; j < heights.length; j++) {
        //         totalArea = Math.min(heights[i],heights[j]) * (j-i);
        //         if(totalArea > maxArea) {
        //             maxArea = totalArea;
        //         }
        //     }
            
        // }
        // return maxArea;
    }
}
