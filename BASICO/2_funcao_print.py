# \r\n -> CRLF comum em Windows mais antigos
# \n -> LF
print(12, 34, 1011, end='#') # Aceita múltiplos argumentos
print(56, 78, sep=' - ', end='\r\n') # Cria um espaço automaticamente entre os argumentos
print(56, 78, sep=' - ', end='\n') 
# 'sep' permite alterar o separador, por padrão é um 'espaço'.
# 'end' permite alterar o final, por padrão é um '\n' (Uma quebra de linha)