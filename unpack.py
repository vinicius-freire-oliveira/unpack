# Define um dicionário chamado pessoa com as chaves 'nome' e 'idade'
pessoa = {'nome': 'Éder Jofre', 'idade': 85}

# Usa a função format() para formatar uma string com os valores do dicionário pessoa
# O operador ** é usado para desempacotar o dicionário pessoa e passá-lo como argumentos nomeados para a função format()
print('Olá, {nome}. Você tem {idade} anos.'.format(**pessoa))
