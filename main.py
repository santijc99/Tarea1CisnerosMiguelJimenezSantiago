# Tarea 1 de Microprocesadores y Microcontroladores}
# ERR9x2 -4

def check_char(crt):
    resultado = 1  # definción de variable del resultado
    # chequea que el termino introducido sea un string
    if type(crt) == str or type(crt) == chr:
        # confirmar que solo se trate de un único carácter
        if (len(crt) > 1):
            print("ERROR: MTC \n"
                  "More than one character \n")
            resultado = 1
            return resultado
        # checa que sea un caractér entre A-Z
        if (65 <= ord(crt) <= 90) or (97 <= ord(crt) <= 122):
            print("No Error\n"
                  "El cáracter introducido está entre A y Z \n"
                  )
            resultado = 0
            return resultado
        else:  # Si es un caracter fuera de A-Z retorna un error y 1
            print("ERROR: CNP \n" "Character not permitted \n")
            resultado = 1
            return resultado
    else:
        resultado = 1
        print("ERROR: PNS \n" "Parameter not a string or a character \n")
        return resultado


def caps_switch(crt):
    res = check_char(crt)
    if(res == 0):  # el caracter es válido
        if (ord(crt) >= 65 or ord(crt) <= 90):  # es una letra mayúscula
            print("El caractér introducido es:\n" + crt + "\n")
            crt = crt.swapcase()  # se pasa a minuscula
            print("El nuevo caractér es:\n" + crt + "\n")
            return res
        elif (ord(crt) >= 97 or ord(crt) <= 122):  # letra minúscula
            print("El caractér introducido es:\n" + crt + "\n")
            crt = crt.swapcase()  # se pasa a minuscula
            print("El nuevo caractér es:\n" + crt + "\n")
            return res
        else:
            return res
