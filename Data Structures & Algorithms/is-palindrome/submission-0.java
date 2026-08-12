class Solution {
    public boolean isPalindrome(String s) {
        String alphaNumS = s.replaceAll("\\p{Punct}", "").toLowerCase();
        alphaNumS = alphaNumS.replaceAll(" ", "");
        int i = 0;
        int j = alphaNumS.length()-1;
        while(j >= i) {
            if(alphaNumS.charAt(i) != alphaNumS.charAt(j)) {
                System.out.println(alphaNumS.charAt(i));
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
