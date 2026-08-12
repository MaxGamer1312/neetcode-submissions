class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new Stack();
        int open = 0;
        int closed = 0;
        backtrackingRecur(result,"",0,0,n);
        return result;
    }
    public String backtrackingRecur(List<String> result, String partialResult, int open, int closed, int n) {
        if(open == n && open == closed) {
            result.add(partialResult);
        }
        if(open < n) {
            backtrackingRecur(result, partialResult + "(", open + 1, closed,n);
        }
        if(closed < open) {
            backtrackingRecur(result, partialResult + ")", open, closed + 1,n);
        }
        return partialResult;
    }
}
