def verificar_rut(rut):
    
    if(len(rut)<=10):
        rut_lista = rut.split('-')
        if(len(rut_lista)==2):
            try:
                valor = int(rut_lista[0])
                aux = []
                ingresar = [aux.append(numeros) for numeros in rut_lista[0]]
                aux.reverse()
                recorrido = 2
                multiplicar = 0
                for x in aux:
                    multiplicar+=int(x)*recorrido
                    if recorrido==7: 
                        recorrido = 1
                    recorrido+=1
                    modulo = multiplicar%11
                    resultado = 11-modulo
                    if resultado == 11: 
                        digito=0
                    elif resultado == 10: 
                        digito="K"
                    else: 
                        digito=resultado
                if(str(digito).lower() == rut_lista[1].lower()):
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False
    else:
        return False
