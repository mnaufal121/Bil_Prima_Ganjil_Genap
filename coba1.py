def function_types(number):
    def temp(massage):
        print(number + ' termasuk bilangan ' + massage)
    return temp


numbers = []
input1 = input('Masukkan jumlah batas list: ')
limit = int(input1)

for i in range(0, limit):
    input2 = input('Masukkan angka : '.format(i))
    numbers.append(input2)

for number in numbers:
    result1 = function_types(number)
    point = 1
    for i in range(2, int(number)):
        if int(number) % i == 0:
            point = 0
            break
    if point == 1:
        result1('prima')
    elif int(number) % 2 == 0:
        result1('genap')
    else:
        result1('ganjil')