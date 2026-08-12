class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> map = new HashMap<>();
        if(s.length() != t.length()) {
            return false;
        }
        for(int i = 0; i < s.length(); i++) {
            if(map.get(s.charAt(i)) != null) {
                map.put(s.charAt(i),map.get(s.charAt(i))+1);
            }
            else {
                map.put(s.charAt(i),1);
            }
        }
        System.out.println(map);
        for(int i = 0; i < t.length(); i++) {
            if(map.get(t.charAt(i)) != null) {
                map.put(t.charAt(i),map.get(t.charAt(i))-1);
            }
            else{
                System.out.println("hi");
                return false;
            }
            if(map.get(t.charAt(i)) == 0) {
                map.remove(t.charAt(i));
            }
        }
        if(map.isEmpty()) {
            return true;
        }
        return false;
    }
}
