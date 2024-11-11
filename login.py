# -> Se realiza una pantalla de LOGIN ✔
# --> verificar alineacion de componentes. para que quede responsive.
# -> Campos: Usuario y contraseña
# -> Se validan ambos campos para permitir ingreso
# -> Se CREA CUENTA ✔
# -> agregar FUNCIONALIDAD

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
            padding= ft.padding.only(60) #ft.padding.only(20,20)
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
            padding=ft.padding.only(60)
        ),
        ft.Container(
            ft.Checkbox(
                label= "Recordar Contraseña",
                check_color= "white"
            ),
            padding=ft.padding.only(240) # + mueve a la derecha
        ),
        ft.Container(
            ft.ElevatedButton(
                text= "Ingresar",
                width=280
            ),
            padding=ft.padding.only(100)
        ),
        ft.Text("Iniciar Sesión con ",
                text_align= "center",
                width= 480
                ),
        ft.Container(
            ft.Row([
                ft.IconButton(
                    icon= ft.icons.EMAIL,
                    tooltip= "Google",
                    icon_color= "white",
                    icon_size=30
                ),
                ft.IconButton (
                    icon= ft.icons.FACEBOOK,
                    tooltip= "Facebook",
                    icon_color= "white",
                    icon_size=30
                )
            ],
            alignment= ft.MainAxisAlignment.CENTER # -> propiedad de alineacion
            ),
            #padding= ft.padding.only(180)
        ),
        ft.Container(
            ft.Row ([
                ft.Text ("¿No Tiene Cuenta?"),
                ft.TextButton("Crear Cuenta")
            ],
            alignment=ft.MainAxisAlignment.CENTER
            )
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