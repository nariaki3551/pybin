# COMMAND
make new linux command by using python.


## Preparation
Download `COMMAND`folder in your home directory (or anywhere). <br>
Then, open `.bashrc` file in your home dirctory and add the following.

```
##### COMMAND ######
dict(){
	python3 ~/COMMAND/dict.py $1
}
reverse() {
	python3 ~/COMMAND/reverse.py
}
tac(){
	cat "$1" | reverse
}
line(){
	python3 ~/COMMAND/line.py $1 $2
}
column(){
	python3 ~/COMMAND/column.py $1 $2 $3
}
remove(){
	python3 ~/COMMAND/remove.py $1
}
split(){
	python3 ~/COMMAND/split.py $1 
}
sum(){
	python3 ~/COMMAND/sum.py $1 $2
}
max(){
	python3 ~/COMMAND/max.py $1 $2
}
min(){
	python3 ~/COMMAND/min.py $1 $2
}
replace(){
	python3 ~/COMMAND/replace.py $1 $2
}
join(){
	python3 ~/COMMAND/join.py $1
}
T(){
	python3 ~/COMMAND/T.py $1
}
```
Please change `~/COMMAND` according to the place where you downloaded COMMAND folder.
<br>
<br>

Next, add the following to `.bash_profile`

```
# read align from .bashrc
source ~/.bashrc
```

##How to use
Essentially all commands are used through pipes.<br>
Exsample,
`cat file | reverse`.<br><br>
Some commands can be given options.  
Exsample, `cat file | line -f`

##Explanation of each command

###<font color="Maroon">reverse</font>
Reverse inputs.

```
$ ls 
> README.md
T.py
column.py
dict.py

$ ls | reverse
> dict.py
column.py
T.py
README.md
```
<br>

###<font color="Maroon">tac</font>
Revese `cat file`.

```
$ cat sample.txt
> aaa
bbb
ccc

$ tac sample.txt
> ccc
bbb
aaa
```
<br>

###<font color="Maroon">split</font>
Split the specified char.

```
$ ls
> README.md
T.py
column.py
dict.py

$ ls | split .
> REAME md
T py
column py
dict py
```

<br>

###<font color="Maroon">line</font>
Operations on rows.

```
$ cat sample.txt
> aaa
bbb
ccc

cat sample.txt | line -l
> [0] aaa
[1] bbb
[2] CCC

cat sample.txt | line 1
> bbb

cat sample.txt | line -1 -l
> [2] ccc

cat sample.txt | line :-1
> aaa
bbb
```
<br>

###<font color="Maroon">column</font>
Operations on columns.

```
$ ls | split .
> REAME md
T py
column py
dict py

$ ls | split . | column -l
> [0] REAME [1] md
[0] T [1] py
[0] column [1] py
[0] dict [1] py

$ ls | split . | column -l -a
> [0] REAME  [1] md
[0] T      [1] py
[0] column [1] py
[0] dict   [1] py

$ ls | split . | column 0
> REAME
T
column
dict
```

<br>

###<font color="Maroon">remove</font>
Remove specified char.

```
$ ls
> README.md
T.py
column.py
dict.py

$ ls | remove py
> README.md
T.
column.
dict.
```
<br>

###<font color="Maroon">sum</font>
Summation.

```
$ cat test.txt
> 10
20
30

$ cat test.txt | sum
> 60.0

$ cat test.txt | sum -i 
60 


$ cat test2.txt
> 10
20
30
aaa

$ cat test2.txt | sum
> error line: aaa
10.0
```
<br>

###<font color="Maroon">max</font>
Max.

```
$ cat test.txt | max
> 30.0

$ cat test.txt | max -i
30
```
<br>
###<font color="Maroon">min</font>
Min.

```
$ cat test.txt | min
> 10.0

$ cat test.txt | min -i
10
```
<br>
###<font color="Maroon">replace</font>
Replace strA to strB.

```
$ ls
> README.md
T.py
column.py
dict.py

$ ls | replace . 2
> README2md
T2py
column2py
dict2py
```
<br>
###<font color="Maroon">join</font>
Join.

```
$ ls | split .
> README md
T py
column py
dict py

$ ls | split . | join 3
> README3md
T3py
column3py
dict3py
```
<br>
###<font color="Maroon">T</font>

```
$ ls | split .
> README md
T py
column py
dict py

$ ls | split . | T
> README T column dict 
md py py py 

$ ls | split . | T | column -a
> README T  column dict
md     py py     py
```
<font color="Maroon"></font>
