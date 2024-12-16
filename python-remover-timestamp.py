import re

print('Cole aqui:')
texto = []  # lista para armazenar as linhas digitadas

# Captura de múltiplas linhas até o usuário digitar uma linha vazia
while True:
    linha = input()
    if linha == '':  # linha vazia interrompe o loop
        break
    texto.append(linha)

# Junta todas as linhas da lista em um único texto
texto_completo = "\n".join(texto)

# Expressão regular para encontrar os tempos no formato 00:00:00 - 00:00:11
regex = r"\d{2}:\d{2}:\d{2} - \d{2}:\d{2}:\d{2}\n"

# Remover os tempos utilizando re.sub
texto_sem_tempo = re.sub(regex, '', texto_completo)

# Exibe o texto sem os tempos
print(texto_sem_tempo)

# Pausa a execução até o usuário pressionar Enter
input("Pressione Enter para sair...")
