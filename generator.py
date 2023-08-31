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

# Euler-formel, løsbar iflg https://nonogram.kniffen.dev/
m = """
--XX-XX-------------
--X-X-X--------X----
--XX-XX-------XX----
---------------X----
-XXXXXXXX------X----
--XX----X------X----
---XX---------XXX---
----XX--------------
---XX------XXXXXXXXX
--XX----X-----------
-XXXXXXXX----X---X--
X------------X---X--
X------XXX---X-X-X--
X-X-XX-X-X---XX--X--
XX-----X-X---X-X----
X-X-XX-X-X---X-X-X--
X-X----XXX----------""".split("\n")[1:]

# Mario bullet
# m = """
# ---XXXX--XXXXXXX-----------
# --XXXXXXXXXXXXXXXXXX-------
# -X---XXXX-----X--XXXXX-----
# -X---X-XX-----X---XXXXX----
# XXXXX-XXXXXXXXXX--XXXXXX---
# XXXXX-X-XXXXXXXXXXX--XXXX--
# XXXXX-X-XXXXXXXXXX---X-XXX-
# XXXXX-X-XXXXXXXXXX--X-X-XX-
# XXXXX-X-XXXXXXXX-XX--XXXXXX
# XXXXX-X-XXXXXXX---XX---XXXX
# XXXXX-X-XXXXXX-X--XXXXXXXXX
# XXXXX-X-XXXXXX-X---XXXXXXXX
# XXXXX-X-XXXXXX-X----XXXXXXX
# XXXXX-X-XXXXXX--XXX---XXXXX
# XXXXX-X-XXXXXX--XXX-----XX-
# -XXXX-X-XXXXXXX-XXXXXX--X--
# -XXXXX-X-XXXXXX---XXXXXX---
# --XXXX-XXXXXXXXX---XXX-----
# --XXXXX--XXXXXXXXXXX-------""".split("\n")[1:]

# # Kanin
# m = """
# ------XXXXXXXXXX-----------
# ------XX-----XXXX----------
# ------XXXXXXX-XXXX---------
# -----XXXXXXXXX-XXXXXXX-----
# ----XXX-----XXX-XXXXXXXX---
# ----XXX-------XXXXXXXXXXX--
# -----XXX-------XXXXXXXXXXX-
# -----XXXXXXXXXX-XXXX--XXXX-
# ------XXXXXXXXXXXXXX--XXXXX
# --------XXXXX-XXXXXXXXXXXXX
# -------------XXXXXXXXXXXXXX
# --------------XXXXXXXXXXXX-
# ---------XXXXXXXXXXXXXXXX--
# -------XXXXXXXX-XXXXXXXX---
# -----XXXXXXXXXXX-XXXXXX----
# ----XXXXXXXXXXXXXX---XXX---
# ----XXXXXXXXXXXXXXXXXXXX---
# ---XXXXXXXXXXXXXXXXXXXXX---
# ---XXXXXXXXXXXXXXXXXXXXX---
# --XXXXXXXXX--XXXXXXXXXXX---
# --XXXXXXXXXXX-XXXXXXXXXX---
# XX-XXXXXXXXXX-XXXXXXXXX----
# X-XXXXXXXXXXXX-XXXX-XX-----
# X-XXXXXXXXXXXX-XXX-XXX-----
# XX-XXXXXXXXXX-XXXXXX-XX----""".split("\n")[1:]
solution = False

# print(m)
#

import argparse
import sys

parser = argparse.ArgumentParser(
    prog = 'Nonogram tex-file generator',
    description = 'Generates a TEX-file for a nonogram puzzle.')

parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout)
parser.add_argument('-s', '--solution', action='store_true')

args = parser.parse_args()
infile, outfile, solution = (args.input, args.output, args.solution)

print(infile)

with infile as f:
    m = f.read().splitlines()

rows = [[(next(group)[0], 1+sum(1 for _ in group)) for k, group in groupby(enumerate(line), key=lambda x: x[1]) if k == "X"]
                               for line in m]
cols = [[(next(group)[0], 1+sum(1 for _ in group)) for k, group in groupby(enumerate(line), key=lambda x: x[1]) if k == "X"]
                               for line in zip(*m)]

output = ""
output += """\\documentclass[tikz]{standalone}
\\usepackage{logicpuzzle}

\\begin{document}

"""

output += f"\\begin{{center}}\\begin{{nonogram}}[rows={len(rows)}, columns={len(cols)}, fontsize=huge]"
output += "\\nonogramV{" + ", ".join("{" + (", ".join(map(lambda x: str(x[1]), ix[::-1])) if ix else "0") + "}" for ix in rows[::-1]) + "}"
output += "\\nonogramH{" + ", ".join("{" + (", ".join(map(lambda x: str(x[1]), ix[::-1])) if ix else "0") + "}" for ix in cols) + "}"
if solution:
    for i, row in enumerate(rows[::-1]):
        if row:
            output += f"\\nonogramrow{{ {i+1} }}{{" + ", ".join([f"{i+1}/{l}" for i, l in row]) + "}"
output += "\\end{nonogram}"
output +="\\end{center}"
output += "\\end{document}"

with outfile as f:
    f.write(output)
