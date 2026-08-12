class MinStack {
    Stack<Integer[]> stack;
    int minNum;
    public MinStack() {
        stack = new Stack();
        minNum = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        if(!stack.isEmpty()) {
            if(val < stack.peek()[1]) {
                minNum = val;
            }
            else{
                minNum = stack.peek()[1];
            }
        }
        else {
            minNum = val;
        }
        System.out.println(minNum);
        stack.add(new Integer[]{val,minNum});
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek()[0];
    }
    
    public int getMin() {
        return stack.peek()[1];
    }
}
