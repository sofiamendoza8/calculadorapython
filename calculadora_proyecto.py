from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA")
i=0
#entrada
e_texto=Entry(ventana, font= ("Calibri 60"))
e_texto.grid(row = 0, column= 0, columnspan = 4, padx = 5, pady = 5)
#funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
def borrar():
    e_texto.delete(0, END)
    i = 0
def calculo_operaciones():
    ecuacion = e_texto.get()
    resultado=eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0,resultado)
    i = 0


#botones 
boton1=Button(ventana, text = "1", width = 20, height = 3, command= lambda:click_boton(1))
boton2=Button(ventana, text = "2", width = 20, height = 3, command= lambda:click_boton(2))
boton3=Button(ventana, text = "3", width = 20, height = 3, command= lambda:click_boton(3))
boton4=Button(ventana, text = "4", width = 20, height = 3, command= lambda:click_boton(4))
boton5=Button(ventana, text = "5", width = 20, height = 3, command= lambda:click_boton(5))
boton6=Button(ventana, text = "6", width = 20, height = 3, command= lambda:click_boton(6))
boton7=Button(ventana, text = "7", width = 20, height = 3, command= lambda:click_boton(7))
boton8=Button(ventana, text = "8", width = 20, height = 3, command= lambda:click_boton(8))
boton9=Button(ventana, text = "9", width = 20, height = 3, command= lambda:click_boton(9))
boton0=Button(ventana, text = "0", width = 30, height = 3, command= lambda:click_boton(0))


boton_borrar=Button(ventana, text = "AC", width = 20, height = 3, command= lambda:borrar())
boton_PAREVTESIS1=Button(ventana, text = "(", width = 20, height = 3, command= lambda:click_boton("("))
boton_PARENTESIS2=Button(ventana, text = ")", width = 20, height = 3, command= lambda:click_boton(")"))
boton_PUNTO=Button(ventana, text = ".", width = 20, height = 3, command= lambda:click_boton("."))

boton_DIVISION=Button(ventana, text = "/", width = 20, height = 3, command= lambda:click_boton("/"))
boton_MULTIPLICACION=Button(ventana, text = "x", width = 20, height = 3, command= lambda:click_boton("*"))
boton_SUMA=Button(ventana, text = "+", width = 20, height = 3, command= lambda:click_boton("+"))
boton_RESTA=Button(ventana, text = "-", width = 20, height = 3, command= lambda:click_boton("-"))
boton_IGUAL=Button(ventana, text = "=", width = 20, height = 3, command= lambda:calculo_operaciones())

#AGREGAR BOTONES
# fila 1
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_PAREVTESIS1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_PARENTESIS2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_DIVISION.grid(row = 1, column = 3, padx = 5, pady = 5)

#fila 2
boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1 , padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_MULTIPLICACION.grid(row = 2, column = 3, padx = 5, pady =5)
 #fila 3
boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_SUMA.grid(row = 3, column = 3, padx = 5, pady = 5)

#fila 4
boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_RESTA.grid(row = 4, column = 3, padx = 5, pady = 5)

#fila 5
boton0.grid(row = 5, column = 0,columnspan = 2 , padx = 5, pady = 5)
boton_PUNTO.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_IGUAL.grid(row = 5, column = 3, padx = 5, pady = 5)


ventana.mainloop() 


