# Nonogram TEX generator

## Usage
You write a file like the following:

<input.txt>
``` sh
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
-----XX---XX--------
```

And invoke the program as such:

``` sh
$ python3 generator.py -i input.txt -o output.tex
```

along with an optional `-s` or `--solution` if you want the solution to be part of the output. Then compile the resulting tex-file using XeLaTeX.

Both input and output files are optional. If any of them are omitted, stdin/stdout wil be used respectively.
