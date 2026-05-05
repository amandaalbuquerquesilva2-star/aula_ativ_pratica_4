cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
# Imposto é sempre 10% do subtotal, independente de descontos
imposto = subtotal * 0.10

desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
# Desconto aplicado sobre o subtotal antes de adicionar imposto
desconto = subtotal * (desconto_cupom / 100)

# Total final: subtotal + imposto (sempre cobrado) - desconto do cupom
total = subtotal + imposto - desconto

linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")
# Exibe desconto apenas se houver cupom válido (percentual > 0)
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha