
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

textoClaro = 'ATACARBASESUL'
textoEscuro = 'LBMCOCJMSSDCX'
tamtexto = len(textoClaro)

chave = ''
i=0
while i < tamtexto:
	e = alfabeto.find(textoEscuro[i])
	c = alfabeto.find(textoClaro[i])
	p = (e - c) %26
	chave +=  alfabeto[p]
	i += 1
print 'Chave:' ,
print chave

