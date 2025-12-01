import flet as ft


def main(page: ft.Page):
    def calcular_combustivel(e):
        if not gasolina.value:
            gasolina.error_text = "Valor da gasolina não pode ficar vazio."
            page.update()
        else:
            gasolina.error_text = ""
            page.update()
        if not etanol.value:
            etanol.error_text = "Valor do etanol não pode ficar vazio."
            page.update()
        else:
            etanol.error_text = ""

            gasolina_valor = float(gasolina.value.replace(",","."))
            etanol_valor = float(etanol.value.replace(",","."))
            resultado = "gasolina" if etanol_valor >= gasolina_valor*0.7 else "Etanol"
            dlg_modal.content.value = resultado
            gasolina.value = ""
            gasolina.value = ""

            page.open(dlg_modal)

            page.update()

    page.title = "App Flex Fuel"
    page.scroll = "adaptative"
    page.theme_mode = ft.ThemeMode.LIGHT

    gasolina = ft.TextField(
        label="valor da gasolina",
        prefix_text="R$",
        keyboard_type=ft.KeyboardType.NUMBER
    )    
    
    etanol = ft.TextField(
        label="valor do etanol",
        prefix_text="R$",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=calcular_combustivel
    )

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Melhor abastecer com:"),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("FLEX FUEL", size=35, weight="bold"),
                alignment=ft.alignment.center,
                padding=115
            
            
                
            ),
            #expand=True,
        ),
        ft.ResponsiveRow(
            [
                ft.Container(gasolina, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(etanol, col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Calcular", on_click=calcular_combustivel),
                    padding=30
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)