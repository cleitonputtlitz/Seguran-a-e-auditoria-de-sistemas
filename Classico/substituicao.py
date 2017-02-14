alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabetoCifra = 'PORTUGALBCDEFHIJKMNQSVWXYZ'
numLinhas = 7

texto = 'FUJAMTODOSFOMOSDESCOBERTOS'
tamTexto = len(texto)
tamBloco = 5
textoCodificado = ''
i=0
while i < tamTexto:
	k = alfabeto.find(texto[i])
	textoCodificado += alfabetoCifra[k]
	i += 1
	resto = i % tamBloco
	if not resto:
		textoCodificado += ' '

print 'Codificado: ',
print textoCodificado

tamTexto = len(textoCodificado)
textoDecodificado = ''
i=0
while i < tamTexto:
	if textoCodificado[i] == " ":
		textoDecodificado += ' '
	else:
		k = alfabetoCifra.find(textoCodificado[i])
		textoDecodificado += alfabeto[k]
	i += 1
	
print 'Codificado: ',
print textoDecodificado
