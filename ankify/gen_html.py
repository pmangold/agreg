import sys

path = str(sys.argv[1])

f = open(path, "r")

first = True
end_char = ""

f_lines = f.readlines()

print(f_lines[0].rstrip(), f_lines[1].rstrip(), end=end_char)
print("#",end=end_char)

print('<meta charset="UTF-8">', end=end_char)

print("<ol type='I'>", end=end_char)

for l in f_lines:
    l = l.lstrip().rstrip()
    if l == "":
        continue

    t = l[0]

    if t == "i" or t == "I":
        l = l[2:]

    if t == "I":
        if not(first):
            print("</ol></li>", end=end_char)
        print("<li>", end=end_char)
        print(l, end=end_char)
        print("<ol>", end=end_char)
        if first:
            first = False

        
    elif t == "i":
        print("<li>", end=end_char)
        print(l, end=end_char)
        print("</li>", end=end_char)

    elif "(dev)" in l:
        print(l, end=end_char)
#       or l[0]== "I" \
#       or "(dev)" in l:
#        print(l, end="")

print("</li></ol>", end=end_char)
