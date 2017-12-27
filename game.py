import math
import random
words=["hello", "music", "random", "rhythm", "python", "texas", 
"dictionary", "cooking", "spaghetti", "jazz","bagpipes", "galaxy", 
"blizzard","knapsack","algorithms","engineering", "computer", 
"electrical","megahertz", "pineapple","daydreamer", "brainstorm",
"crystallized", "notebook", "chocolate", "festival", "camera", 
"highway", "headphones", "fluorescent"]
letters={
	'a':False,'b':False,'c':False,'d':False,'e':False,'f':False,
	'g':False,'h':False,'i':False,'j':False,'k':False,'l':False,
	'm':False,'n':False,'o':False,'p':False,'q':False,'r':False,
	's':False,'t':False,'u':False,'v':False,'w':False,'x':False,
	'y':False,'z':False
}

def letterReplacer(targetWord, displayedWord, letter):
	newWord=list(displayedWord)
	for i in range(len(targetWord)):
		if letter == targetWord[i]:
			newWord[i]=letter
	return ''.join(newWord)

def checkValidity(userinput):
	if not userinput in letters:
		print "Invalid guess."
		return False
	elif letters[userinput]:
		print "You guessed that one already!"
		return False
	else: return True

triesLeft=7
lettersLeft=0
index=random.randrange(0, len(words),1)
won= False

target=words[index]
lettersLeft=len(target)
displayedWord="_" * len(target)

while (triesLeft>0):
	print displayedWord
	c=raw_input("Enter a letter: ")
	c=c.lower()
	while (not checkValidity(c)):
		c=raw_input("Enter a letter: ")
		c=c.lower()
	letters[c]=True
	if c in target:
		print "You correctly guessed a letter!"
		displayedWord=letterReplacer(target, displayedWord,c)
		if target==displayedWord:
			print "You won!"
			print "Your word was " + target
			won=True
			break
	else: 
		print "You didn't guess a letter!"
		triesLeft=triesLeft-1
		if triesLeft==6:
			print " O "
			print ""
			print ""
			print ""
		elif triesLeft==5:
			print " O "
			print " | "
			print ""
			print ""
		elif triesLeft==4:
			print " O "
			print " | "
			print " | "
			print ""
		elif triesLeft==3:
			print " O "
			print "\| "
			print " | "
			print ""
		elif triesLeft==2:
			print " O "
			print "\|/"
			print " | "
			print ""
		elif triesLeft==1:
			print " O "
			print "\|/"
			print " | "
			print "/  "
		elif triesLeft==0:
			print " O "
			print "\|/"
			print " | "
			print "/ \ "
if won==False:
	print "You lose!"
	print "Your word was " + target
			

