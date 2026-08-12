class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> mapOfParen = new HashMap<>();
        mapOfParen.put('(', ')');
        mapOfParen.put('[', ']');
        mapOfParen.put('{', '}');
        Deque<Character> stack = new ArrayDeque<>();
        for(int i = 0; i < s.length(); i++) {
            Character target = s.charAt(i);
            if(mapOfParen.containsKey(target)) {
                stack.add(target);
            }
            else {
                if(target.equals(mapOfParen.get(stack.peekLast()))) {
                    stack.removeLast();
                }
                else {
                    return false;
                }
            }
        }
        if(stack.isEmpty()) {
            return true;
        }
        return false;
 }
}
