from os import replace, system

def judul():
    system('cls')
    print('======================')
    print('TEMPERATURE CONVERSION')
    print('======================')

def menu():
    judul()
    print('1. celcius')
    print('2. reamur')
    print('3. fahrenheit')
    print('4. kelvin')
    print('5. exit')
    choose2 = input('choose option number : ')
    if choose2 == '1':
        celcius()
    elif choose2 == '2':
        reamur()
    elif choose2 == '3':
        fahrenheit()
    elif choose2 == '4':
        kelvin()
    elif choose2 == '5':
        out()
    else:
        wrong()

def wrong():
    wrong1 = input('wrong input[enter]')
    menu()

def celcius():
    try:
        celcius_value = float(input('Enter number of celcius : '))
    except ValueError:
        error = input('wrong input, please retry')
        celcius()
    reamur = (4/5) * celcius_value
    fahrenheit = ((9/5)*celcius_value) + 32
    kelvin = celcius_value + 273

    print('=====result=====')
    print('reamur : ', reamur)
    print('fahrenheit : ', fahrenheit)
    print('kelvin : ', kelvin)
    print('==================')
    back = input('retry conversion? [y/n]')
    if back == 'y' or back == 'Y':
        celcius()

    else:
        menu()


def reamur():
    try:
        reamur_value = float(input('Enter number of reamur : '))
    except ValueError:
        error = input('wrong input, please retry')
        reamur()
    celcius = (5/4) * reamur_value
    fahrenheit = ((9/4)*reamur_value) + 32
    kelvin = ((5/4)*reamur_value) + 273

    print('=====result=====')
    print('celcius : ', celcius)
    print('fahrenheit : ', fahrenheit)
    print('kelvin : ', kelvin)
    print('==================')
    back = input('retry conversion? [y/n]')
    if back == 'y' or back == 'Y':
        reamur()

    else:
        menu()


def fahrenheit():
    try:
        fahrenheit_value = float(input('Enter number of fahrenheit : '))
    except ValueError:
        error = input('wrong input, please retry')
        fahrenheit()
    celcius = (5/9) * (fahrenheit_value - 32)
    reamur = (4/9) * (fahrenheit_value - 32)
    kelvin = ((5/9) * (fahrenheit_value - 32)) + 273

    print('=====result=====')
    print('celcius : ', celcius)
    print('reamur : ', reamur)
    print('kelvin : ', kelvin)
    print('==================')
    back = input('retry conversion? [y/n]')
    if back == 'y' or back == 'Y':
        fahrenheit()

    else:
        menu()


def kelvin():
    try:
        kelvin_value = float(input('Enter number of kelvin : '))
    except ValueError:
        error = input('wrong input, please retry')
        kelvin()
    celcius = kelvin_value - 273
    reamur = (4/5) * (kelvin_value - 273)
    fahrenheit = ((9/5) * (kelvin_value - 273)) + 32

    print('=====result=====')
    print('celcius : ', celcius)
    print('reamur : ', reamur)
    print('fahrenheit : ', fahrenheit)
    print('==================')
    back = input('retry conversion? [y/n]')
    if back == 'y' or back == 'Y':
        kelvin()

    else:
        menu()

def out():
    exit()
menu()
