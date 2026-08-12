class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<Character, Integer> frequencyMapCharacter = new HashMap<>();
        HashMap<HashMap<Character, Integer>, List<String>> frequencyMapString = new HashMap<>();
        List<List<String>> mainList = new ArrayList<>();
        for(int i = 0; i < strs.length; i++) {
            for(int j = 0; j < strs[i].length(); j++) {
                if(frequencyMapCharacter.containsKey(strs[i].charAt(j))) {
                    frequencyMapCharacter.put(strs[i].charAt(j), frequencyMapCharacter.get(strs[i].charAt(j))+1);
                }
                else {
                    frequencyMapCharacter.put(strs[i].charAt(j), 1);
                }
            }
            if(frequencyMapString.containsKey(frequencyMapCharacter)) {
                frequencyMapString.get(frequencyMapCharacter).add(strs[i]);
            }
            else {
                frequencyMapString.put(frequencyMapCharacter, new ArrayList<>(Arrays.asList(strs[i])));
            }
            frequencyMapCharacter = new HashMap<>();
        }
        for(List<String> combination: frequencyMapString.values()) {
            mainList.add(combination);
        }
        return mainList;
    }
}
