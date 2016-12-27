# COMMAND
Original linux commands by using python.


## Install
Download `pybin` folder in your home directory, and type following

```
cd ~/pybin
python3 setup.py
```

Then, add following in `~/.bash_profile`

```
PATH=~/pybin:"$PATH"
```



##How to use
Essentially all commands are used through pipes.<br>
Exsample,
`cat file | reverse`.<br><br>
Some commands can be given options.  
Exsample, `cat file | line -f`

##Simple explanation of each command

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


cat sample.txt | line -1 -l
[2] ccc


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
[0] README  [1] md
[0] T      [1] py
[0] column [1] py
[0] dict   [1] py


$ ls | split . | column 0
REAME
T
column
dict
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
Replace strA to strB.

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


$ ls | add -e -a \'
'README.md'
'T.py'
'column.py'
'dict.py'

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


$ $ cat tmp.txt | split , | corr -p -a | pysort -k 2
a c: -0.7472647177570733
b c: -0.7844645405527361
a b: 0.9525793444156803
```
<br>

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
31 2
10 2
52 4
6 21


$ cat tmp.txt | pysort -n 
0 39
1 4
6 21
31 2
10 2
52 4


$ cat tmp.txt | pysort -k 1 -n
31 2
10 2
1 4
52 4
6 21
0 39


$ cat tmp.txt | pysort -k 1 0 -n
10 2
31 2
1 4
52 4
6 21
0 39
```