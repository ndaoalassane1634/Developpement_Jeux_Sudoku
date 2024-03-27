import random

grille=[
    [0,9,3,4,7,8,5,2,6],
    [7,2,5,6,9,3,8,4,1],
    [4,6,8,5,2,1,3,7,9],
    [9,8,7,3,5,6,2,1,4],
    [6,5,1,2,8,4,9,3,7],
    [2,3,4,9,1,7,6,5,8],
    [3,4,2,1,6,9,7,8,5],
    [5,7,6,8,4,2,1,9,3],
    [8,1,9,7,3,5,4,6,2]
]

def check_ligne(grille):
  for i in range(9):
    if sorted(grille[i]) !=[1,2,3,4,5,6,7,8,9]:
      return False
  return True

def check_col(grille):
  for i in range(9):
    col=[]
    for j in range(9):
      col.append(grille[i][j])
    if sorted(col) !=[1,2,3,4,5,6,7,8,9]:
      return False
  return True

def check_carre(grille,a,b):
  carre=[]
  for i in range(a,a+3):
    for j in range(b,b+3):
      carre.append(grille[i][j])
  if sorted(carre)!=[1,2,3,4,5,6,7,8,9]:
    return False

def check_carre_grille(grille):
  for x in range(0,9,3):
    for y in range(0,9,3):
      if check_carre(grille,x,y) is False:
        return False
  return True


check_carre_grille(grille)

def sudoku_checker(grille):
  return check_carre_grille(grille) and check_col(grille) and check_ligne(grille)

sudoku_checker(grille)

def case_vide(grille):
  for i in range(9):
    for j in range(9):
      if grille[i][j]==0:
        return i,j
  return None, None


def ligne_valide(n,x,grille):
  return not n in grille[x]

def col_valide(n,y,grille):
  col=[]
  for i in range(9):
    col.append(grille[i][y])
  return not n in col


def choix_carre(x, y):
    return (x // 3) * 3, (y // 3) * 3

def carre_valide(n,x,y,grille):
  hor, ver = choix_carre(x,y)
  liste_carre=[]
  for i in range (hor,hor+3):
    for j in range (ver, ver+3):
      liste_carre.append(grille[i][j])
  return not n in liste_carre

def chiffre_valide(n,x,y,grille):
  return ligne_valide(n,x,grille) and col_valide(n,y,grille) and carre_valide(n,x,y,grille)

chiffre_valide(1,0,0,grille)

def afficher_grille(grille):
    ligne = "-" * 23
    print(ligne)
    for i in range(len(grille)):
        if i % 3 == 0 and i != 0:
            print(ligne)
        for j in range(len(grille[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grille[i][j])
            else:
                print(str(grille[i][j]) + " ", end="")
    print(ligne)
def solver(grille):
  ligne,colonne = case_vide(grille)
  if ligne is None:
    return True
  for i in range(1,10):
    if chiffre_valide(i,ligne,colonne,grille):
      grille[ligne][colonne]=i
      afficher_grille(grille)
      if solver(grille):
        return True
      grille[ligne][colonne]=0
      afficher_grille(grille)
  return False

solver(grille)


def remplir_carre(grille,x,y):
  liste=random.sample(range(1,10),9)
  compteur=0
  for i in range(x,x+3):
    for j in range(y,y+3):
      grille[i][j]=liste[compteur]
      compteur+=1
  return grille

def remplir_carre_diag(grille):
  for i in range(0,9,3):
    grille=remplir_carre(grille,i,i)
  return grille

remplir_carre_diag()

def remplir_grille(grille, x=0, y=0):
  if x==9: #dépassement derniere ligne
    return True # cas de base, tt est rempli
  if grille[x][y]!=0: #si la case est déja remplie
    if y==8: #passer à la ligne suivante en arrivant au bout de la colonne
      return remplir_grille(grille, x+1, 0)
    else: #colonne suivante
      return remplir_grille(grille, x, y+1)
  for i in range(1,10): #tester les chiffres
    if chiffre_valide(i,x,y,grille):
      grille[x][y]=i #si ok, le placer ds la grille
      if y==8: #ligne suivante en bout de colonne
        if remplir_grille(grille, x+1, 0):
          return True
      else: #colonne suivante
        if remplir_grille(grille, x, y+1):
          return True
      grille[x][y]=0
  return False #déclenche le backtrack si aucun chiffre trouvé

def generation_grille():
  grille=[[0] * 9 for _ in range(9)]
  remplir_carre_diag(grille)
  remplir_grille(grille)
  return grille

afficher_grille(generation_grille())
