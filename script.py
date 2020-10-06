import pandas as pl 
import matplotlib.pyplot as plt

    ## Lendo arquivos csv /txt

# Lendoo um arquivo .csv com pandas e criando um pandas data frame
dataframe = pl.read_csv('C:/python/data-science/annual-real-gnp-us-1909-to-1970.csv')
    # with open('annual-real-gnp-us-1909-to-1970.txt, 'r') as f:
    # Usando a expressão regular para o separador indicando que eles são os
    # espaços em braco
    # df = pd.read_table(f, sep='\s+')
    # print(df)

plt.figure(figsize=(8, 6))
plt.plot(dataframe['Year'], dataframe['GNP'])
plt.xlabel('Year')
plt.ylabel('GNP')
plt.title('PIB EUA Real Anual de 1909 a 1970')

        ## Inserindo anotações
plt.annotate('Fim da Segunda Mundial', xy=(1945, 355.2),
arrowprops=dict(arrowstyle='->'), xytext=(1920, 300))

plt.annotate('Queda da Bolsa', xy=(1929, 203.6), 
arrowprops=dict(arrowstyle='->'), xytext=(1909, 200))

# Salvar e gerar o gráfico em imagem
plt.savefig('annual-real-gnp-us-1909-to-1970.png')

plt.show()

# plt.close()
