nome = input("Qual é o seu nome? ")
print('Olá', nome, ',é um prazer te conhecer!')

expressão = input("Agora digite a sequência de caracteres, para validar sua expressão: ")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")

    if expressão[x] == "[":
        pilha.append("[")

    if expressão[x] == "{":
        pilha.append("{")

    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força a mensagem de erro
            break

    if expressão[x] == "]":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append("]")  # Força a mensagem de erro
            break

    if expressão[x] == "}":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append("}")  # Força a mensagem de erro
            break

    x = x + 1
if len(pilha) == 0:
    print("Parabéns", nome,"! Sua Expressão está correta!")
else:
    print("Poxa", nome,"! Sua Expressão NÃO está correta!")