# -> se diseña pantalla para que el usuario cree cuenta
# -> se almacena datos en BBDD
# -> hay boton de regreso a pantalla anterior
# -> hay boton de lOGIN y se ingresa a sistema

#-------------------------------------------------
import flet as ft

container = ft.Container (
    ft.Column([
        ft.Container(
            ft.Text(
                "CREAR CUENTA",
                width= 420,
                size=30,
                text_align= "center",
                weight= "w900",
                color= ft.colors.WHITE
            ),
           # padding = ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField (
                width= 350,
                height= 40,
                hint_text= "Nombre",
                border= "underline",
                color= "white"
            ),
            padding= ft.padding.only(60)  #verificar alineacion!
        ),
    ])
)


# instancio para crear la página
def main (page: ft.Page):
    page.bgcolor = ft.colors.PINK_50   #GREY_400
    page.vertical_alignment= "center"     # alineacion 
    page.horizontal_alignment= "center"   # alineacion
    page.add (container)
    


# para visualizar la ventana gráfica
ft.app(target=main)