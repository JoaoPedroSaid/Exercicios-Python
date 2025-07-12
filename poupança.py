valorAtual = float(input('Quantos R$ você deseja depositar na sua poupança? '))
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8') # isso é para conseguir formatar datas, valores, etc. no padrão brasileiro

for mes in range(1, 13):
    valorAtual = valorAtual * (1 + 0.005) 
    print(f'No {mes}º você possui {locale.currency(valorAtual, grouping=True)}') 
