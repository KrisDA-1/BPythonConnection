lenguajes=["Python", "Ruby", "PHP", "JavaScript", "Java"]
lenguajes.insert(2, "Go") ##inserta el elemento Go en la posición 2 de la lista
lenguajes.remove("PHP") ##elimina el elemento PHP de la lista
lenguajes.append("C++") ##añade el elemento C++ al final de la lista
print("PHP" in lenguajes) ##verifica si el elemento PHP está en la lista, devuelve True o False
lenguajes.clear() ##elimina todos los elementos de la lista
print(lenguajes) ##imprime toda la lista
print(len(lenguajes)) ##imprime la longitud de la lista, es decir, el número de elementos que tiene
lenguajes.sort() ##ordena la lista alfabéticamente