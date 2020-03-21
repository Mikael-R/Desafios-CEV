print('='*15, '\033[4mDESAFIO 34\033[m', '='*15, '\n')
print('\033[1;30m-_-'*12, '\n\033[1;33mAnalisador de triângulos v2.0\033[m\n', '\033[1;30m-_-\033[m'*12, '\n')
s1 = int(input('\033[1mPrimeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Teçeiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 == s2 and s2 == s3:
    print('\033[1;32mÉ possivel construir um triângulo!\033[m\n\033[1mO triângulo é equilátero.\033[m')
elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 == s2 or s2 == s3:
    print('\033[1;32mÉ possivel construir um triângulo!\033[m\n\033[1mO triângulo é isósceles.\033[m')
elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 != s2 and s2 != s3:
    print('\033[1;32mÉ possivel construir um triângulo!\033[m\n\033[1mO triângulo é escaleno.\033[m')
else:
    print('\033[1;31mNão é possivel construir um triângulo com esses segmentos!\033[m')
