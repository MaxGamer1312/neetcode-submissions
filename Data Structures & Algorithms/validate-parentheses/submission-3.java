class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> mapOfParen = new HashMap<>();
        mapOfParen.put('(', ')');
        mapOfParen.put('[', ']');
        mapOfParen.put('{', '}');
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            Character target = s.charAt(i);
            if(mapOfParen.containsKey(target)) {
                stack.add(target);
            }
            else {
                if(!stack.isEmpty() && target.equals(mapOfParen.get(stack.peek()))) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
 }
}
