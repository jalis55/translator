
from googletrans import Translator

f=open('output.txt','r')

translator = Translator()
translate=" "
lines=f.read()

translate = translator.translate(lines, src='en', dest='ja')


print(translated.text)