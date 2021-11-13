import pyzipper


comprimido = pyzipper.AESZipFile('tarea.zip', 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES)


archivo = open('listado-general.txt', 'rb')

for linea in archivo:
    try:
        datos = comprimido.extract('secreto.txt',pwd=linea)
    except RuntimeError:
        pass
    except:
        print('Contraseña %s correcta' % linea)
        break

        

archivo.close()
comprimido.close()