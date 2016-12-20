from sys import stdin 
data = [row.strip() for row in stdin.readlines()]
for elm in data[::-1]:
	print(elm)