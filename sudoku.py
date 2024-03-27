grid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
grid


#verifier que chaque ligne contient tt les nombres de 1 à 9
def sudoku_checker_ligne (grid) :
    for i in range(0,8):
        ligne = grid[i]
        if sorted(ligne) != [1,2,3,4,5,6,7,8,9] :
            return False
    return True

test = sudoku_checker_ligne(grid)
test


#verifier que chaque colonne contient tt les nombres de 1 à 9
def sudoku_checker_colonne(grid) :

    for i in range(0, 9) :
        h = []
        for j in range (0, 9) :
            h.append(grid[j][i])
        print(h)
        if sorted(h) !=  [1,2,3,4,5,6,7,8,9] :
            print(h)
            return False
    return True
tes2 = sudoku_checker_colonne(grid)
tes2


#veriefier les carrée
def checker_carre(grid, l, c) :
    liste = []
    for i in range(l, l+3) :
        for j in range(c, c+3) :
            liste.append(grid[i][j])
    if sorted(liste) != [1,2,3,4,5,6,7,8,9] :
        print(liste)
        return False
    return True
carre1 = checker_carre(grid, 0,0)
carre1


def checker_carre_total (grid) :
    for i in range (0, 9, 3) :
        for j in range (0, 9, 3) :
            if checker_carre(grid, i, j) == False:
                return False
    return True
carre2 = checker_carre_total(grid)
carre2


#creation fonction sudoku checker
def sudoku_checker(grid) :
    sudoku_checker_ligne(grid)
    sudoku_checker_colonne(grid)
    checker_carre_total(grid)
    if sudoku_checker_ligne(grid) == True and sudoku_checker_colonne(grid) == True and checker_carre_total(grid) ==True :
        return True
    else :
        return False

test = sudoku_checker_colonne(grid)
test
