#
# Programa para tratar ficheros PDF.
#
# versión: 0.0.0
#
# Juan Francisco Ortuño Puche

from PyPDF2 import PdfReader, PdfWriter

lectura = PdfReader("Billetes_Madrid.pdf")
longitud = len(lectura.pages)
print (f"{longitud}")

if longitud > 1:
    i=0
    for pagina in lectura.pages:
        salida = PdfWriter()
        salida.add_page(pagina)
        fichero = "Billete"+str(i)+".pdf"
        print(f"Creando fichero {fichero} ")
        salida.write(f"Billete{i}.pdf")
        i+=1
    print (f"El fichero tenía {i} páginas.")
    print (f"Han sido creados {i} ficheros.")
else:
    print("Este fichero solo tiene 1 página.")