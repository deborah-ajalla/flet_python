# -> Se realiza una pantalla de LOGIN
# -> Campos: Usuario y contraseña
# -> Se validan ambos campos para permitir ingreso
# -> Se CREA CUENTA 

#-------------------------------------------------

import flet as ft

container = ft.Container (   # creo el CONTENEDOR PPAL
    # >creo columna para insertar titulo, usuario y password
    ft.Column ([
         ft.Container(
             ft.Text(
                 "INICIAR SESIÓN",
                  width= 420,
                  size= 30,
                  text_align= "center",
                  weight= "w900",
                  color= ft.colors.WHITE,              
            ),
            padding = ft.padding.only(20,20)  # >indica distancia a los lados
        ),
        ft.Container(
            ft.TextField(
                width=350,
                height=40,
                hint_text= "Correo Electrónico",
                border= "underline",
                color= "white",   # > cuando escribo el color es blanco
                prefix_icon= ft.icons.EMAIL
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=350,
                height=40,
                hint_text= "Password",
                border= "underline",
                color= "white",
                prefix_icon=ft.icons.LOCK,
                password=True
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Checkbox(
                label= "Recordar Contraseña",
                check_color= "white"
            ),
            padding=ft.padding.only(180)
        ),
        ft.Container(
            ft.ElevatedButton(
                text= "Iniciar"
            ),
            padding=ft.padding.only(50)
        )
    ],
    alignment= ft.MainAxisAlignment.SPACE_EVENLY
),


    border_radius= 20,
    width= 480,
    height= 500,
    gradient= ft.LinearGradient(  #-> indico qué colores forman el degradado
        [ft.colors.PURPLE,
         ft.colors.PURPLE_200,
         ft.colors.PURPLE_100]
    )
)

# instancio para crear la página
def main (page: ft.Page):
    page.bgcolor = ft.colors.PINK_50   #GREY_400
    page.vertical_alignment= "center"     # alineacion 
    page.horizontal_alignment= "center"   # alineacion
    page.add (container)
    


# para visualizar la ventana gráfica
ft.app(target=main)