import numpy as np
#As funcoes np.() sao do numpy
#O valor da hipotenusa e igual a raiz quadrada da soma do
#quadrado dos lados A e B

a=int(input("digite o Lado A ")) 
b=int(input("digite o lado B "))
c=int
#variavel "d" representa o resultado

a=a**2
print("lado a ", a)

b=b**2
print("lado b ", b)

c=a+b
print(c)

c=np.sqrt(c)
print("A hipotenusa e ", c)
