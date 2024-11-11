#-----------------------------------------------------------------------------------------------------
######## Se trabaja con la librería FLET y se navega entre distintas ventanas en la misma app ########

# --> verificar contenido de cada pagina

#-----------------------------------------------------------------------------------------------------
import flet as ft
# ----- FUNCIÓN PRINCIPAL -----
def main (page : ft.Page):
    page.title = "Interfaz pestañas"
    page.bgcolor = ft.colors.PURPLE_200 #DEEP_PURPLE_300    
    page.horizontal_alignment =ft.CrossAxisAlignment.CENTER  # alinea todos los elementos al centro 
 
    # ----- FUNCIÓN CADA VEZ Q SE CLIQUEA UN ICONO DE PESTAÑA -----
    def on_navigation_change (evento):
        selected_index = evento.control.selected_index    # --> guardo el indice seleccionado en la variable
        if selected_index == 0:   # ---> indice 0: muestra el HOME
            mostrar_home ()
        elif selected_index == 1:
            mostrar_busqueda ()
        elif selected_index == 2:
            mostrar_config ()
        page.update()
  
    # ----- FUNCIÓN IR AL HOME -----
    def mostrar_home ():
        page.controls.clear ()  # --> si estaba en otra pantalla y vuelvo a home: borra la pantalla para q aparezca contenido de home
        contador.value = f"Contador: {contador_value}"
        page.add (barra_navegacion, contador, boton_mas, boton_menos)

    # ----- FUNCIÓN IR A BUSQUEDA -----
    def mostrar_busqueda():
        page.controls.clear ()      # --> si estaba en otra pantalla borra el contenido para q aparezca contenido de la pantalla
        search_out.value = ""
        search_input.value = ""
        page.add (barra_navegacion, search_input, boton_buscar, search_out)

    # ----- FUNCIÓN IR A CONFIG -----
    def mostrar_config ():
        page.controls.clear ()      # -->  borra el contenido para q aparezca contenido de la pantalla config
        slider_brillo.value = 50
        page.add (barra_navegacion, slider_brillo, boton_resetear_brillo)

    # --> contenido de pagina HOME <--
    contador = ft.Text (value="Contador : 0", size= 40, color=ft.colors.WHITE) 
    contador_value = 0

    # --> contenido de pagina BUSQUEDA <--
    search_input = ft.TextField (label= "Ingrese lo que desea buscar...")
    search_out = ft.Text (value= "", size=20, color=ft.colors.WHITE)

    # --> contenido de pagina CONFIG <--
    slider_brillo = ft.Slider (min= 0, max= 100, value= 50, label= "Brillo")    #  -> crea la barra para aumentar brillo


    # --> funciones de pagina HOME <--
    def mas_contador (evento):    # --> el evento q recibe como parametro es el on_click
        nonlocal contador_value
        contador_value += 1
        contador.value = f"Contador: {contador_value}"
        page.update ()

    def menos_contador (evento):
        nonlocal contador_value
        contador_value -= 1
        contador.value = f"Contador: {contador_value}"
        page.update ()
    
    # --> funciones de pagina BUSQUEDA <--
    def buscar (evento):
        search_out.value = f"Resultado de la búsqueda: {search_input.value}"
        page.update ()

    # --> funciones de pagina CONFIG <--
    def reset_brillo (evento):
        slider_brillo.value = 50
        page.update ()
 
    # --> botones <--
    boton_mas = ft.ElevatedButton (text= "Sumar", on_click= mas_contador)
    boton_menos = ft.ElevatedButton (text= "Restar", on_click= menos_contador)
    boton_buscar = ft.ElevatedButton (text= "Buscar", on_click= buscar)
    boton_resetear_brillo = ft.ElevatedButton (text= "Reset Brillo", on_click= reset_brillo)
     

    # -----> CREA BARRA DE NAVEGACION <-----
    barra_navegacion = ft.NavigationBar (
        selected_index= 0,                 # posiciona por defecto la primer posicion de pestaña
        on_change= on_navigation_change,   # -> función
        destinations= [                    # -> click en el icono y se abre una pestaña
            ft.NavigationBarDestination ( icon= ft.icons.HOME, label= "Inicio"),
            ft.NavigationBarDestination ( icon= ft.icons.SEARCH, label= "Buscar"),
            ft.NavigationBarDestination ( icon= ft.icons.SETTINGS, label= "Herramientas"),
        ],
        bgcolor= ft.colors.PURPLE_100,
        indicator_color=  ft.colors.PINK_200,
    )


    page.add (barra_navegacion)    # --> se agrega a la pagina para que se vea todo lo que se guardó en contenido <--
    mostrar_home()                 # --> muestra la pantalla HOME por defecto al abrir la app <--

# --> se instancia la aplicacion <--
ft.app (target= main)    