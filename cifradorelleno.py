import binascii
from random import getrandbits

#funciones
def convertir_a_bits(text, encoding='utf-8', errors='surrogatepass'):
    """función convertir_a_bits recibe como parámetro un texto y retorna su equivalente en binario"""
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def generar_relleno_aleatorio(n):
    """función generar_relleno_aleatorio recibe como parámetro la longitud de un binario y genera otro binario de igual longitud"""
    return bin(getrandbits(n))[2:].zfill(n)


def xor(m, k):
    """funcion xor recibe como parametro 2 valores que pueden ser la llave y"""
    a = int(m, base=2)
    b = int(k, base=2)
    return bin(a ^ b)[2:].zfill(len(m))


def convertir_bits_a_texto(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return bytes_a_int(n).decode(encoding, errors)


def bytes_a_int(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

####################################################
continuar='s'

while(continuar == 's'):

    print('CIFRADO DE RELLENO DE UNA SOLA VEZ \n'
          '¿Desea cifrar(c) o descifrar(d) su mensaje? : ')
    opcion = input()

    while(opcion.upper() != 'C' and opcion.upper() != 'D'):
        opcion = input('ingrese un valor correcto: ')




    if(opcion.upper() == 'C'):
        print('\n ---------------cifrado--------------------------')
        mensaje = input('Ingrese su mensaje a cifrar: ')
        bits = convertir_a_bits(mensaje)
        relleno = generar_relleno_aleatorio(len(bits))
        mensaje_cifrado = xor(bits,relleno)
        print('su mensaje es: '+mensaje)
        print('su mensaje en bits es: ' + bits)
        print('el relleno que se usó es: ' + relleno)
        print('su mensaje cifrado es: ' + mensaje_cifrado)
    else:
        print('\n ------------------descifrado-----------------------')
        mensaje_bits = input('Ingrese su mensaje cifrado en bits: ')
        relleno_mensaje = input('Ingrese el relleno del mensaje: ')
        bits_originales = xor(relleno_mensaje, mensaje_bits)
        mensaje_descifrado = convertir_bits_a_texto(bits_originales)
        print('su mensaje es: ' + mensaje_descifrado)
        print('su mensaje en bits es: ' + bits_originales)
    continuar = input("desea continuar si(s) no(otra tecla): ")
