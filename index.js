const fs = require('fs');
const { format } = require('date-fns-tz');

// Obter a data atual no fuso horário do Brasil
const dataAtual = new Date();
const fusoHorario = 'America/Sao_Paulo';
const formatoDesejado = 'yyyyMMddHHmm';
const dataFormatada = format(dataAtual, formatoDesejado, { timeZone: fusoHorario });

// Criar o conteúdo do arquivo de texto
const conteudoArquivo = `time: ${dataFormatada}`;

// Escrever o conteúdo no arquivo
fs.writeFileSync('update.txt', conteudoArquivo);

console.log('Arquivo gerado com sucesso!');
