import pandas as pd
import numpy as np
from auxiliar.conexoes import obter_dados

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
    #print(df_ocorencias.columns)
    #estelionato, mes_ano
except Exception as e:

    print('Deu erro ai paizão, confere a parte das ocorrências ai',e)
    exit()
    
    #peguei os dados estelionato, data e botei num df
try:
    df_estelionato_data = df_ocorencias[['estelionato','mes_ano']]

    df_estelionato_total = df_estelionato_data.groupby(['mes_ano']).sum(['estelionato'])

except Exception as e:

    print('Deu erro ai paizão, confere a parte das ocorrências ai',e)
    exit()
 # fazendo array
try:
     
    array_estelionato_total= df_estelionato_total['estelionato'].to_numpy()
    
    #q1 e q3 # ' weibull é o padrão ' 
    q1 = np.quantile(array_estelionato_total,0.25,method='weibull')
    q3 = np.quantile(array_estelionato_total,0.75,method='weibull')

    
    df_estelionato_maior = df_estelionato_total[df_estelionato_total['estelionato'] > q3]
    df_estelionato_menor = df_estelionato_total[df_estelionato_total['estelionato'] < q1]

    print('\nmes-ano com mais indice de estelionato : :')
    print(20*'-')
    print(df_estelionato_maior.sort_values(by='estelionato', ascending= False))
    print('\nmes-ano com menos indice de estelionato :')
    print(20*'-')
    print( df_estelionato_menor.sort_values(by='estelionato', ascending= True))

except Exception as e:

    print("Deu b.o paizao", e)
    exit()


    