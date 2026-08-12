class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        ArrayList<Integer> currMaxTemp = new ArrayList();
        currMaxTemp.add(temperatures.length-1);
        result[temperatures.length-1] = 0;
        for(int i = temperatures.length-1; i >= 0; i--) {
            System.out.println(currMaxTemp);
            int j = currMaxTemp.size()-1;
            while(j > 0 && temperatures[i] >= temperatures[currMaxTemp.get(j)]) {
                j--;
            }
            if(temperatures[i] >= temperatures[currMaxTemp.get(j)]) {
                result[i] = 0;
            } else {
                result[i] = currMaxTemp.get(j)-i;
            }
            if(i > 0 && temperatures[i] >= temperatures[i-1]) {
                currMaxTemp.add(i);
            }

        }
        return result;
    }
}
