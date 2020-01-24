# pybin
Original linux commands coded by python.

<br>

## Install

Type following in where you want to save `pybin`.

```
git clone https://github.com/nariaki3551/pybin.git
cd pybin
pip3 install -r requirement.txt
python3 setup.py
```

Then, add following in `~/.bash_profile`, `~/.bashrc`, `~/.zshrc` or other appropriate file.

```
export PATH=xxx/pybin/bin:${PATH}
```

This is displayed when you run  `python3 setup.py`.

<br>

## How to use

Essentially all commands are used through pipes.<br>
`cat file | pyreverse`<br>

Some commands has options.<br>
`cat file | pyline -l`

<br>

## Commands

+ Text manipulation
  + pyline
  + pycolumn
  + T
  + pysplit
  + pyjoin
  + pyreplace
  + pyremove
  + pyadd
  + pycount
  + pyreverse
+ statistics
  + pysum
  + pymax
  + pymin
  + pymean
  + pyvar
  + pycorr
+ other
  + pysort
  + pywhile

<br>

## Simple explanation of commands

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

cat sample.txt | pyline 1
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


$ ls | pysplit . | pycolumn 0
REAME
T
column
dict


$ ls | pysplit . | pycolumn 0\|1
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


$ ls | pysplit -n 2
RE ADME.md
T. py
co lumn.py
di ct.py
```

<br>

#### pyjoin

Join.

```shell
$ ls | split .
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


$ ls | pyadd -a test_
test_README.md
test_T.py
test_column.py
test_dict.py


$ ls | pyadd -a -e \'
'README.md'
'T.py'
'column.py'
'dict.py'

$ ls | pyadd -a -n 0
0README.md
1T.py
2column.py
3dict.py
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

#### pyreverse

Reverse inputs.

```bash
$ cat aaa.py
def main():
    print('HELLO WORLD')
main()


$ cat aaa.py | pyreverse
main()
    print('HELLO WORLD')
def main():


$ cat aaa.py | pyreverse -s
main()
print('HELLO WORLD')
def main():
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
<br>

#### pyvar

Calculate variance.

```shell
$ cat test.txt
10
20
30

$ cat test.txt | pyvar -d 0
66.6666666667

$ cat test.txt | pyvar -d 1
100.0
```

<br>

#### pycorr

Calculate correlation coefficient.

```shell 
$ cat tmp.txt | pysplit ,
a b c
1 3 4
1 2 3
0 1 5
3 5 2
4 5 3


$ cat tmp.txt | pysplit , | pycorr -p 0 1
a b: 0.9525793444156803


$ cat tmp.txt | pysplit , | pycorr -p -a
a b: 0.9525793444156803
a c: -0.7472647177570733
b c: -0.7844645405527361


$ cat tmp.txt | pysplit , | pycorr -p -a | pysort -k 2 -n
b c: -0.7844645405527361
a c: -0.7472647177570733
a b: 0.9525793444156803
```
<br>

### others
#### pysort

Sort.

```shell
$ cat tmp.txt
0 39
31 2
10 2
6 21
1 4
52 4

$ cat tmp.txt | pysort
0 39
1 4
10 2
31 2
52 4
6 21

$ cat tmp.txt | pysort -n -i
0 39
1 4
6 21
10 2
31 2
52 4

$ cat tmp.txt | pysort -k 1 -n -i
31 2
10 2
1 4
52 4
6 21
0 39

$ cat tmp.txt | pysort -k 1 0 -n -i
10 2
31 2
1 4
52 4
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
     436     801    4361 README.md
      34      83     655 T.py
      76     209    1905 column.py
      35      69     692 dict.py

$ ls | pywhile wc -l
     436 README.md
      34 T.py
      76 column.py
      35 dict.py
```


<br>
<br>
<br>
## Specific example of commands
Sort files by line number.

```
ls | pywhile wc -l | pysort -k 0 -n
```
<br>
Kill all jobs.

```
jobs -ls | pycolumn 1 | pywhile kill
```

