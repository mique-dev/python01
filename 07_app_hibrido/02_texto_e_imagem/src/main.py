import flet as ft


def main(page: ft.Page):
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("vai ser tetra vai vendo." , size=30, weight="bold", font_family="comic sans ms"),
                alignment=ft.alignment.center,
            )
        ),
        ft.Container(
            ft.Image(
                src="pexels-jonathanborba-34926322 (1).jpg",
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Text("Não foi possivel carrgar a imagem.")
            ),
            alignment=ft.alignment.center,
            expand=True,
        )
    )


ft.app(main)
