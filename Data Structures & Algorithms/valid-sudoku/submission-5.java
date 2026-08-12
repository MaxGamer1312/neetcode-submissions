// class Solution {
//     public boolean isValidSudoku(char[][] board) {
//         HashMap<Integer,ArrayList<Integer>> rowMap = new HashMap<>();
//         HashMap<Integer,ArrayList<Integer>> columnMap = new HashMap<>();
//         HashMap<ArrayList<Integer>,ArrayList<Integer>> matrixMap = new HashMap<>();
//         for(int i = 0; i < board.length; i++) {
//             rowMap.put(i, new ArrayList<Integer>());
//             for(int j = 0; j < board[i].length; j++) {
//                 ArrayList<Integer> matrixNum = new ArrayList<>();;
//                 matrixNum.add((int)(j/3));
//                 matrixNum.add((int)(i/3));
//                 if(board[i][j] == '.') {
//                     continue;
//                 }
//                 int target = Character.getNumericValue(board[i][j]);
//                 if(columnMap.get(j) == null) {
//                     columnMap.put(j, new ArrayList<Integer>());
//                 }
//                 if(matrixMap.get(matrixNum) == null) {
//                     matrixMap.put(matrixNum, new ArrayList<Integer>());
//                 }
//                 if(rowMap.get(i).contains(target)) {
//                     return false;
//                 }
//                 if(columnMap.get(j).contains(target) ) {
//                     return false;
//                 }
//                 if(matrixMap.get(matrixNum).contains(target) ) {
//                     return false;
//                 }
//                 rowMap.get(i).add(target);
//                 columnMap.get(j).add(target);
//                 matrixMap.get(matrixNum).add(target);
//             }
//         }
//         return true;
//     }

    
// }

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> squares = new HashMap<>();  // key = (r / 3) * 3 + c / 3

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char cell = board[r][c];
                if (cell == '.') {
                    continue;
                }
                // Use computeIfAbsent directly inside the if statement
                if (!rows.computeIfAbsent(r, k -> new HashSet<>()).add(cell)
                    || !cols.computeIfAbsent(c, k -> new HashSet<>()).add(cell)
                    || !squares.computeIfAbsent((r / 3) * 3 + c / 3, k -> new HashSet<>()).add(cell)) {
                    return false;
                }
            }
        }
        return true;
    }
}
