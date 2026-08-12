class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer,ArrayList<Integer>> rowMap = new HashMap<>();
        HashMap<Integer,ArrayList<Integer>> columnMap = new HashMap<>();
        HashMap<ArrayList<Integer>,ArrayList<Integer>> matrixMap = new HashMap<>();
        for(int i = 0; i < board.length; i++) {
            rowMap.put(i, new ArrayList<Integer>());
            for(int j = 0; j < board[i].length; j++) {
                ArrayList<Integer> matrixNum = new ArrayList<>();;
                matrixNum.add((int)(0.3*(j+1)));
                matrixNum.add((int)(0.3*(i+1)));
                if(board[i][j] == '.') {
                    continue;
                }
                int target = Character.getNumericValue(board[i][j]);
                if(columnMap.get(j) == null) {
                    columnMap.put(j, new ArrayList<Integer>());
                }
                if(matrixMap.get(matrixNum) == null) {
                    matrixMap.put(matrixNum, new ArrayList<Integer>());
                }
                if(rowMap.get(i).contains(target)) {
                    return false;
                }
                if(columnMap.get(j).contains(target) ) {
                    return false;
                }
                if(matrixMap.get(matrixNum).contains(target) ) {
                    return false;
                }
                rowMap.get(i).add(target);
                columnMap.get(j).add(target);
                matrixMap.get(matrixNum).add(target);
            }
        }
        return true;
    }
}
