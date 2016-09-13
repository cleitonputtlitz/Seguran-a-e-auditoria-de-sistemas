from Crypto.Cipher import AES

chave = '1234567890ASDFGH'

# tamanho do bloco para a cifra
BLOCK_SIZE = 16

# caracter utilizado para preenchimento caso o tamanho do texto digitado nao seja um
# multiplo de BLOCK_SIZE
PADDING = ' '

cifra = AES.new(chave)

texto = raw_input("Digite o texto a ser encriptado: ")

# preenche o texto com PADDING ate que o tamanho seja multiplo de BLOCK_SIZE
texto = texto + (BLOCK_SIZE - len(texto) % BLOCK_SIZE) * PADDING

# codifica a string
textoCodificado = cifra.encrypt(texto)
print 'Texto encriptado:', textoCodificado

# decodifica o texto para a mensagem original
textoDecodificado = cifra.decrypt(textoCodificado)
print 'Texto desencriptado:', textoDecodificado
