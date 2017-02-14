alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numLinhas = 7

texto = 'FUJAM TODOS FOMOS DESCOBERTOS'
tamTexto = len(texto)
numColunas = tamTexto / numLinhas
numColunas += 1

textocodificado = [["A" for x in range(numColunas)] for y in range(numLinhas)]

i = 0
for x in range(numColunas):
	for y in range(numLinhas):
		if i < tamTexto:
			textocodificado[y][x] = texto[i]
		else:
			textocodificado[y][x] = alfabeto[(i*numLinhas)%26]
		i += 1

linhaTextoCodificado = ''

for y in range(numLinhas):
	for x in range(numColunas):
		linhaTextoCodificado += textocodificado[y][x]

print 'Codificado: ',
print linhaTextoCodificado

tamTexto = len(linhaTextoCodificado) 
numLinhas = tamTexto / numLinhas
numColunas = tamTexto / numLinhas
i = 0
textoDecodificado = [["A" for x in range(numColunas)] for y in range(numLinhas)]
for x in range(numColunas):
	for y in range(numLinhas):
		if i < tamTexto:
			textoDecodificado[y][x] = linhaTextoCodificado[i]
		else:
			textoDecodificado[y][x] = ' '
		i += 1

linhaTextoDeCodificado = ''
for y in range(numLinhas):
	for x in range(numColunas):
		linhaTextoDeCodificado += textoDecodificado[y][x]

print 'Decodificado: ',
print linhaTextoDeCodificado
