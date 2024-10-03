import pandas as pd
import numpy as np
from auxiliar.conexoes import obter_dados

# Constante do Endereço dos dados

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
TIPO_ARQUIVO = 'csv' #input('Qual é o tipo do arquivo? :').lower()
SEPARADOR = ';' #input('Qual é o separador do arquivo? : ').lower()
# obter dados
# CSV = Comma separated values mas que nem sempre são vírgulas, é preciso verificar
#sep = separator ';' ou '.' ou ','
# encoding = UTF-8 ou iso-8859-1 ou latin
try:
    print('Pegando os dados da ocorrências meu cria...')
    #(endereco_arquivo, nome_arquivo, tipo_arquivo, separador) parâmetros
    df_ocorencias = obter_dados(ENDERECO_DADOS,'',TIPO_ARQUIVO,SEPARADOR)
    #print(df_ocorencias.head()) # head sem valor trará as  primeiras linhas

    print("Dados obtidos com sucesso!")

except Exception as e:

    print('Deu erro ai paizão, confere a parte das ocorrências ai',e)
    exit()

# delimitar as variaveis solicitadas e totalizando

try:
    print('Delimitando as colunas e variaveis solicitadas e totalizando-as')
    # cidade e roubo de veículos
    # cidade = munic, roubo de veiculos = roubo_veiculo
    #print(df_ocorencias.columns)

    df_roubo_veiculo = df_ocorencias[['munic','roubo_veiculo']]

    df_total_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()

    #print(df_total_roubo_veiculo)

    print('Delimitação e totalização Concluida')

except Exception as e:

    print('Deu erro ai paizao', e)

    exit()

# array: é uma estrutura de dados que potencializa os calculos matemáticos e estatísticos, logo recomenda-se a utilização dessa estrutura para esse fim
# para utilizar o array é preciso instalar e importar a biblioteca NumPy responsável por nos oferecer métodos matemáticos e estatísticos
    
# obter quartis e indentificar
    
try:

    print('Obtendo maiores e menores munics...')

# converter a variavel rubo_veiculo para array numpy

    array_roubo_veiculo = df_total_roubo_veiculo['roubo_veiculo'].to_numpy()

    #QUANTIL / QUARTIL
    #Q1 - 25%
    q1 = np.quantile(array_roubo_veiculo,0.25,method='weibull')
    #Q2 - 50%
    q2 = np.quantile(array_roubo_veiculo,0.5,method='weibull')
    #ou mediana = np.median(array_roubo_veiculo)
    #Q3- 75%
    q3 = np.quantile(array_roubo_veiculo,0.75,method='weibull')
    #print(q1,q2,q3)
    #Obter os municipios c mais roubos de veiculos
    df_munics_acima_q3 = df_total_roubo_veiculo[df_total_roubo_veiculo['roubo_veiculo'] > q3]
        #Obter os municipios c menos roubos de veiculos
    df_munics_abaixo_q1 = df_total_roubo_veiculo[df_total_roubo_veiculo['roubo_veiculo'] < q1]
    print('\nMunicípios com mais roubos de veículos :')
    print(20*'-')
    print(df_munics_acima_q3.sort_values(by='roubo_veiculo', ascending= False))
    print('\nMunicípios com menos roubos de veículos :')
    print(20*'-')
    print(df_munics_abaixo_q1.sort_values(by='roubo_veiculo', ascending= True))
except Exception as e:

    print('Deu b.o nos maiores menores paizao', e)
    exit()