
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chave = 'LIMAO'

texto = 'ATACARBASESUL'
tamtexto = len(texto)

mult = tamtexto / len(chave)
mult += 1
palavrachave = chave * mult

textocodificado = ''
i=0
while i < tamtexto:
	k = alfabeto.find(palavrachave[i])
	p = alfabeto.find(texto[i])
	c = (p + k) %26
	textocodificado +=  alfabeto[c]
	i += 1
print 'Texto codificado:' ,
print textocodificado

textodescodificado = ''
i=0
while i < tamtexto:
	k = alfabeto.find(palavrachave[i])
	c = alfabeto.find(textocodificado[i])
	p = (c - k + 26) %26
	textodescodificado +=  alfabeto[p]
	i += 1
print 'Texto decodificado:' ,
print textodescodificado

