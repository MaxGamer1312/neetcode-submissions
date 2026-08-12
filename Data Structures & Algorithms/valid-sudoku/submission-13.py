class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictBox = {}
        dictCol = {}
        
        for irow in range(len(board)):
            setRow = set()
            #print(dictCol)
            for icol in range(len(board)):
                
                ibox = icol//3
                element = board[irow][icol]
                

                if element in setRow:
                    return False
                else:
                    if(element.isdigit()):
                        setRow.add(element)
                if icol not in dictCol:
                    dictCol[icol] = set()

                setCol = dictCol[icol]
                print((icol,irow))
                print(setCol)
                print(element)
                if element in setCol:
                    return False
                else:
                    if(element.isdigit()):
                        setCol.add(element)
                    
                if(ibox not in dictBox or dictBox[ibox][0] == 9):
                    dictBox[ibox] = [0,set()]
                dictBox[ibox][0] += 1
                if(element.isdigit()):
                    prev = len(dictBox[ibox][1])
                    dictBox[ibox][1].add(element)
                    if(prev == len(dictBox[ibox][1])):
                        print("hi")
                        return False
                
        return True

                
