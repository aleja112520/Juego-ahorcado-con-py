##Se le pedirá al jugador 1 ingresar la pablabra a adivinar
##luego, se le dirá al jugador 2 que ingrese letras con el fin de ponerlas en la palabra, 
##el juego se guardará en un archivo de texto y se tratarán excepciones
from io import open
import os

name_archivo="ahorcado.txt"
if os.path.isfile(name_archivo)==False:
    archivo=open("ahorcado.txt","w")
def comparar(tamaño,palabra_ini,palabra,letra):
    palabrax=[letra if (letra==palabra[x]) else '*' for x in range(tamaño)]
    palabra_final=[palabra[i] if (palabrax[i]!='*') or (palabra_ini[i]!='*') else '*' for i in range(tamaño)]
    return palabra_final
def vidas(num_vidas,palabra_anterior,nueva_palabra):
    if nueva_palabra==palabra_anterior:
        num_vidas=num_vidas-1
    else:
        num_vidas=num_vidas
    return num_vidas

if __name__ == '__main__':
    archivo=open("ahorcado.txt","r")
    texto=archivo.readlines()
    #print(texto)
    if texto!=[] and (texto[-4]=="PERDIO\n" or texto[-4]=="GANO\n"):
        palabra=list(input("Jugador 1: Ingresa la palabra \n"))
        num_vidas=5
        tamaño=len(palabra)
    elif texto!=[] and texto[-4]=="\n":
        pala=list(texto[-3])
        palabra=[]
        for x in range(len(pala)-1):
            palabra.append(pala[x])
        print("Palabra en juego anterior: "+ texto[-2])
        tamaño=len(palabra)
        num_vidas=int(texto[-1])
    elif texto==[]:
        palabra=list(input("Jugador 1: Ingresa la palabra \n"))
        num_vidas=5
        tamaño=len(palabra)
    archi=open("ahorcado.txt","a")
    try:
        for x in range(tamaño):
            assert (palabra[x]!="0" and palabra[x]!="1" and palabra[x]!="2" and palabra[x]!="3" and palabra[x]!="4"
            and palabra[x]!="5" and palabra[x]!="6" and palabra[x]!="7" and palabra[x]!="8" and palabra[x]!="9")
        palabrax=['*' for x in range(tamaño)]
        while num_vidas>=1:
            try:
                letra=input("Jugador 2: Ingresa una letra \n")
                assert (letra!="0" and letra!="1" and letra!="2" and letra!="3" and letra!="4" and letra!="5"
                and letra!="6" and letra!="7" and letra!="8" and letra!="9")                   
                letra_list=list(letra)
                if len(letra_list)>1:
                    raise TypeError
                print(comparar(tamaño,palabrax,palabra,letra))
                num_vidas=vidas(num_vidas,palabrax,comparar(tamaño,palabrax,palabra,letra))
                print("Numero de vidas: ",num_vidas)
                palabrax=comparar(tamaño,palabrax,palabra,letra)
                if palabrax==palabra:
                    print("Has ganao ti@")
                    archi.write("GANO")
                    break
            except (TypeError):
                print("Ingresó más de una letra ome")
                break
        if num_vidas<1:
            print("Has perdido mi querid@ amig@") 
            archi.write("PERDIO")
    except (AssertionError):
        print("Ingresaste un número mij@")
    finally:
        palabra_st=""
        for x in range(len(palabra)):
            palabra_st=palabra_st+str(palabra[x])
        archi.write("\n"+palabra_st+ "\n")
        archi.write(str(palabrax) + "\n")
        archi.write(str(num_vidas)+"\n")