print('='*15, 'DESAFIO 40', '='*15, '\n')
print("""_____________________________________________________________
     IMC	         CLASSIFICAÇÃO	        OBESIDADE (GRAU)
MENOR QUE 18,5	       MAGREZA	                0
ENTRE 18,5 E 24,9	   NORMAL	                0
ENTRE 25,0 E 29,9	   SOBREPESO	            I
ENTRE 30,0 E 39,9	   OBESIDADE	            II
MAIOR QUE 40,0	       OBESIDADE GRAVE	        III
_____________________________________________________________""")
peso = float(input('Peso em quilogramas: '))
altura = float(input('Altura em metros: '))
imc = peso / (altura * altura)
print('\nO IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Classificado como MAGREZA!')
elif imc < 25:
    print('Classificado como NORMAL!')
elif imc < 30:
    print('Classificado como SOBREPESO (GRAU I)!')
elif imc < 40:
    print('Classificado como OBESIDADE (GRAU II)!')
elif imc > 40:
    print('Classificado como OBESIDADE GRAVE (GRAU III)!')
