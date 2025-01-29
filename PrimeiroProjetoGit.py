n1 = float(input('Digite sua nota da P1:'))
n2 = float(input('Digite sua nota da P2:'))

media = (n1 + n2) / 2

print('Você tirou na P1 {:.1f} e na P2 {:.1f}, sua média é: {:.1f}'.format(n1, n2, media))

if media < 5:
    print('Você está Reprovado')

elif media >= 5 and media <7 :
    print('Você está de Recuperação')

elif media >= 7:
    print('Você está Aprovado')
