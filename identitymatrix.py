# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

def is_identity_matrix(lp):
    #Write your code here
    l = len(lp)
    if l == 0:
        return True

    p = len(lp[0])
    if l != p:
        return False
    else:
        i, k = 0, 0
        while i < l:
            if lp[i][k] == 1:
                i = i + 1
                k = k + 1
            else:
                return False
#        return True

        i, k = 0, 0

        while k < l:
            count = 0
            while i < l:
#                print k, i, lp[k][i]
                if lp[k][i] > 0:
                    i = i + 1
                    count = count + 1
                else:
                    i = i + 1
#            print count
            if count > 1:
                return False
            k = k + 1
            i = 0

        return True

# Test Cases:
# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,1],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False