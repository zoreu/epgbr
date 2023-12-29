import datetime
import pytz

# Obter a data atual no fuso horário do Brasil
data_atual = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))

# Definir o formato desejado
formato_desejado = '%Y%m%d%H%M'

# Formatar a data
data_formatada = data_atual.strftime(formato_desejado)

# Criar o conteúdo do arquivo de texto
conteudo_arquivo = f'time: {data_formatada}'

# Escrever o conteúdo no arquivo
with open('update.txt', 'w') as arquivo:
    arquivo.write(conteudo_arquivo)

print('Arquivo gerado com sucesso!')
