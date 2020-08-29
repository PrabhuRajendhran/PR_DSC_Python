import sys
n=len(sys.argv)
print(sys.argv)
vcnt=0
ccnt=0
scnt=0
for i in range(1,n):
	for k in sys.argv[i]:
		if k.isalpha():
			if k in ["a","e","i","o","u"]:
				vcnt+=1
			else :
				ccnt+=1
		else:
			scnt+=1	

print("Vowels :", vcnt)
print("Consonants :", ccnt)
print("Special Chars :" , scnt)