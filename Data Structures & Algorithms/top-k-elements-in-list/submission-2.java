class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, ArrayList<Integer>> frequencyMapList = new HashMap<>();
        HashMap<Integer, Integer> frequencyMapInteger = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++) {
            if(frequencyMapInteger.containsKey(nums[i])) {
                frequencyMapInteger.put(nums[i], frequencyMapInteger.get(nums[i]) + 1);
            }
            else {
                frequencyMapInteger.put(nums[i], 1);
            }
        }
        for(Integer element:frequencyMapInteger.keySet()) {
            if(frequencyMapList.containsKey(frequencyMapInteger.get(element))) {
                frequencyMapList.get(frequencyMapInteger.get(element)).add(element);
            }
            else {
                frequencyMapList.put(frequencyMapInteger.get(element),new ArrayList<Integer>());
                frequencyMapList.get(frequencyMapInteger.get(element)).add(element);
            }
        }
        int[] mainList = new int[frequencyMapInteger.size()];
        int index = 0;
        for(Integer element:frequencyMapList.keySet()) {
            for(Integer elementOfList:frequencyMapList.get(element)) {
                mainList[index] = elementOfList;
                index++;
            }
        }
        mainList = Arrays.copyOfRange(mainList, mainList.length-k, mainList.length);
        return mainList;
    }
}
