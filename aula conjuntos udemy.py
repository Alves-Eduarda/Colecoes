''' Conjuntos
Forma 1
s = set({1,2,3,3,1})
print(s)
print(type(s))
#Métodos matemáticos em conjuntos
estudantes_python = {'Marcos','Patrícia','Pedro','Júlio'}
estudantes_Java = {'Fernando','Júlia','Patrícia','Lucio'}

# Gerando conjuntos com nomes de estudantes únicos

# Forma 1

unicos1 = estudantes_python.union(estudantes_Java)
print(unicos1)

#Forma 2
unicos2 = estudantes_python | estudantes_Java
print(unicos2)

# conjuntos com ambos os vlores

ambos1 = estudantes_python.intersection(estudantes_Java)

ambos2 = estudantes_python & estudantes_Java

print(ambos1)
print(ambos2)

# gerar um conjunto onde os valores do primeiro não estão no outro

so_python = estudantes_python.difference(estudantes_Java)
print(so_python)'''

''' Module collections - counter
Ele gera um dicionário contendo a quantidade das repetições dos iteráveis
no estilo chave: valor
from collections import Counter
texto = """Texto é um conjunto de palavras e frases encadeadas 
que permitem interpretação e transmitem uma mensagem.
É qualquer obra escrita em versão original e 
que constitui um livro ou um documento escrito. Um texto é uma 
unidade linguística de extensão superior à frase."""

palavras = Counter(texto)
print(palavras)
# encontrando as palavras com mais ocorrências
print(palavras.most_common(5))'''

''' Modulo Collections - Default Dict
Default Dict -> ao criar um dicionário utilizando - o, nós informamos um valor 
default, portanto utilizar um lambda para isso. Este valor será utilziado sempre 
que houver um valor definido. Caso tentemos  uma chave que não existe, essa chave 
será criada e o valor default será atribuido.
Obs : lambda são funções sem nome, que podem ou não receber parÂmetros de entrada
e retornar valores.

from collections import defaultdict
dicionario = defaultdict(lambda : 0)

dicionario['curso'] = 'Programação'
print(dicionario)
print(dicionario['outro']) # não irá gerar o keyerror e 
# ainda adiciona uma nova chave com a qual não fazia parte do dicionário 
print(dicionario)

'''

'''
Módulo collections : Ordered Dict
Ele garante a saída de acordo com a ordem de inserção dos elementos no dicionário

from collections import OrderedDict
dic = OrderedDict({'e' : 1, 'c' : 3, 'b' : 4, 'v' : 6})
print(dic)
print()
for c, v in dic.items():
    print(f"chaves {c} :  valores{v}")
'''

"""
Modulo Collections - Named Tuple
São tuplas diferenciadas, onde , especificamos um nome para
a mesma e também parâmetros

from collections import namedtuple
cachorro = namedtuple('cachorro', 'idade')
# criou um tipo de variável cachorro

ray = cachorro(idade=2)
print(ray)
"""
