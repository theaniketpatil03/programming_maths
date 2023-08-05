from loguru import logger


class Matrix:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        logger.info(f'" {rows}x{cols} null matrix created "' )


    def __str__(self):
        # for row in self.data:
        #     print([map(str,row)])
        # for row in self.data:
        #     print(list(map(str, row)))
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    def set_element(self,row,col,value):
        self.data[row][col] = value

    def get_element(self,row,col):
        return self.data[row][col]

    def add(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must be the same for addition.")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_element(i,j,self.get_element(i,j) + other.get_element(i,j))

        return result

    def scalar_multiply(self,scalar):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_element(i,j,self.get_element(i,j)*scalar)

        return result

test = Matrix(3,6)
# print(test)

test.set_element(0,0,1)
print(test)