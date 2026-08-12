class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < tokens.length; i++) {
            if(tokens[i].equals("*")) {
                stack.add(stack.pop()*stack.pop());
            }
            else if(tokens[i].equals("/")) {
                int temp = stack.pop();
                stack.add(stack.pop()/temp);
            }
            else if(tokens[i].equals("+")) {
                stack.add(stack.pop()+stack.pop());
            }
            else if(tokens[i].equals("-")) {
                stack.add(-stack.pop()+stack.pop());
            }
            else {
                stack.add(Integer.parseInt(tokens[i]));
            }
        }
        return stack.peek();
    }
}
