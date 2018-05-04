print "Enter a sting "
st=raw_input("")

digit=0
letters=0
for i in st:
	if i>='a' and i<='z':
		letters= letters +1
	elif i>="A" and i<= "Z":
		letters = letters+1
	elif i>='0' and i<='9':
		digit= digit +1

print "digits :"
print digit
print "letters :"
print letters