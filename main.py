from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_dos_produtos

path_arquivo = 'vendas.csv'

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_valores_dos_produtos = somar_valores_dos_produtos(produtos_entregues)

print(valor_valores_dos_produtos)