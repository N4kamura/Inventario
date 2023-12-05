'''
Esta version es nada más que de prueba
'''
from PIL import Image, ImageDraw,ImageFont
import barcode
from barcode import EAN13
from barcode.writer import ImageWriter

data='123456789012'
file_path="imagenes/imagen_"+data+".png"

ean=EAN13(data,writer=ImageWriter())

ean.save(file_path)

'''
Lluvia de ideas
Marca
Unidad de uso
Ubicación Física
Lote ¿?
Fecha Venc.
Stock Físico = 400
Stock Actual = 456
Cantidad de más = 0
Cantidad de menos = 456-500 = 0
Cantidad Buena
Cantidad Mala

También se podría mandar a imprimir un reporte. Pero no seas tan cochino aún.

Crear el ingreso manual en caso no se pueda ver.
Y de allí que detectando su nombre y características únicas, que proceda
a colocar datos como los de arriba de manera manual.

También debe estar el caso de confirmar o de eliminar.

Ya si eres sucio, colocas una imagen pequeña para saber cómo es.

'''