
#Autor: João 
#Data: 22/12/22/


nome=input("Digite um funcionario: ")
empresa=input("Digite a instituição: ")
quant_funcionarios=int(input("Digite a quantidade de funcionarios: "))
mediaMensalidade=float(input("Digite a media da mensalidade: "))

print(nome + "trabalha na empresa" + empresa)
print("Possui: ", quant_funcionarios, "funcionarios.")
print("A media da mensalidade e de: " + str(mediaMensalidade))

print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [quanti_funcionarios] é: ",type(empresa))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))

responsavel=input("Digite o nome do responsável: ")
funcionario=input("Digite o nome do funcionário: ")
evento=input("Digite o nome do evento: ")
valor=float(input("Digite o valor que será ressarcido: "))

print("Declaro para o senhor" + responsavel + ", que o senhor" +
funcionario + "esteve presente no evento" + evento + "e gastou o valor de RS" + str(valor) + " com a entrada.")
