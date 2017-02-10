# pybin
Original linux commands by python.

<br>
## Install
Open Application `Terminal.app` and type following.

```
git clone https://github.com/nariaki3551/pybin.git
cd ~/pybin
python3 setup.py
```

Then, add following in `~/.bash_profile` or other appropriate file.

```
# Setting PATH for pybin
PATH=~/pybin:"$PATH"
```


<br>
##How to use
Essentially all commands are used through pipes.<br>
Exsample,
`cat file | reverse`<br><br>
Some commands has options.  
Exsample, `cat file | line -l`

<br>
##Simple explanation of commands
###Text manipulation
###<font color="Maroon">reverse</font>
Reverse inputs.

```
$ cat aaa.py
def main():
    print('HELLO WORLD')
main()


$ cat aaa.py | reverse
main()
    print('HELLO WORLD')
def main():   


$ cat aaa.py | reverse -s 
main()
print('HELLO WORLD')
def main():   
```
<br>

###<font color="Maroon">split</font>
Split the specified char.

```
$ ls
README.md
T.py
column.py
dict.py


$ ls | split .
README md
T py
column py
dict py


$ ls | split -n 2
RE ADME.md
T. py
co lumn.py
di ct.py
```

<br>

###<font color="Maroon">line</font>
Operations on rows.

```
$ cat sample.txt
aaa
bbb
ccc

cat sample.txt | line -l
[0] aaa
[1] bbb
[2] CCC

cat sample.txt | line 1
bbb

cat sample.txt | line :-1
aaa
bbb
```
<br>

###<font color="Maroon">column</font>
Operations on columns.

```
$ ls | split .
README md
T py
column py
dict py


$ ls | split . | column -l
[0] README [1] md
[0] T [1] py
[0] column [1] py
[0] dict [1] py


$ ls | split . | column -l -a
[0] README [1] md
[0] T      [1] py
[0] column [1] py
[0] dict   [1] py


$ ls | split . | column 0
REAME
T
column
dict


$ ls | split . | column 0\|1
README md
T py
column py
dict py

```

<br>


###<font color="Maroon">remove</font>
Remove specified char.

```
$ ls
README.md
T.py
column.py
dict.py


$ ls | remove py
README.md
T.
column.
dict.
```

<br>
###<font color="Maroon">replace</font>
Replace charA to charB.

```
$ ls
README.md
T.py
column.py
dict.py


$ ls | replace . 2
README2md
T2py
column2py
dict2py
```
<br>
###<font color="Maroon">add</font>

Attach char in head or tail.

```
$ ls
README.md
T.py
column.py
dict.py


$ ls | add -a test_
test_README.md
test_T.py
test_column.py
test_dict.py


$ ls | add -a -e \'
'README.md'
'T.py'
'column.py'
'dict.py'

$ ls | add -a -n 0
0README.md
1T.py
2column.py
3dict.py
```

<br>


###<font color="Maroon">join</font>
Join.

```
$ ls | split .
README md
T py
column py
dict py


$ ls | split . | join 3
README3md
T3py
column3py
dict3py
```
<br>
###<font color="Maroon">T</font>
Swap rows and columns.

```
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
###<font color="Maroon">count</font>
```
$ cat test.txt
1
2
3
1
2

$ cat test.txt | count
3: 1
1: 2
2: 2
```
<br>
###<font color="Maroon">pyif</font>
```
$ cat test.txt
a 1
b 1
c 1
d 2
e 3
f 2

$ cat test.txt | pyif 'float(row[1]) >= 2'
d 2
e 3
f 2 
```

<br>

## statistics
###<font color="Maroon">sum</font>
Calculate total sum.

```
$ cat test.txt
10
20
30

$ cat test.txt | sum
60.0

$ cat test.txt | sum -i 
60 


$ cat test2.txt
10
20
30
aaa

$ cat test2.txt | sum
error line: aaa
60.0

$ cat test2.txt | sum -f -i 
60
```
<br>

###<font color="Maroon">max</font>
Find max element.

```
$ cat test.txt
10
20
30

$ cat test.txt | max
30.0

$ cat test.txt | max -i
30
```
<br>
###<font color="Maroon">min</font>
Find min element.

```
$ cat test.txt
10
20
30

$ cat test.txt | min
10.0

$ cat test.txt | min -i
10
```

<br>
###<font color="Maroon">mean</font>
Calculate mean.

```
$ cat test.txt
10
20
30

$ cat test.txt | mean
20.0
```
<br>

###<font color="Maroon">var</font>

Calculate variance.

```
$ cat test.txt
10
20
30

$ cat test.txt | var -d 0
66.6666666667

$ cat test.txt | var -d 1
100.0
```

<br>

###<font color="Maroon">corr</font>

Calculate correlation coefficient.

```
$ cat tmp.txt | split ,
a b c
1 3 4
1 2 3
0 1 5
3 5 2
4 5 3


$ cat tmp.txt | split , | corr -p 0 1
a b: 0.9525793444156803


$ $ cat tmp.txt | split , | corr -p -a
a b: 0.9525793444156803
a c: -0.7472647177570733
b c: -0.7844645405527361


$ $ cat tmp.txt | split , | corr -p -a | pysort -k 2 -n
b c: -0.7844645405527361
a c: -0.7472647177570733
a b: 0.9525793444156803
```
<br>

###others
###<font color="Maroon">pysort</font>
Sort.

```
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
###<font color="Maroon">pywhile</font>
While commands.

```
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
##Specific example of commands
Sort files by line number.

```
ls | pywhile wc -l | pysort -k 0 -n
```
<br>
Kill all jobs.

```
jobs -ls | column 1 | pywhile kill
```