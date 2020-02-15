'''
    . - Em modo padrão, significa qualquer caractere, menos o de nova linha
    ^ - Em modo padrão, significa inicio da string
    $ - Em modo padrão, significa fim da string
    \ - Caractere de escape, permite usar caracteres especiais como se fossem comuns
    [] - Qualquer caractere dos listados entre os colchetes
    * - Zero ou mais ocorrências da expressão anterior
    + - Uma ou mais ocorrências da expressão anterior
    ? - Zero ou uma ocorrência da expressão anterior
    {n} - n ocorrências da expressão anterior
    | - “ou” lógico
    () - Delimitam um grupo de expressões
    \d - Dígito. Equivale a [0-9]
    \D - Não dígito. Equivale a [^0-9]
    \s - Qualquer caractere de espaçamento ([ \t\n\r\f\v])
    \S - Qualquer caractere que não seja de espaçamento.([^ \t\n\r\f\v])
    \w - Caractere alfanumérico ou sublinhado ([a-zA-Z0-9_])
    \W - Caractere que não seja alfanumérico ou sublinhado ([^a-zA-Z0-9_])
'''
import re

#Usando o compile() a expressão regular fica compilada e pode ser usada mais de uma vez
regex = re.compile("\w+")
#Encontra todas as ocorrêncis que atendam a expressão
bandas = "Yes, Genesis & Camel"
print(bandas,"->",regex.findall(bandas))
#Identifica as ocorrências de Björk (e suas variações)
bjork = re.compile('[Bb]j[öo]rk')
nomes = ('Björk', 'björk', 'Biork', 'Bjork', 'bjork')
for nome in nomes:
    # match() localiza ocorrências no inicio da string para localizar em qualquer parte da string, use search()
    print(nome,"->",bool(bjork.match(nome)))
#Substituindo o texto
texto = "A próxima faixa é Stairway to Heaven"
print(texto,"->",re.sub("[Ss]tairway [Tt]o [Hh]eaven","The Rover",texto))
#Dividindo o texto
bandas = "Tool, Porcupine Tree e NIN"
print(bandas,"->",re.split(",?\s+e?\s+", bandas))