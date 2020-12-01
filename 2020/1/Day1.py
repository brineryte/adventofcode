def partOne():
    with open('input.txt') as file:
        arrExpenses = []
        for line in file:
            arrExpenses.append(int(line))

        for expense in arrExpenses:
            for otherExpense in arrExpenses:
                if expense + otherExpense == 2020:
                    print(expense * otherExpense)
                    break

        print(arrExpenses)

    print()


def partTwo():
    with open('input.txt') as file:
        arrExpenses = []
        for line in file:
            arrExpenses.append(int(line))

        for expense in arrExpenses:
            for otherExpense in arrExpenses:
                for thirdExpense in arrExpenses:

                    if expense + otherExpense + thirdExpense == 2020:
                        print(expense * otherExpense * thirdExpense)
                        break

        print(arrExpenses)

    print()


partOne()
partTwo()