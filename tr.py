from translate import Translator

tr = Translator(from_lang="en", to_lang='ru')

en_txt = 'test record'
ru_txt = tr.translate(en_txt)
print(f' перевод: {ru_txt}')