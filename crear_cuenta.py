# -> se diseña pantalla para que el usuario cree cuenta ✔
# -> se almacena datos en BBDD
# -> hay boton de regreso a pantalla anterior ✔
# -> hay boton de REGISTRARSE y se ingresa a sistema

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
            padding = ft.padding.all(30) # queda responsive
        ),
        ft.Container(
            ft.TextField (
                width= 350,
                height= 40,
                hint_text= "Nombre",
                border= "underline",
                border_color= ft.colors.WHITE54,
                color= "white"
            ),
            padding= ft.padding.only(60)  #verificar alineacion!
        ),
        ft.Container(
            ft.TextField(
                width=350,
                height= 40,
                hint_text= "Usuario",
                border= "underline",
                border_color= ft.colors.WHITE54,
                color= "white"
            ),
            padding= ft.padding.only(60)
        ),
         ft.Container(

            ft.TextField(
                width= 350,
                height= 40,
                hint_text= "Contraseña",
                password= True,
                can_reveal_password= True,
                border= "underline",
                border_color= ft.colors.WHITE54, # -> cuando hago click el borde se pone blanco
                #focused_border_color= "grey",
                color= "white"
            ),
            padding= ft.padding.only(60)
         ),
         ft.Container(
             ft.TextField(
                 width= 350,
                 height= 40,
                 hint_text= "Repetir Contraseña",
                 password= True,
                 can_reveal_password= True,
                 border= "underline",
                 border_color= ft.colors.WHITE54,
                 color= "white"
             ),
             padding= ft.padding.only(60)
         ),
         ft.Container(
             ft.Row([
                   ft.ElevatedButton(
                      text= "Registrarse",
                      width= 260                
                    ), 
             ],
               alignment= ft.MainAxisAlignment.CENTER
             ),
             padding= ft.padding.only(top=35)
         ),
         ft.Container(
             width= 60,
             height= 78,
             border_radius= 10,
             padding= ft.padding.symmetric(20),
             content= ft.IconButton (
             icon= ft.icons.ARROW_BACK_IOS_NEW_OUTLINED,
             icon_color= ft.colors.WHITE54,
             #style= ft.ButtonStyle ()
            ), 
            margin=ft.margin.only(left= 210)
         )
    ],
  
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