from os import listdir
from os.path import isfile, join

import codecs

developpements = []

couplages_path = "couplages.txt"
couplages = open(couplages_path, "w")
couplages.write("\\part{Couplages}\n")


mypath = ".."
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

onlyfiles.sort()

part = ""

for f in onlyfiles:
    if f[-1] == "~":
        continue
    mode = ""
    lines_f = codecs.open("../" + f, encoding="utf-8").read().splitlines()
    
    if f[0] == "1" and part != "1":
        part = "1"
        print("\\part{Leçons d'algèbre}")
        couplages.write("\\chapter*{Leçons d'algèbre}\n")
    if f[0] == "2" and part != "2":
        part = "2"
        print("\\part{Leçons d'analyse}")
        couplages.write("\\chapter*{Leçons d'analyse}\n")
    if f[0] == "9" and part != "9":
        part = "9"
        print("\\part{Leçons d'informatique}")
        couplages.write("\\chapter*{Leçons d'informatique}\n")

    print()
    print()
    print()
    
    print("\\setcounter{chapter}{" + str(int(lines_f[0]) - 1) + "}")
    print("\\chapter{" + lines_f[1] + "}")
    print()

    couplages.write("\\setcounter{section}{" + str(int(lines_f[0]) - 1) + "}\n")
    couplages.write("\\section{" + lines_f[1] + "}\n\n")
    
    print("\\vspace{-2em}")
    print()

    for l in lines_f[2:]:
        l = l.lstrip().rstrip()
        
        if len(l) <= 0:
            print()
            continue
        if l[0] == "#":
            mode = l[1]
            if l[1] == "r":
                couplages.write("\\end{itemize}")
                print("\\section*{Références}")
                print()
            if l[1] == "d":
                couplages.write("\\begin{itemize}")
                print("\\section*{Développements}")
                print()
            if l[1] == "c":
                print("\\begin{quote}")
            if l[1] == "p":
                print("\\end{quote}")
                print()

            continue

        if mode == "r":
            print("\\bibentry{" + l + "}.")
            print()                

        elif mode == "p":
            sect = False
            if l[0] == "I":
                sect = True
                print("\section{", end="")
            if l[0] == "i":
                sect = True
                print("\subsection{", end="")
            if l[0] == "-":
                sect = True
                print("\subsubsection{", end="")

            if sect == True:
                print(l[2:], end="")
                print("}")

            else:
                print(l)

        elif mode == "d":
            if not(l in developpements):
                developpements.append(l)
            couplages.write("\\item " + l + ".\n\n")
            print(l + ".")
            print()

        else:
            print(l)


dvts = open("developpements.txt", "w")

dvts.write("\\part{Développements}\n")
dvts.write("\\begin{itemize}")
for l in sorted(developpements):
    dvts.write("\\item " + l + ".\n\n")
dvts.write("\\end{itemize}")
