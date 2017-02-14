
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 3

texto = 'A LIGEIRA RAPOSA MARROM SALTOU SOBRE O CACHORRO CANSADO'
tamtexto = len(texto)
textocodificado = ''
i=0
while i < tamtexto:
	if texto[i] != " ":
		k = alfabeto.find(texto[i])
		c = (k + n) %26
		textocodificado +=  alfabeto[c]
	else:
		textocodificado +=  " "
	i += 1
print 'Texto codificado:' ,
print textocodificado

textodescodificado = ''
i=0
while i < tamtexto:
	if textocodificado[i] != " ":
		k = alfabeto.find(textocodificado[i])
		p = (k - n) %26
		textodescodificado +=  alfabeto[p]
	else:
		textodescodificado += " "
	i += 1
print 'Texto decodificado:' ,
print textodescodificado

