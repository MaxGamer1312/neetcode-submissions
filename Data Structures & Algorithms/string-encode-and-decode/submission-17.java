class Solution {

    public String encode(List<String> strs) {
        if(strs.isEmpty()) {
            return "EMPTY";
        }
        String encodedInfo = String.valueOf(strs.get(0).length()) + "#" + strs.get(0);
        if(strs.size() > 1) {
            for(int i = 1 ; i < strs.size(); i++) {
                encodedInfo += strs.get(i).length() + "#" + strs.get(i);
            }
        }
        return encodedInfo;
    }

    public List<String> decode(String str) {
        System.out.println(str);
        if(str.equals("EMPTY")) {
            return new ArrayList<String>();
        }
        ArrayList<String> mainList = new ArrayList<>();
        int i = 0;
        int num = 0;
        while(i < str.length()) {
            num = Integer.valueOf(str.substring(i, str.indexOf("#",i)));
            System.out.println(String.valueOf(num).length());
            mainList.add(str.substring(i + 1 + String.valueOf(num).length(),i + 1 + String.valueOf(num).length() + num));
            i += num + 1 + String.valueOf(num).length();
        }
        return mainList;
    }
}
