from tkinter import *
from tkinter import ttk,font
import tkinter as tk
from datetime import datetime
import requests


class Aplicacion():
    __window = None
    __actual = None
    list = []

    def __init__(self):
        self.__window = Tk()
        self.__window.geometry('299x278')
        self.__actual = StringVar()
        self.__window.resizable(0,0) # la ventana no se puede redimensionar
        self.__window.config(bg='#e4e8d1')

        '''FUENTES'''
        self.fuente1 = font.Font(family='Arial',weight = 'bold',size=11)
        self.fuente2 = font.Font(family='Arial',weight = 'normal',size=11)
        self.fuente3 = font.Font(family='Arial',weight = 'normal',size=10)
        
        '''Etiquetas'''
        self.etiqueta = tk.Label(self.__window,bg="#85bb65" )
        self.etiqueta.place(relwidth=1, relheight =0.14)

        self.etiqueta1=tk.Label(self.etiqueta,text="Moneda",bg='#85bb65',fg='white',font=self.fuente1)
        self.etiqueta1.place(x=10, y=7)
        self.etiqueta2=tk.Label(self.etiqueta,text="Compra",bg='#85bb65',fg='white',font=self.fuente1)
        self.etiqueta2.place(x=176, y=7)
        self.etiqueta3=tk.Label(self.etiqueta,text="Venta",bg='#85bb65',fg='white',font=self.fuente1)
        self.etiqueta3.place(x=241, y=7)
 
        '''Carga de variables'''
        self.cargar()
        dolar1 = Label(self.__window, text = self.list[0][0],font=self.fuente3,bg='#e4e8d1')
        dolar1C = Label(self.__window, text =  '$%s' %(self.list[0][1]),font=self.fuente3,bg='#e4e8d1')
        dolar1V = Label(self.__window, text =  '$%s' %(self.list[0][2]),font=self.fuente3,bg='#e4e8d1')

        dolar2 = Label(self.__window, text = self.list[1][0],font=self.fuente3,bg='#e4e8d1')
        dolar2C = Label(self.__window, text =  '$%s' %(self.list[1][1]),font=self.fuente3,bg='#e4e8d1')
        dolar2V = Label(self.__window, text =  '$%s' %(self.list[1][2]),font=self.fuente3,bg='#e4e8d1')

        dolar3 = Label(self.__window, text = self.list[2][0],font=self.fuente3,bg='#e4e8d1')
        dolar3C = Label(self.__window, text =  '$%s' %(self.list[2][1]),font=self.fuente3,bg='#e4e8d1')
        dolar3V = Label(self.__window, text =  '$%s' %(self.list[2][2]),font=self.fuente3,bg='#e4e8d1')

        dolar4 = Label(self.__window, text = self.list[3][0],font=self.fuente3,bg='#e4e8d1')
        dolar4C = Label(self.__window, text =  '$%s' %(self.list[3][1]),font=self.fuente3,bg='#e4e8d1')
        dolar4V = Label(self.__window, text =  '$%s' %(self.list[3][2]),font=self.fuente3,bg='#e4e8d1')

        dolar5 = Label(self.__window, text = self.list[4][0],font=self.fuente3,bg='#e4e8d1')
        dolar5C = Label(self.__window, text =  self.list[4][1],font=self.fuente3,bg='#e4e8d1')
        dolar5V = Label(self.__window, text =  '$%s' %(self.list[4][2]),font=self.fuente3,bg='#e4e8d1')

        dolar6 = Label(self.__window, text = self.list[5][0],font=self.fuente3,bg='#e4e8d1')
        dolar6C = Label(self.__window, text = '$%s' % (self.list[5][1]),font=self.fuente3,bg='#e4e8d1')
        dolar6V = Label(self.__window, text = '$%s'%(self.list[5][2]),font=self.fuente3,bg='#e4e8d1')
        
        '''SEPARADORES'''
        self.line_style = ttk.Style()
        self.line_style.configure("Line.TSeparator", background="#85bb65")
        self.line = ttk.Separator(self.__window, orient=HORIZONTAL, style="Line.TSeparator")
        self.line2 = ttk.Separator(self.__window, orient=HORIZONTAL, style="Line.TSeparator")
        self.line3= ttk.Separator(self.__window, orient=HORIZONTAL, style="Line.TSeparator")
        self.line4 = ttk.Separator(self.__window, orient=HORIZONTAL, style="Line.TSeparator")
        self.line5 = ttk.Separator(self.__window, orient=HORIZONTAL, style="Line.TSeparator")
        self.line6 = ttk.Separator(self.__window, orient=HORIZONTAL, style="Line.TSeparator")

        '''Botones'''
        boton = Button(self.__window, text = 'ACTUALIZAR', command = self.actualizar,fg='white',bg='#0c9f59')
        
        text4 = Label(self.__window, textvariable = self.__actual,bg='#e4e8d1',font=self.fuente3)
        fecha = datetime.now()
        self.__actual.set(f'Actualizado {fecha.day}/{fecha.month}/{fecha.year} {fecha.hour}:{fecha.minute}')
 
        '''Posicion Place'''
        dolar1.place(x=14,y=40)
        dolar1C.place(x=185,y=40)
        dolar1V.place(x=240,y=40)

        dolar2.place(x=14,y=70)
        dolar2C.place(x=180,y=70)
        dolar2V.place(x=240,y=70)

        dolar3.place(x=14,y=100)
        dolar3C.place(x=180,y=100)
        dolar3V.place(x=240,y=100)        

        dolar4.place(x=14,y=130)
        dolar4C.place(x=180,y=130)
        dolar4V.place(x=240,y=130)

        dolar5.place(x=14,y=160)
        dolar5C.place(x=180,y=160)
        dolar5V.place(x=240,y=160)   

        dolar6.place(x=14,y=190)
        dolar6C.place(x=180,y=190)
        dolar6V.place(x=240,y=190)      
      
        '''POSICION SEPARADORES'''
        self.line.place(relx=0,y=65,relwidth=1,width = 8 )
        self.line2.place(relx=0,y=95,relwidth=1,width = 8 )
        self.line3.place(relx=0,y=125,relwidth=1,width = 8 )
        self.line4.place(relx=0,y=155,relwidth=1,width = 8 )
        self.line5.place(relx=0,y=185,relwidth=1,width = 8 )
        self.line6.place(relx=0,y=215,relwidth=1,width = 8 )


        '''Poscion Botones'''
        boton.place(x=14,y=230)
        text4.place(x=130,y=230)
        self.__window.mainloop()   

    def cargar(self):
        url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        x = requests.get(url)
        dolares = x.json()

        for i in range(len(dolares)):
            if dolares[i]['casa']['nombre'].find('Dolar') >= 0 and dolares[i]['casa']['compra'] != '0' and dolares[i]['casa']['venta'] != '0':
                dolar = [dolares[i]['casa']['nombre'], dolares[i]['casa']['compra'], dolares[i]['casa']['venta']]
                self.list.append(dolar)

    def actualizar(self):
        self.list = []
        self.cargar()
        fecha = datetime.now()
        self.__actual.set('Actualizado {}/{}/{} {}:{}'.format(fecha.day, fecha.month, fecha.year, fecha.hour, fecha.minute))      