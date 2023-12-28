#Main Program
import pickle
from personClass import *

def agregarPersona(objeto, filename='mainFile'):
    try:
        with open(filename, 'ab') as file:
            pickle.dump(objeto, file)
        print(f'La persona {objeto.name} fue guardada correctamente en {filename}')
    except Exception as e:
        print(f'Error al guardar la persona es {filename}: {e}')

def cargarPersonas(filename='mainFile'):
    objetos=[]
    try:
        with open(filename, 'rb') as file:
            while True:
                try:
                    actual_data=pickle.load(file)
                    objetos.append(actual_data)
                except EOFError:
                    break
        return objetos
    except Exception as e:
        print(f'Error al cargar personas desde {filename}: {e}')            
        return []
    

persona1=person('Juan', 'Masculino', 30)

persona2=person('Ana', 'Femenino', 25)

agregarPersona(persona1)
agregarPersona(persona2)