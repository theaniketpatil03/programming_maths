class AugmentedMatrix:
    def __init__(self,data) -> None:

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])


    def __str__(self):
        return '\n'.join([' '.join(map(str,row)) for row in self.data])

    def to_echelon_form(self):
        
        # First create a copy of the matrix
        matrix = [row[:] for row in self.data]

        num_rows = self.rows
        num_cols = self.cols


        # Initialize pivot row and pivot column
        pivot_row = 0
        pivot_col = 0

        while pivot_row < num_rows and pivot_col < num_cols -1 :
            # Find a nonzero pivot element in the current column
            print('here')
            if matrix[pivot_row][pivot_col] == 0:

                nonzero_found = False

                for i in range(pivot_row + 1, num_rows):
                    if matrix[i][pivot_col] != 0:
                        matrix[pivot_row], matrix[i] = matrix[i], matrix[pivot_row]
                        nonzero_found = True
                        break

                print('inside here')
                if not nonzero_found:
                    pivot_col += 1           
                    continue
            

            # Make the pivot element 1
            pivot = matrix[pivot_row][pivot_col]
            for j in range(pivot_col, num_cols):
                matrix[pivot_row][j] /= pivot


            # Eliminate other elements in the current column
            for i in range(pivot_row + 1, num_rows):
                factor = matrix[i][pivot_col]
                for j in range(pivot_col, num_cols):
                    matrix[i][j] -= factor * matrix[pivot_row][j]
            # Eli
            # else:
            #     print('breaking')


            pivot_row += 1
            pivot_col += 1
            # break

        print(AugmentedMatrix(matrix))


    
matrix = AugmentedMatrix([[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]])
matrix.to_echelon_form()
# print(matrix)