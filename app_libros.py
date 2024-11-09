# --> trabajo en un entorno virtual
# --> tema: una app  que permite:
#  insertar titulo, insertar texto en el cuerpo y borrar la nota y agregarla a lista de favoritos
# verificar y arreglar codigo y separar para que en favoritos solo aparezca ELIMINAR y funcione ... :(
# octubre: 2024
# 💜 Realizado por Deborah Ajalla 💜
#---------------------------------------------------------------------
import flet as ft  # --> se descargó flet en la consola para empezar a trabajar
#---------------------------------------------------------------------
# ---- FUNCIÓN PRINCIPAL ----
def ppal (page: ft.Page):
    # -- creo titulo de la ventana --
    page.title = "My App"
    
    # --> activo modo oscuro
    page.theme_mode = ft.ThemeMode.DARK     

    # -- FUNCIÓN  Cambia Modo oscuro/ claro -- (cambiar ternario a if/ else simple)
    def cambiar_tema (e): 
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK        # -- cambia pantalla
        theme_icon_button.icon = ft.icons.DARK_MODE if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE # -- cambia icono

        page.update()   # actualiza la pagina

    # -- creo boton para cambiar tema --
    theme_icon_button = ft.IconButton (
         icon = ft.icons.LIGHT_MODE, 
         tooltip= "Cambiar Tema",
         on_click= cambiar_tema,
         )
    
    # -- creo titulo de la ventana --
    titulo = ft.Text ("My App- Sabado")
    
    # -- creo barra de menu --
    app_bar = ft.AppBar(                                    # --> crea una barra tipo menubar
                        title= titulo,                      # -> coloco el titulo en la menubar
                        center_title= True,                 # -> posicin centrada
                        bgcolor= ft.colors.SURFACE_VARIANT, # -> color de la menubar
                        actions= [theme_icon_button],       # -> la unica accion de la menubar
                       )

    # --> creo barra lateral con contenido
    books_view = ft.ListView (expand= 1, spacing= 10, padding= 20)      # creo la seccion lateral y le doy las medidas
    wishlist_view = ft.ListView (expand= 1, spacing= 10, padding= 20)

    # --> FUNCIÓN AGREGA LISTA DE DESEOS <--
    def lista_deseos (e):
       deseado = ft.ListTile (title= ft.Text (title_field.value),
                              subtitle= ft.Text (autor_field.value)
                             
                             )
       wishlist_view.controls.append (deseado)  # -> a la lista de libros le agrego el nuevo libro
       page.update ()

    # --> FUNCIÓN AGREGA LIBROS <--
    def add_book (e):
        if not title_field.value:   # -> si el titulo está vacío
            title_field.error_text = "Por Favor ingrese un título..."
            page.update()
            return 
        new_book = ft.ListTile (
                       title= ft.Text (title_field.value),
                       subtitle= ft.Text (autor_field.value if autor_field.value else "Autor Desconocido"),
                       trailing= ft.PopupMenuButton (
                                      icon = ft.icons.MORE_VERT,  # --> more_vert son los 3 puntitos q hacemos click y muestran contenido
                                      items= [ft.PopupMenuItem (text= "Eliminar", 
                                                                on_click= lambda _:books_view.controls.remove(new_book) or page.update ()),
                                              ft.PopupMenuItem ( text= "Añadir a Lista de deseos",
                                                                on_click= lambda _:wishlist_view.controls.append (new_book) or page.update())                                                                 
                                             ],
                                                     ),
                             )
        books_view.controls.append (new_book)  # -> a la lista de libros le agrego el nuevo libro

        # --> para resetear a 0 los campos ingreados
        title_field.value = ""
        autor_field.value = ""

        # --> para resetear que muestre error en el campo
        title_field.error_text = None

        page.update ()


    title_field = ft.TextField (label= "Titulo del Libro", width= 300)  # --> es el imput donde se ingresa el libro
    autor_field = ft.TextField (label= "Autor", width= 300)             # --> es el imput donde se ingresa el libro
    
    # --> creo botón para agregar libro
    add_button = ft.ElevatedButton (text= "Añadir Libro", on_click= add_book)


    add_book_view = ft.Column ([
                                ft.Text (value= "Añadir nuevo libro", size= 20, weight= ft.FontWeight.BOLD), 
                                title_field,
                                autor_field, 
                                add_button],
                                spacing= 20
                               )
    
    def destination_change (e):
        index = e.control.selected_index
        content.controls.clear()
        if index == 0:   # click en mis libros
            content.controls.append (books_view)      # -> muestra contenido de libros
        elif index == 1: # click añadir
            content.controls.append (add_book_view)   # -> muestra para añadir un libro
        elif index == 2: # click en favoritos
            content.controls.append (wishlist_view)   # -> muestra lista de deseos
        page.update()
    
    rail = ft.NavigationRail (
                               selected_index= 0,
                               label_type= ft.NavigationRailLabelType.ALL,
                               min_width= 100,
                               min_extended_width= 400,
                               destinations= [
                                               ft.NavigationRailDestination (icon= ft.icons.BOOK, label= "Mis Libros"),
                                               ft.NavigationRailDestination (icon= ft.icons.ADD, label= "Añadir Libro"),
                                               ft.NavigationRailDestination (icon= ft.icons.FAVORITE, label= "Lista de Deseos"),
                                             ],

                               on_change= destination_change,
                             )
    
    content = ft.Column ([books_view, wishlist_view], expand= True)

    # --> coloca el contenido en la ventana
    page.add (app_bar, ft.Row ([rail, ft.VerticalDivider (width = 1), content], expand= True))


ft.app (target= ppal)

