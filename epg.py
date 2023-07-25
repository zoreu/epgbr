import sys
from datetime import datetime, timedelta
import re
def fix(epg_file):

    # Ler o conteúdo do arquivo e realizar as correções de horário
    print('lendo arquivo para correcao')
    with open(epg_file, 'rb') as f:
        content = f.read().decode('utf-8')  # Decodificar os bytes em uma string

    # Localizar todas as tags <programme> no conteúdo
    programas = re.findall(r'<programme.*?</programme>', content, re.DOTALL)
    print('aplicando correcao')
    for programa in programas:
        # Extrair os atributos "start" e "stop" do programa
        start_match = re.search(r'start="(\d{14}) \+(\d{4})"', programa)
        stop_match = re.search(r'stop="(\d{14}) \+(\d{4})"', programa)

        if start_match and stop_match:
            start_str = start_match.group(1)
            start_offset = start_match.group(2)

            stop_str = stop_match.group(1)
            stop_offset = stop_match.group(2)

            start_time = datetime.strptime(start_str, '%Y%m%d%H%M%S')
            stop_time = datetime.strptime(stop_str, '%Y%m%d%H%M%S')

            # Subtrair 3 horas dos horários
            start_time -= timedelta(hours=3)
            stop_time -= timedelta(hours=3)

            # Converter de volta para strings no formato correto
            start_str = start_time.strftime('%Y%m%d%H%M%S %z')
            stop_str = stop_time.strftime('%Y%m%d%H%M%S %z')

            # Substituir os horários corrigidos no programa
            programa_corrigido = programa.replace(start_match.group(0), 'start="{} +{}"'.format(start_str, start_offset))
            programa_corrigido = programa_corrigido.replace(stop_match.group(0), 'stop="{} +{}"'.format(stop_str, stop_offset))

            # Substituir o programa corrigido no conteúdo
            content = content.replace(programa, programa_corrigido)


    # Escrever o conteúdo corrigido no arquivo novamente em modo binário
    print('gravando arquivo novamente')
    with open(epg_file, 'wb') as f:
        f.write(content.encode('utf-8'))  # Codificar a string de volta em bytes

fix(sys.argv[1])