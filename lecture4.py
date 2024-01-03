#Excercice 1 Factoriel
#7!=1*2*3*4*5*6*7
#3!=1*2*3
"""
lire un entier n 
calculer et afficher le factoriel de n 
"""
""" n=int(input("donner un nombre"))
F=1
for counter in range(1,n+1):
    F=F*counter
print("le factoriel de N est ",F) """
#Triangle de Pascal
"""
lire un entier donnee par l'utilisateur 
exemple=7
*******
******
*****
****
***
**
*
"""
""" n=int(input("donner le nomber de lignes "))
etoile=n
for ligne in range(1,n+1):
    chaine=""
    for i in range(0,etoile):
        chaine=chaine+"*"
    print(chaine)
    etoile=etoile-1 """
"""
n=7
1
12
123
1234
# ""-->"1"-->"12"-->"123"-->"1234"-->"12345"                    limite=5
123456
1234567
"""
""" nombre=int(input("donner un nombre a tester"))
limite=1
for ligne in range(1,nombre+1):
    ch=""
    for nbr in range(1,limite+1):
        ch=ch+str(nbr)
    print(ch)
    limite=limite+1 """
"""
lire un entier n 
N=7
1
11
112
1124
11248
1124816
112481623

"""
""" n=int(input("donner le nombre de lignes"))
ch="1"
print(ch)
for ligne in range(2,n+1):
    s=0
    for indice in range(0,len(ch)):
        entier=int(ch[indice])
        s=s+entier
    ch=ch+str(s)
    print(ch)
   """
""" nombre=107
chaine="this is our first lecture in the course.welcome to our python course.thank your all for your confidence"
newString=chaine.split(".")
print(newString) """
"""
chaine[indice]--> le caractere qui se trouve a la postion indice
str  convert any other type to string/str
len  taille d'une chaine de caracteres
lower A --> a    B-->b 
upper a --> A   c --> C
capitalize   transforme le premier caractere d'une chaine de caractere en majuscule
title transforme le premier caractere de chaque mot majuscule
count compter le nombre d'ocurrence d'un caractere ou d'un mot
index retourne l'indice de la premiere occurence d'un caractere
find retourne l'indeice de la premiere occurence d'un caractere , s'il n'existe pas elle -1
replace remplacer une ancienne valeur d'un caractere par une nouvelle valeur
stratswith retourne vrai si la chaine commence par la valeur donne ,retourne faux sinon
endswith retourne vrai si la chaine se termine par la valeur donne,retourne faux sinon
split
"""

#Excercice 
#lire une chaine de caractere donnee par l'utilisateur composee de 7 caracteres (boucle)
#1-Verfifer si la chaine donnee commence et se termine par le meme caractere  abaca --> Vrai   
# abcvvbf  --> Faux
# verifier si la chaine donnee contient des lettres majuscules 
# verifier si la chaine est palindrome -- > abbcbba
# verifier si la chaine de caracteres est  purement alphabetique. 







#def
#arrays

"""
N=5
1
11
112
1124
11248
afficher "1"
"1"
"11248"+"16"-->"1124816"
ch[0]
ch[4]
x=0 
x=0+ch[0]
x=0+ch[0]+ch[1]
x=0+ch[0]+ch[1]+ch[2]
x=0+"1"+"1"+"2"+"4"
x=0+"1"+"1"+"2"+"4"+"8"=16-->str(x) "16"
"""