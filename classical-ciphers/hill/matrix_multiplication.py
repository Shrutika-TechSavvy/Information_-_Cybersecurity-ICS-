
def matrix_multiply(A, B):
    #Number of rows and coulumns
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    #Check if multiplication of matrix is possible
    if cols_A != rows_B :
        raise ValueError("MAtrix multiplication is not possible...")
    
    #creating the result matrix filled with 0's
    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            row.append(0)
        result.append(row)
    
    #multiplying the matrix
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j]  =  result[i][j] + A[i][k] * B[k][j]
                
    return result

