from googletrans import Translator

translator = Translator()

f=open('output2.txt','rb')
lines=f.readlines()

for i in lines:
	a=i.decode('ascii', errors='ignore')
	print(a)

	result = translator.translate(a,dest='ja')
	print(result.text)
	break;