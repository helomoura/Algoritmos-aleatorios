def FizzBuzz():
    inicial = int(input("Informe o numero inicial: "))
    final = int(input("Informe o numero final: "))
    if final>= inicial:
        for num in range(inicial, final + 1):
            if num % 3 == 0 and num % 5 == 0:
                print("FzzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
             print(num)
    else:
        print("O numero final nao pode ser menor que o numero inicial.")

FizzBuzz()