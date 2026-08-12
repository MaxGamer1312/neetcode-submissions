class Solution {
    public int maxArea(int[] heights) {
        int maxArea = 0;
        for(int i = 0; i < heights.length-1; i++) {
            int totalArea = 0;
            for(int j = i+1; j < heights.length; j++) {
                totalArea = Math.min(heights[i],heights[j]) * (j-i);
                if(totalArea > maxArea) {
                    maxArea = totalArea;
                }
            }
            
            System.out.println(totalArea);
        }
        return maxArea;
    }
}
