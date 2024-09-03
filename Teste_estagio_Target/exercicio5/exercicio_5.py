#  Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# Dados do exercicio

palavra = (input("Digite uma palavra:"))
palavra_original = palavra
palavra_reversa = palavra_original[::-1]
print("palavra original", palavra_original)
print("palavra reversa: ", palavra_reversa)

