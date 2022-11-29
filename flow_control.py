operand = input(F"оберіть дію: додавання + віднімання - множення * ділення / возведення у ступінь **")
score = float(input("Введіть перше число"))
score2 = float(input("Введіть другечисло"))
while True:
    if operand == "+":
        print(score + score2)
        break
    if operand == "-":
        print(score - score2)
        break
    if operand == "*":
        print(score * score2)
        break
    if operand == "/":
        print(int(score / score2))
        break
    if operand == "**":
        exponentiation = int(input("до якого ступіню потрібно примножити число"))
        print(score ** exponentiation)
        break
    else: operand = input(F"неправильний знак: додавання + віднімання - множення * ділення / возведення у ступінь ** ")
