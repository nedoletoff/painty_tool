import flet as ft


def main(page: ft.Page):
    page.title = "Painty Tool"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.Text(value="0", width=100)

    def add_number(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def subtract_number(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.ADD, on_click=add_number),
                txt_number,
                ft.IconButton(ft.icons.REMOVE, on_click=subtract_number),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
