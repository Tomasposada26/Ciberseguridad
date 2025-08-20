def cifrar(texto, clave):
    """Cifra el texto usando el cifrado César."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            inicio = ord('a') if char.islower() else ord('A')
            alfabeto_len = 26
            indice_original = ord(char) - inicio
            indice_cifrado = (indice_original + clave) % alfabeto_len
            resultado += chr(inicio + indice_cifrado)
        else:
            resultado += char
    return resultado

def descifrar(texto, clave):
    """Descifra el texto usando el cifrado César."""
    return cifrar(texto, -clave)

def main():
    """Función principal que maneja la interacción con el usuario."""
    print("--- Cifrador y Descifrador César ---")
    
    texto_cifrado_anterior = None
    
    while True:
        modo = input("¿Qué desea hacer? (c/d para cifrar/descifrar): ").lower()
        
        if modo not in ['c', 'd']:
            print("Opción no válida. Por favor, escriba 'c' o 'd'.")
            continue

        if modo == 'c':
            # Solicita el mensaje y la clave para cifrar
            mensaje = input("Ingrese el mensaje a cifrar: ")
            
            while True:
                try:
                    clave = int(input("Ingrese la clave numérica (un entero): "))
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número entero.")
            
            texto_cifrado = cifrar(mensaje, clave)
            print(f"Mensaje cifrado: {texto_cifrado}")
            
            # Guarda el texto cifrado y la clave para la siguiente operación
            texto_cifrado_anterior = texto_cifrado
            
        elif modo == 'd':
            # Si hay un texto cifrado de la operación anterior, lo usa automáticamente
            if texto_cifrado_anterior:
                print(f"Usando el texto cifrado de la operación anterior: {texto_cifrado_anterior}")
                texto_a_descifrar = texto_cifrado_anterior
                
                while True:
                    try:
                        clave = int(input("Ingrese la clave numérica que usó para cifrar: "))
                        break
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número entero.")
                
                texto_descifrado = descifrar(texto_a_descifrar, clave)
                print(f"Mensaje descifrado: {texto_descifrado}")
            else:
                # Si no hay texto anterior, pide al usuario que ingrese el texto y la clave
                mensaje_a_descifrar = input("Ingrese el mensaje a descifrar: ")
                
                while True:
                    try:
                        clave = int(input("Ingrese la clave numérica: "))
                        break
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número entero.")
                
                texto_descifrado = descifrar(mensaje_a_descifrar, clave)
                print(f"Mensaje descifrado: {texto_descifrado}")
                
        continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()