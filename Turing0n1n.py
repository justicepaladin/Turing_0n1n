def TuringOn1n(cod):
    cinta = list(cod)
    cinta = cinta + ['_','_'] #represento el espacio en blanco con un guión bajo
    estado = 0
    i = 0
    blank = ''
    # estado 4 -> estado de éxito
    # estado 5 -> estado de error
    while estado != 4 and estado != 5:
        if estado == 0:
            if cinta[i] == '0':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un 0 y lo cambio por X')
                cinta[i] = 'X'
            elif cinta[i] == 'X':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un X, cambio al estado 1 y me muevo a la derecha')
                estado = 1
                i+=1
            elif cinta[i] == 'Y':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un Y, cambio al estado 3 y me muevo a la derecha')
                estado = 3
                i
            elif cinta[i] == '1':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un 1 y voy al estado de error')
                estado = 5
            elif cinta[i] == '_':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un espacio y voy al estado de éxito')
                estado = 4
        elif estado == 1:
            if cinta[i] == '0':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un 0 y me muevo a la derecha')
                i+=1
            elif cinta[i] == '1':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un 1, lo cambio por Y y cambio al estado 2')
                cinta[i] = 'Y'
                estado = 2
            elif cinta[i] == 'Y':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un Y y me muevo a derecha')
                i+=1
            elif cinta[i] == '_':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un espacio y voy al estado de error')
                estado = 5
        elif estado == 2:
            if cinta[i] == '0':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un 0 y me muevo a la izquierda')
                i-=1
            elif cinta[i] == 'X':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un X, cambio al estado 0 y me muevo a la derecha')
                estado = 0
                i+=1
            elif cinta[i] == 'Y':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un Y y me muevo a la izquierda')
                i-=1
        elif estado == 3:
            if cinta[i] == 'Y':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un Y y me muevo a la derecha')
                i+=1
            elif cinta[i] == '_':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un espacio y voy al estado de éxito')
                estado = 4
            elif cinta[i] == '1':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un 1 y voy al estado de error')
                estado = 5
            #agrego haciendo prueba y error
            elif cinta[i] == '0':
                print(blank.join(cinta) + ' | Estoy en el estado ' + str(estado) + ', leo un 0 y voy al estado de error')
                estado = 5
        
    if estado == 4:
        print("La cadena es aceptada por la máquina de Turing")
    else:
        print("La cadena no es aceptada por la máquina de Turing")


cinta = '101'
TuringOn1n(cinta)