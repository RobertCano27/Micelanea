
from calendar import c
import os
from pickle import TRUE


deSeccion = ""
deOp = ""
sp = 1



while sp == 1:
    os.system("cls")

    print("Bienvenido a la miselanea de operaciones: ")

    print("------------------------")
    print("--- 1. Operadores    ---")
    print("--- 2. Condicionales ---")
    print("--- 3. Ciclos        ---")
    print("------------------------")

    deSeccion = int(input("Seleccione la opcion a realizar"))

    print(deSeccion)
    if(deSeccion > 3):
        os.system("cls")
        print("ERROR, ingrese un valor correspondiente a la seccion")
        input("Enter para continuar")
    elif(deSeccion ==1):
        os.system("cls")
        print("-------      Operadores      -------")
        print("------------------------------------")
        print("1. Calcular el area de un triangulo")
        print("2. Suma de dos numeros")
        print("3. Ingresar un numero y elevarlo al cuadrado")
        print("4. De Euros a Dolares")
        print("5. Ingresar el lado de un cuadrado y calcular su area y perimetro")
        print("6. Determinar el area y volumen de un cilindro")
        print("7. Calcular el radio de una circunferencia ")
        print("8. Calcular el promedio de tres numeros")
        print("99. Salir del programa")

        if(deSeccion == 1):
            print("Ingrese la opcion que desea: ")
            deOp = input("")
            if(deOp == "1"):
                os.system("cls")
                print("------- CALCULO AREA DE UN TRIANGULO------")
                print("------------------------------------------")
                base = int(input("Ingrese la base del triangulo: "))
                altura = int(input("Ingrese la altura del triangulo: "))
                resultado = (base * altura)/2
                print(f"El area del triangulo es: {resultado}")

                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")

            if(deOp == "2"):
                os.system("cls")
                print("-------- SUMA --------")
                print("----------------------")
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                suma = num1 + num2
                print(f"La suma de los dos numeros es: {suma}")
                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            if(deOp == "3"):
                os.system("cls")
                print("------- Elevar un numero al Cuadrado -------")
                print("--------------------------------------------")
                num= int(input("Ingrese un numero para elevarlo al cuadrado: "))
                cua= num**2
                print(f"El numero ingresado {num} al cuadrado es: {cua}")
                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            if(deOp == "4"):
                os.system("cls")
                print("--------- Conversor de Euros a Dolares ---------")
                print("------------------------------------------------")
                num = float(input("Ingrese la cantidad para realizar la conversion: "))
                con = num * 1.10140
                print(f"La conversion de la divisa euros a dolares es: {round(con,2)}")
                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            if(deOp == "5"):
                os.system("cls")
                print("----- Calcular el area y perimetro de un cuadrado -----")
                print("-------------------------------------------------------")
                lado = int(input("Ingrese el lado del cuadrado: "))
                area = lado * lado
                for i in range(2):
                    lado = lado + lado
                print(f"El area del cuadrado es: {area}")
                print(f"El perimetro del cuadrado es: {lado}")
                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            if(deOp == "6"):
                os.system("cls")
                print("------- Calcular el area y volumen de un cilindro -------")
                print("---------------------------------------------------------")
                r = float(input("Ingrese el radio en cm de la circunferencia: "))
                h = float(input("Ingrese la altura del cilindro: "))
                a = (2*3.1416*(r*h)) + (2*3.1416*(r**2))
                print(f"El area del cilindro es: {round(a,2)} cm^2")
                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            if(deOp == "7"):
                os.system("cls")
                print("------- Calcular el promedio de tres numeros -------")
                print("----------------------------------------------------")
                numero1 = int(input("Ingrese el primer numero: "))
                numero2 = int(input("Ingrese el segundo numero: "))
                numero3 = int(input("INgrese el tercer numero: "))
                promedio = (numero1 + numero2 + numero3)/3
                print(f"El promedio de los tres numeros es: {round(promedio, 2)}")
                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            if(deOp == "99"):
                print("Programa finalizado")
                deOp = ""
                break
    elif (deSeccion == 2):
        os.system("cls")
        print("-------      Condicionales      -------")
        print("---------------------------------------")
        print("1. Saber si un numero es negativo o positivo")
        print("2. Saber cual es el mayor y cual es el menor con dos numeros")
        print("3. Saber cual es el mayor y el menor de tres numeros")
        print("4. Calcular dos numeros  si A es menor que B sumar y si no restar los numeros")
        print("5. Hallar el cociente entre dos numeros A Y B")
        print("6. Sumar dos numeros A y B si alguno de ellos es negativo, en caso contrario multiplicarlos")
        print("7. Determinar si un año es bisiesto o no ")
        print("99. Salir del programa")

        print("Ingrese la opcion que desea de la seccion de operadores: ")
        deOp = input("")

        if (deOp == "1"):
            os.system("cls")
            print("------- Determinar si un numero es negativo o positivo ------")
            print("-------------------------------------------------------------")

            numero = int(input("Ingrese el numero"))

            if (numero < 0):
                print(f"El numero {numero} es negativo ")

                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            elif(numero == 0 ):
                print(f"El numero {numero} es neutro")

                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            else:
                print(f"El numero {numero} es positivo ")

                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
        if(deOp == "2"):
            os.system("cls")
            print("--------- Calcular que numero es mayor y cual es menor ---------")
            print("----------------------------------------------------------------")

            numero1 = int(input("Ingrese el primer numero: "))
            numero2 = int(input("Ingrese el segundo numero: "))

            if (numero1 > numero2):
                print(f"El numero {numero1} es mayor que el numero {numero2} ")

                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            else:
                print(f"El numero {numero1} es menor que el numero {numero2} ")

                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
        if(deOp == "3"):
            os.system("cls")
            print("------- Calcular que numero es mayor y cual es menor de tres numeros -------")
            print("----------------------------------------------------------------------------")

            numero1 = int(input("Ingrese el primer numero: "))
            numero2 = int(input("Ingrese el segundo numero: "))
            numero3 = int(input("Ingrese el tercer numero: "))

            if(numero1 > numero2 and numero1 > numero3 ):
                print("")
                print(f"El numero {numero1} es el mayor")

                if(numero2 < numero1 and numero2 < numero3):
                    print(f"El numero menor es el {numero2}")
                elif(numero3 < numero1 and numero3 < numero2):
                    print(f"El numero menor es el {numero3}")
                
                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            elif(numero2 > numero1 and numero2 > numero3):
                print("")
                print(f"El numero {numero2} es el mayor")

                if(numero1 < numero2 and numero1 < numero3):
                    print(f"El numero menor es el {numero1}")
                elif(numero3 < numero2 and numero3 < numero1):
                    print(f"El numero menor es el {numero3}")
                
                print("")
                ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                if(ude == "2"):
                    print("")
                    print("Programa finalizado")
                    sp = 0
                else:
                    input("Enter para regresar al menu ")
            else:
                if(numero3 > numero1 and numero3 > numero2):
                    print("")
                    print(f"El numero {numero3} es el mayor")

                    if(numero1 < numero3 and numero1 < numero2):
                        print(f"El numero menor es el {numero1}")
                    elif(numero2 < numero3 and numero2 < numero1):
                        print(f"El numero menor es el {numero2}")

                    print("")
                    ude = input("¿Desea continuar? 1. SI / 2. NO: ")
                    if(ude == "2"):
                        print("")
                        print("Programa finalizado")
                        sp = 0
                    else:
                        input("Enter para regresar al menu ")
        if(deOp == "4"):
            os.system("cls")
            print("------- Calcular dos numeros  si A es menor que B sumar y si no restar los numeros -------")
            print("------------------------------------------------------------------------------------------")

            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))

            if(a < b):
                print(f"El numero {a} es menor que {b}, su suma es: ")
                
            else:
                print(f"El numero {a} es mayor que {b}, su resta es: ")
            print("")
            ude = input("¿Desea continuar? 1. SI / 2. NO: ")
            if(ude == "2"):
                print("")
                print("Programa finalizado")
                sp = 0
            else:
                input("Enter para regresar al menu ")
        if(deOp == "6"):

            os.system("cls")
            print("------- Sumar dos numeros A y B si alguno de ellos es negativo sumarlos, en caso contrario multiplicarlos -------")
            print("-----------------------------------------------------------------------------------------------------------------")

            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))

            if (a < 0 or b < 0):
                suma = a + b
                print(f"La suma es : {suma}")
                
            else:
                mul = a * b
                print(f"La multiplicacion es: {mul}")

            print("")
            ude = input("¿Desea continuar? 1. SI / 2. NO: ")
            if(ude == "2"):
                print("")
                print("Programa finalizado")
                sp = 0
            else:
                input("Enter para regresar al menu ")
        if(deOp == "99"):
            print("Programa finalizado")
            deOp = ""
            break
    elif(deSeccion == 3):
        os.system("cls")
        print("-------      Ciclos      -------")
        print("--------------------------------")
        print("1. Imprimir todos los múltiplos de 3 que hay entre 1 y 100.")
        print("2. Imprimir los números impares entre 0 y 100.")
        print("3. Imprimir los números pares del 1 al 100.")
        print("4. Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30.")
        print("5. Escribir un programa que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla.")
        print("6. Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente.")
        print("7. Sumar todos los números que se digitan por teclado mientras no sea cero. ")
        print("99. Salir del programa")

        print("Ingrese la opcion que desea de la seccion de operadores: ")
        deOp = input("")

        if (deOp == "1"):
            os.system("cls")
            print("------- Imprimir todos los múltiplos de 3 que hay entre 1 y 100 ------")
            print("----------------------------------------------------------------------")

            input("Enter para iniciar el claculo")

            print("Múltiplos de 3 entre 1 y 100:")  
            for i in range(1,101):  
                if i%3==0:
                    print(i)  

            print("")
            ude = input("¿Desea continuar? 1. SI / 2. NO: ")
            if(ude == "2"):
                print("")
                print("Programa finalizado")
                sp = 0
            else:
                input("Enter para regresar al menu ")
        if (deOp == "2"):
            os.system("cls")
            print("------- Imprimir los números impares entre 0 y 100 ------")
            print("---------------------------------------------------------")

            input("Enter para iniciar el claculo")

            numero=0

            print("Los numeros impares entre 0 y 100:")
            while numero<100:
                numero+=1
                if numero%2 != 0:
                    print(numero)
            
            print("")
            ude = input("¿Desea continuar? 1. SI / 2. NO: ")
            if(ude == "2"):
                print("")
                print("Programa finalizado")
                sp = 0
            else:
                input("Enter para regresar al menu ")
        if(deOp == "3"):
            os.system("cls")
            print("------- Imprimir los números pares entre 1 y 100 ------")
            print("--------------------------------------------------------")

            input("Enter para iniciar el claculo")

            numero=1

            print("Los numeros pares entre 1 y 100:")
            while numero<100:
                numero+=1
                if numero%2 == 0:
                    print(numero)
            
            print("")
            ude = input("¿Desea continuar? 1. SI / 2. NO: ")
            if(ude == "2"):
                print("")
                print("Programa finalizado")
                sp = 0
            else:
                input("Enter para regresar al menu ")
        if(deOp == "4"):
            os.system("cls")
            print("------- Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 ------")
            print("-----------------------------------------------------------------------------------------------------")
            s = 0

            for i in range(1,30):
                c=0
                c= i **2
                s = s+c
                print(f"El Cuadrado es: {c}")
            print(f"La suma de los cuadrados es: {s}")
            print("")
            ude = input("¿Desea continuar? 1. SI / 2. NO: ")
            if(ude == "2"):
                print("")
                print("Programa finalizado")
                sp = 0
            else:
                input("Enter para regresar al menu ")
        if(deOp == "5"):
            os.system("cls")
            print("------- Escribir un programa que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla ------")
            print("-----------------------------------------------------------------------------------------------------")

            s = 0

            for i in range(1,101):
                c=0
                c= i **2
                s = s+c
            print(f"La suma de los cuadrados es: {s}")
            print("")
            ude = input("¿Desea continuar? 1. SI / 2. NO: ")
            if(ude == "2"):
                print("")
                print("Programa finalizado")
                sp = 0
            else:
                input("Enter para regresar al menu ")
        if(deOp == "7"):
            os.system("cls")
            print("------- Sumar todos los números que se digitan por teclado mientras no sea cero. ------")
            print("---------------------------------------------------------------------------------------")

            a = int(input("¿Cuantos numeros desea ingresar? "))
            for i in range(a):
                i = i+1 
                n = int(input(f"Ingrese el numero {i}: "))
                n = n+n
            print(f"La suma es: {n}")
            
            print("")
            ude = input("¿Desea continuar? 1. SI / 2. NO: ")
            if(ude == "2"):
                print("")
                print("Programa finalizado")
                sp = 0
            else:
                input("Enter para regresar al menu ")
        if(deOp == "99"):
            print("Programa finalizado")
            deOp = ""
            break


