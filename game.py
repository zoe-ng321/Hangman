import math
import random
words=[]
letters={
	'a':False,'b':False,'c':False,'d':False,'e':False,'g':False,
	'h':False,'i':False,'j':False,'k':False,'l':False,'m':False,
	'n':False,'o':False,'p':False,'q':False,'r':False,'s':False,
	't':False,'u':False,'v':False,'w':False,'x':False,'y':False,
	'z':False
}

triesLeft=7
lettersLeft=0
index=random.randrange(0, len(words))

target=words[index]
lettersLeft=len(target)

while (triesLeft>0):
	c=nput("Enter a letter: ")
	while (not letters[c]):
		c=input("Enter a letter: ")
	letters[c]=True
	if c in target:
		
