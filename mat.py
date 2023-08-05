from loguru import logger

class Matrix:
    def __init__(self, data) -> None:
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])


    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must be the same for addition.")

        result_data = []

        for i in range(self.rows):
            row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]

            result_data.append(row)

        return result_data
    
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

        result_data = []

        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                element = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(element)
            
            result_data.append(row)

        return result_data

    def reduce_to_echelon_form(self):
        
        # Create a copy of the matrix
        matrix = [row[:] for row in self.data]

        num_rows = self.rows
        num_cols = self.cols

        # Initialize pivot row and pivot column
        pivot_row = 0
        pivot_col = 0

        while pivot_row < num_rows and pivot_col < num_cols:
            # Find a nonzero pivot element in the current column
            if matrix[pivot_row][pivot_col] == 0:
                nonzero_found = False

                for i in range(pivot_row + 1, num_rows):
                    if matrix[i][pivot_col] != 0:
                        matrix[pivot_row], matrix[i] = matrix[i], matrix[pivot_row]
                        nonzero_found = True
                        break
                if not nonzero_found:
                    pivot_col += 1
                    continue

            # print(matrix)

            # Make the pivot element 1
            pivot = matrix[pivot_row][pivot_col]
            for j in range(pivot_col, num_cols):
                matrix[pivot_row][j] /= pivot

            # Eliminate other elements in the current column
            for i in range(pivot_row + 1, num_rows):
                factor = matrix[i][pivot_col]
                for j in range(pivot_col, num_cols):
                    matrix[i][j] -= factor * matrix[pivot_row][j]

            pivot_row += 1
            pivot_col += 1

        return Matrix(matrix)


matrix = Matrix([[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]])
result_echelon_form = matrix.reduce_to_echelon_form()
print("Given matrix:")
print(matrix)

print("Matrix in echelon form:")
print(result_echelon_form)
        

