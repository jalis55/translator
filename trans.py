from googletrans import Translator

translator = Translator()



with open("tmil.txt",'r', encoding='utf8') as f:

	lines=f.readlines()
	for line in lines:
		result = translator.translate(line,dest='ja')
		print(result.text)


