import re

# Exemplo de texto com tempo
texto = """
00:00:00 - 00:00:11
os recursos talvez esse seja o assunto
00:00:09 - 00:00:14
mais importante o que diz respeito à
00:00:11 - 00:00:18
modelagem de um contrato flash bem feito
00:00:14 - 00:00:21
porque é o ponto em que eu exijo mais
00:00:18 - 00:00:25
inteligência de análise de entender como
00:00:21 - 00:00:28
é o negócio e como traduzir e recursos
"""

# Expressão regular para encontrar os tempos (horário com formato 00:00:00 - 00:00:11)
regex = r"\d{2}:\d{2}:\d{2} - \d{2}:\d{2}:\d{2}\n"

# Remover o tempo usando re.sub (substitui o padrão por uma string vazia)
texto_sem_tempo = re.sub(regex, '', texto)

# Exibe o texto sem o tempo
print(texto_sem_tempo)
