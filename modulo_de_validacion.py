def solicitud_y_verificacion_de_palabra(cantidad_de_letras):
   while True:
      palabra_ingresada = input("Ingrese una palabra: ")
      if len(palabra_ingresada) != cantidad_de_letras:
         print("Por favor, ingrese una palabra de 5 letras")
      else:
         break 
   return palabra_ingresada