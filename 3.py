def find_operators(seq):
    operators = set()
    for char in seq:
        if char in '+-*/':
            operators.add(char)
    return operators
sequence = input('Введите последовательность символов: ')
result = find_operators(sequence)
print('Множество арифметических операций: ', result)