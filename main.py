import random
import time

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET ='\033[39m'
iniciar_trivia = True
intentos = 0
#puntaje = random.randint (0,10)
puntaje = 0
print(GREEN+"Bienvenido a la Trivia Metalera\n"+RESET)
time.sleep(1)
nombre = input(BLUE+"¿Cual es tu nombre? "+CYAN)

print("")
while nombre in (""," ","  "):
    nombre = input(BLUE+"Debes colocar un nombre: ")
time.sleep(1)
print(BLUE+"\nHola", CYAN+nombre, BLUE+"tengo un desafio para ti")
time.sleep(2)
print("\nPondremos a prueba tus conocimientos para saber si eres un verdadero metalero lml, comenzaras con", puntaje, "puntos, recuerda que respuesta acertada te suma y respuesta incorrecta te resta puntos dependiendo de la dificultad de la pregunta.")
time.sleep(1)
while iniciar_trivia == True:
  intentos+=1
  puntaje = 0
  lista_puntos = [] 
  print(BLUE+"\nResponde las siguientes preguntas escribiendo la letra de la alternativa correcta y presiona  'Enter' para enviar tu respuesta, comenzamos:\n")
  print("Intento número: ", intentos)
  time.sleep(1)
  input("\nPresiona enter para continuar...")
  for numero_carga in range (5,0,-1):
    print(numero_carga)
    time.sleep(1)
  #Pregunta 01
  print(GREEN+"\n1) ¿Cuál es la banda autora del tema 'Paranoid' de 1970?\n"+RESET)
  print(YELLOW+"a) Megadeth")
  print("b) Black Sabbath")
  print("c) Iron Maiden")
  print("d) Annihilator"+RESET)
  respuesta_1 = input(YELLOW+"\n Tu respuesta: "+MAGENTA).lower()
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input(BLUE+"Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  if respuesta_1 == "b":
    puntaje += 10
    lista_puntos.append(10)
    time.sleep(1)
    print(BLUE+"\nEs correcto, iniciamos con pie derecho", CYAN+nombre+BLUE)
    print (CYAN+nombre+BLUE, "tienes", puntaje, "puntos acumulados")
  else:
    puntaje -= 10
    lista_puntos.append(-10)
    print(RED+"\n¡Incorrecto!"+BLUE)
    print (nombre, "tienes", puntaje, "puntos acumulados") 
  input("\nPresiona enter para continuar...")
  
  # Pregunta 02
  print(GREEN+"\n2) ¿Quien popularizo el simbolo de la mano cornuda dentro del heavy metal?\n"+YELLOW)
  print("a) James Hetfield")
  print("b) Paul McCartney")
  print("c) Ronnie James Dio")
  print("d) Ozzy Osbourne")
  respuesta_2 = input("\n Tu respuesta: "+MAGENTA).lower()
  #Agregaremos una respuesta secreta, si el usuario ingresa lml
  while respuesta_2 not in ("a","b","c","d","lml"):
    respuesta_2 = input(BLUE+"Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  if respuesta_2 == "a":
    lista_puntos.append(-10)
    puntaje -= 10
    print(RED+"\n¡Incorrecto!, el vocalista de Metallica no lo fue ")
  elif respuesta_2 == "b":
    lista_puntos.append(-10)
    puntaje -= 10
    print(RED+"\n¡Incorrecto!, formo parte del cuarteto de Liverpool,pero no fue él")
  elif respuesta_2 == "d":
    lista_puntos.append(-10)
    puntaje -= 10
    print(RED+"\n¡Incorrecto!, estuviste cerca", CYAN+nombre+RED)
  elif respuesta_2 == "lml":
    lista_puntos.append(100)
    puntaje += 100
    time.sleep(2)
    print(YELLOW+"\nQue sorpresa..., encontraste el codigo secreto, como recompensa te dare la respuesta y una bonificacion de 100 puntos, Ronnie James Dio lo hizo, una de las más grandes e importantes figuras del heavy metal de todos los tiempos, como dato curioso aparece en la pelicula 'Tenacious D in The Pick of Destiny' con Jack Black\n")
  else:
    lista_puntos.append(10)
    puntaje += 10
    time.sleep(1)
    print(BLUE+"\n!Muy Bien", CYAN+nombre+BLUE, "acertaste, Ronnie James Dio lo popularizo  influenciado por una superstición de su abuela")
  print (CYAN+nombre, BLUE+"tienes", puntaje, "puntos acumulados")
  input("\nPresiona enter para continuar...")
    
  #Pregunta 03
  print(GREEN+"\n3) Es considerado el festival de Metal mas grande del mundo: \n"+YELLOW)
  print("a) Wacken")
  print("b) Live Aid")
  print("c) Woodstock")
  print("d) M'era Luna")
  respuesta_3 = input("\n Tu respuesta: "+MAGENTA).lower()
  while respuesta_3 not in ("a","b","c","d"):
    respuesta_3 = input(BLUE+"Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  if respuesta_3 == "a":
    puntos_3 = random.randint (10, 20)
    lista_puntos.append(puntos_3)
    puntaje += puntos_3
    time.sleep(1)
    print(BLUE+"\n¡Correcto!, uno de los festivales más grandes realizado en Alemania") 
  else:
    puntaje -= 10
    lista_puntos.append(-10)
    print(RED+"\n¡Incorrecto!,",nombre)
  print (BLUE+nombre, "tienes", puntaje, "puntos acumulados")
  input("\nPresiona enter para continuar...")
  
  #Pregunta 04
  print(BLUE+"\nPara esta parte tendremos una pregunta especial, dependiendo cuan cerca estes a la  respuesta te asignaremos un puntaje especial, ¡Buena Suerte! ")
  print(GREEN+"\n4)¿Cual de estas es la banda de Metal Sinfónico mas reconocida a nivel mundial?\n"+YELLOW)
  print("a) Mana")
  print("b) Hamadria")
  print("c) Opeth")
  print("d) Therion")
  respuesta_4 = input("\n Tu respuesta: "+MAGENTA).lower()
  while respuesta_4 not in ("a","b","c","d"):
    respuesta_4 = input(BLUE+"Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  if respuesta_4 == "a":
    if puntaje <= 0:
      lista_puntos.append("puntaje*2")
      puntaje = puntaje*2
    else:
      lista_puntos.append("puntaje/2")
      puntaje = puntaje/2
    time.sleep(1)
    print(RED+"\nIncorrecto, estamos muy lejos",nombre+BLUE)
  elif respuesta_4 == "b":
    lista_puntos.append(-5)
    puntaje -= 5 
    print(RED+"\nNo, Hamadria es una banda Peruana de Heavy Metal, mas no de Metal sinfonico")
  elif respuesta_4 == "c":
    lista_puntos.append(5)
    puntaje += 5
    print(RED+"\n¡Incorrecto!, si son reconocidos pero hacen metal progresivo")
  else:
    if puntaje <= 0:
      lista_puntos.append(20)
      puntaje+=20
    else:
      lista_puntos.append(puntaje)
      puntaje = puntaje*2
    time.sleep(1)
    print(BLUE+"\nCorrecto, esta banda sueca creada en 1987 es una de las más reconocidas dentro del metal sinfónico")
  print (BLUE+nombre, "tienes", puntaje, "puntos acumulados")
  input("\nPresiona enter para continuar...")

  #Pregunta 05; en esta pregunta aplicaremos listas y ciclos
  print(GREEN+"\n5)¿Cual es el nombre de la mascota de Megadeth?\n")
  time.sleep(1)
  letra_opcion = ["a)","b)","c)","d)"]
  opciones_p6 = ["Jack O Lantern","Eddie The Head","Vic Rattlehead","Murray"]
  for number in range (0,4):
    print(YELLOW+letra_opcion[number],opciones_p6[number])
  respuesta_5 = input("\n Tu respuesta: "+MAGENTA).lower()
  while respuesta_5 not in ("a","b","c","d"):
    respuesta_5 = input(BLUE+"Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  if respuesta_5 == "c":
    puntaje+=10
    lista_puntos.append(10)
    print(BLUE+"\n¡Correcto!") 
  else:
    puntaje-=10
    lista_puntos.append(-10)
    print(RED+"\n¡Incorrecto!,",nombre)
  print (BLUE+nombre, "tienes", puntaje, "puntos acumulados")
  input("\nPresiona enter para continuar...")

    #Pregunta 06
  print("\nLa pregunta final es la siguiente", nombre,"...")
  time.sleep(2)
  print(GREEN+ "\n6) ¿Hoy estas con suerte?")
  print(YELLOW+"\na) SI")
  print("b) NO")
  respuesta_6 = input("\n Tu respuesta: "+MAGENTA).lower()
  while respuesta_6 not in ("a","b"):
    respuesta_6 = input(BLUE+"Debes responder a o b. Ingresa nuevamente tu respuesta: ").lower()
  time.sleep(1)
  print(BLUE+"La pondremos a prueba, haremos girar una ruleta por 8 segundos y el valor que salga se aumentara a tu puntaje final")
  input("\nPresiona enter para girar...")
  for conteo_ruleta in range(8,0,-1):
    print(conteo_ruleta)
    time.sleep(1)
  ruleta = random.randint(0,100)
  lista_puntos.append(ruleta)
  time.sleep(1)
  print("Obtuviste", ruleta, "puntos extras")
  puntaje=puntaje+ruleta
  time.sleep(2)
#Agregamos una lista detallada del puntaje por pregunta 
  print(YELLOW+"Puntaje obtenido por pregunta")
  print("Intento: ", intentos)
  lista_pregunta = ["p1","p2","p3","p4","p5","p6"]
  print(lista_pregunta)
  print(lista_puntos)
  print(MAGENTA+nombre, "alcanzaste", puntaje ,"puntos en total.")
  print(GREEN +"\n¿Deseas intentar la Trivia nuevamente")
  repetir_trivia = input("Ingresa 'si' para repetir o cualquier tecla para finalizar: ").lower()
  if repetir_trivia == "si":
    print("\033c", end="")
  elif repetir_trivia != "si":
    print(MAGENTA+"\nGracias por jugar la Trivia Metalera, espero que lo hayas pasado bien, ¡hasta pronto!"+RESET)
    iniciar_trivia = False
    
