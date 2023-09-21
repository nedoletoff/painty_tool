import flet as ft


def main(page: ft.Page):
    page.title = "Painty Tool"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def save_img():
        pass

    save_btn = ft.ElevatedButton(
        "Save",
        on_click=save_img
    )

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Painty Tool"),
                        save_btn
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
