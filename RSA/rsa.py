from Crypto.PublicKey import RSA
from Crypto import Random

#gera o par de chaves (publica e privada)
random = Random.new().read
chave = RSA.generate(1024, random)

#exporta a chave publica, para utiliza-la para criptografar uma mensagem
chave_publica = chave.publickey() 

texto = raw_input("Digite o texto a ser encriptado: ")

textoCodificado = chave_publica.encrypt(texto, 32)
print 'Texto encriptado:', textoCodificado

# decodifica o texto para a mensagem original, utilizando a chave privada
textoDecodificado = chave.decrypt(textoCodificado)
print 'Texto desencriptado:', textoDecodificado
