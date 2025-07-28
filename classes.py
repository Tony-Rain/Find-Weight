class Matrix:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.matrix = args[0]
            self.colon = len(self.matrix[0])  # сначала столбцы потом строки
            self.row = len(self.matrix)
        else:
            self.row = args[0]  # колона
            self.colon = args[1]  # строка
            self.matrix = [[1 for _ in range(self.colon)] for _ in range(self.row)]

    def __eq__(self, other: 'Matrix') -> bool:
        if self.row == other.row and self.colon == other.colon:
            for i in range(self.row):
                for j in range(self.colon):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        else:
            raise Exception("Matrix cannot compare with other matrix")

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.row == other.row and self.colon == other.colon:
            matrix = []
            for i in range(self.row):
                vector = []
                for j in range(self.colon):
                    vector.append(self.matrix[i][j] + other.matrix[i][j])
                matrix.append(vector)
            return Matrix(matrix)
        else:
            raise Exception("Matrix cannot add other matrix")

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if self.row == other.row and self.colon == other.colon:
            matrix = []
            for i in range(self.row):
                vector = []
                for j in range(self.colon):
                    vector.append(self.matrix[i][j] - other.matrix[i][j])
                matrix.append(vector)
            return Matrix(matrix)
        else:
            raise Exception("Matrix cannot subtract other matrix")

    def __mul__(self, other: 'Matrix') -> 'Matrix':  # сначала строка одной матрицы потом столбец другой
        # height - row
        # weight - colon
        if self.colon != other.row:
            raise Exception("Matrix cannot multiply by other matrix")
        else:
            matrix = []
            for i in range(self.row):
                vector = []
                for j in range(other.colon):
                    count = 0
                    for k in range(self.colon):
                        count += self.matrix[i][k] * other.matrix[k][j]
                    vector.append(count)
                matrix.append(vector)
        return Matrix(matrix)

    def tranponate(self):
        matrix = []
        for i in range(self.colon):
            vector = []
            for j in range(self.row):
                vector.append(self.matrix[j][i])
            matrix.append(vector)
        self.matrix = matrix
        self.colon = len(self.matrix[0])
        self.row = len(self.matrix)
        # if type(self) is Vector:
        #     self = Matrix(self.matrix)
        return self

    def __str__(self):
        return str(self.matrix)


class Vector(Matrix):
    def __init__(self, *args):
        super().__init__(*args)
        if self.row != 1:
            raise Exception("Vector cannot have row greater 1")

    def __mul__(self, other: 'Matrix') -> 'Vector':
        other = Vector(other.matrix) if type(other) is Vector else other

        if type(other) is Vector:
            other.tranponate()
            # other = Matrix(other.matrix)
        return Vector((Matrix(self.matrix) * Matrix(other.matrix)).matrix)
