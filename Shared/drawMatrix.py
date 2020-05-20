



def drawMatrix(matrix):
    for i in matrix:
        query = ''
        for j in i:
            query += f'{str(j):4}'+" "
        print(query)