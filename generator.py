from itertools import groupby

# Dino
m = """
-----------XXXXXXXX-
----------XX-XXXXXXX
----------XXXXXXXXXX
----------XXXXXXXXXX
----------XXXXXXXXXX
----------XXXXX-----
----------XXXXXXXX--
X--------XXXXX------
X-------XXXXXX------
XX----XXXXXXXXXX----
XXX--XXXXXXXXX-X----
XXXXXXXXXXXXXX------
-XXXXXXXXXXXXX------
--XXXXXXXXXXX-------
----XXXXXXXX--------
----XXXXXXX---------
-----XXX-XX---------
-----XX---X---------
-----X----X---------
-----XX---XX--------""".split("\n")[1:]

# Euler-formel
m = """
-XX-XX------
-X-X-X------
-XX-XX---X--
--------XX--
-XXXXXX--X--
-X-------X--
--X-----XXX-
---X--------
--X----XXXXX
-X----------
-XXXXXX--X-X
-----------X
X----XXX-X-X
--XX-X-X-X--
X----X-X-X-X
X-XX-X-X----
X----XXX----""".split("\n")[1:]

# Mario bullet
m = """
---XXXX--XXXXXXX-----------
--XXXXXXXXXXXXXXXXXX-------
-X---XXXX-----X--XXXXX-----
-X---X-XX-----X---XXXXX----
XXXXX-XXXXXXXXXX--XXXXXX---
XXXXX-X-XXXXXXXXXXX--XXXX--
XXXXX-X-XXXXXXXXXX---X-XXX-
XXXXX-X-XXXXXXXXXX--X-X-XX-
XXXXX-X-XXXXXXXX-XX--XXXXXX
XXXXX-X-XXXXXXX---XX---XXXX
XXXXX-X-XXXXXX-X--XXXXXXXXX
XXXXX-X-XXXXXX-X---XXXXXXXX
XXXXX-X-XXXXXX-X----XXXXXXX
XXXXX-X-XXXXXX--XXX---XXXXX
XXXXX-X-XXXXXX--XXX-----XX-
-XXXX-X-XXXXXXX-XXXXXX--X--
-XXXXX-X-XXXXXX---XXXXXX---
--XXXX-XXXXXXXXX---XXX-----
--XXXXX--XXXXXXXXXXX-------""".split("\n")[1:]

solution = False

# print(m)

rows = [[(next(group)[0], 1+sum(1 for _ in group)) for k, group in groupby(enumerate(line), key=lambda x: x[1]) if k == "X"]
                               for line in m]
cols = [[(next(group)[0], 1+sum(1 for _ in group)) for k, group in groupby(enumerate(line), key=lambda x: x[1]) if k == "X"]
                               for line in zip(*m)]
# print(*rows, sep="\n")
# print()
# print(*cols, sep="\n")

print("""\\documentclass[tikz]{standalone}
\\usepackage{logicpuzzle}

\\begin{document}

""")

print(f"\\begin{{center}}\\begin{{nonogram}}[rows={len(rows)}, columns={len(cols)}, fontsize=huge]")
print("\\nonogramV{" + ", ".join("{" + ", ".join(map(lambda x: str(x[1]), ix[::-1])) + "}" for ix in rows[::-1]) + "}")
print("\\nonogramH{" + ", ".join("{" + ", ".join(map(lambda x: str(x[1]), ix[::-1])) + "}" for ix in cols) + "}")
if solution:
    for i, row in enumerate(rows[::-1]):
        print("\\nonogramrow{", i+1, "}{", ", ".join([f"{i+1}/{l}" for i, l in row]) + "}")
print("\\end{nonogram}")
print("\\end{center}")
print("\\end{document}")
