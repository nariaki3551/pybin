# pybin : Original linux commands coded by python
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br>

## Install

Type following in where you want to save `pybin`.

```
git clone https://github.com/nariaki3551/pybin.git
cd pybin
python setup.py install
python -m pip install .
```

## How to use

Essentially all commands are used through pipes.<br>
`cat file | pyreverse`<br>

Some commands has options.<br>
`cat file | pyline -l`

<br>

## Commands

+ manager
  + pybin
+ [Text manipulation](https://github.com/nariaki3551/pybin#text-manipulation)
  + pyline
  + pycolumn
  + T
  + pysplit
  + pyjoin
  + pyreplace
  + pyremove
  + pyadd
  + pycount
+ [statistics](https://github.com/nariaki3551/pybin#statistics)
  + pysum
  + pymax
  + pymin
  + pymean
  + pystat
+ [plot](https://github.com/nariaki3551/pybin#plot)
  - pyplot
  - pyscatter
  - pyhist
  - pyviolin
+ [other](https://github.com/nariaki3551/pybin#others)
  + pysort
  + pywhile

<br>

## Simple explanation of commands

**pybin**

```shell
$ pybin -l  # show all commands
pybin commands

T      pyadd   pycolumn pyjoin   pyline    pymax  
pymean pymin   pysort   pyremove pyreplace pysplit
pysum  pywhile pycount  pycolor 

$ pybin --upgrade  # upgrade pybin
pybin upgrade ...
git -C XXX pull
Already up to date.
```

<br>

### Text manipulation

#### pyline

Operations on rows.

```shell
$ cat sample.txt
aaa
bbb
ccc

cat sample.txt | pyline -l
[0] aaa
[1] bbb
[2] CCC

cat sample.txt | pyline -s 1
bbb

cat sample.txt | pyline :-1
aaa
bbb
```

<br>

#### pycolumn

Operations on columns.

```shell
$ ls | pysplit .
README md
T py
column py
dict py


$ ls | pysplit . | pycolumn -l
[0] README [1] md
[0] T [1] py
[0] column [1] py
[0] dict [1] py


$ ls | pysplit . | pycolumn -l -a
[0] README [1] md
[0] T      [1] py
[0] column [1] py
[0] dict   [1] py


$ ls | pysplit . | pycolumn -s 0
REAME
T
column
dict


$ ls | pysplit . | pycolumn -s 0\|1
README md
T py
column py
dict py

```

<br>

#### T

Swap rows and columns.

```shell
$ ls | split .
README md
T py
column py
dict py


$ ls | split . | T
README T column dict
md py py py


$ ls | split . | T | column -a
README T  column dict
md     py py     py
```

<br>

#### pysplit

Split the specified char.

```shell
$ ls
README.md
T.py
column.py
dict.py


$ ls | pysplit .
README md
T py
column py
dict py
```

<br>

#### pyjoin

Join.

```shell
$ ls | pysplit .
README md
T py
column py
dict py


$ ls | split . | pyjoin 3
README3md
T3py
column3py
dict3py
```

<br>

#### pyreplace

Replace charA to charB.

```shell
$ ls
README.md
T.py
column.py
dict.py


$ ls | pyreplace . 2
README2md
T2py
column2py
dict2py
```

<br>

#### pyremove

Remove specified char.

```shell
$ ls
README.md
T.py
column.py
dict.py


$ ls | pyremove py
README.md
T.
column.
dict.
```

<br>

#### pyadd

Attach char in head or tail.

```shell
$ ls
README.md
T.py
column.py
dict.py


$ ls | pyadd test_ -a 
test_README.md
test_T.py
test_column.py
test_dict.py


$ ls | pyadd \' -a -e 
'README.md'
'T.py'
'column.py'
'dict.py'
```

<br>

#### pycount

```shell
$ cat test.txt
1
2
3
1
2

$ cat test.txt | pycount
3: 1
1: 2
2: 2
```
<br>

### statistics

#### pysum

Calculate total sum.

```shell
$ cat test.txt
10
20
30

$ cat test.txt | pysum
60.0

$ cat test.txt | pysum -i
60


$ cat test2.txt
10
20
30
aaa

$ cat test2.txt | pysum
error line: aaa
60.0

$ cat test2.txt | pysum -f -i
60
```
<br>

#### pymax

Find max element.

```shell
$ cat test.txt
10
20
30

$ cat test.txt | pymax
30.0

$ cat test.txt | pymax -i
30
```
<br>
#### pymin

Find min element.

```shell
$ cat test.txt
10
20
30

$ cat test.txt | pymin
10.0

$ cat test.txt | pymin -i
10
```

<br>
#### pymean

Calculate mean.

```shell
$ cat test.txt
10
20
30

$ cat test.txt | pymean
20.0
```

#### pystat

Display all statistics information.

```shell
$ cat test.txt
10
20
30

$ cat test.txt | pystat
num_data     3
min          10.0
max          30.0
mean         20.0
median       20.0
variance     100.0
stdev        10.0
```

<br>

### plot

- pyplot
- pyscatter
- pyhist
- pyviolin

```
$ cat test.txt
10
20
30

$ cat test.txt | pyplot
>> output image
```

### others

#### pysort

Sort.

```shell
$ cat tmp.txt
0 39
31 2
10 2
6 21

$ cat tmp.txt | pysort
0 39
10 2
31 2
6 21

$ cat tmp.txt | pysort -n -i
0 39
6 21
10 2
31 2

$ cat tmp.txt | pysort -k 1 -n -i
31 2
10 2
6 21
0 39
```

<br>

#### pywhile

While commands.

```shell
$ ls
README.md
T.py
column.py
dict.py

$ ls | pywhile wc
wc README.md
     436     801    4361 README.md
wc T.py
      34      83     655 T.py
wc column.py
      76     209    1905 column.py
wc dict.py
      35      69     692 dict.py

$ ls | pywhile wc -p 3  # process number
```
