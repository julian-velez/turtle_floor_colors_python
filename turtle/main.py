from turtle import *        # Importa todas las funciones de turtle para dibujar
from colorsys import *     # Importa funciones para trabajar con colores (HSV a RGB)

tracer(300)                # Acelera la animación (menos renderizado en pantalla)
bgcolor('black')           # Establece el fondo de la ventana en negro
hideturtle()               # Oculta la flecha (cursor) de la tortuga
pensize(2)                 # Define el grosor del lápiz

# Bucle principal que controla el crecimiento del dibujo
for i in range(200):
    # Cambia el color dinámicamente usando HSV (efecto arcoíris)
    color(hsv_to_rgb(i / 300, 0.9 , 1))

    # Primer patrón repetitivo
    for j in range(8):
        forward(i * 0.8)   # Avanza una distancia proporcional a i (crece con el tiempo)
        right(180)         # Gira 180 grados (da media vuelta)
        right(20)          # Gira 20 grados adicionales (crea curvatura/espiral)

        # Segundo patrón interno (más pequeño)
        for j in range(8):
            forward(i * 0.3)  # Avanza una distancia menor (detalle interno)
            left(70)          # Gira a la izquierda 70 grados
            right(40)         # Luego gira a la derecha 40 grados (ángulo neto 30°)

done()  # Mantiene la ventana abierta al finalizar el dibujo