
import flet as ft
import logging

logging.basicConfig(level=logging.DEBUG)


def main(page: ft.Page):
    cupertino_alert_dialog = ft.CupertinoAlertDialog(
        title=ft.Text("Cupertino Alert Dialog"),
        content=ft.Text("Do you want to delete this file?"),
        actions=[
            ft.CupertinoDialogAction(
                "OK",
                is_destructive_action=True,
            ),
            ft.CupertinoDialogAction(text="Cancel"),
        ],
    )

    alert_dialog = ft.AlertDialog(
        title=ft.Text("Material Alert Dialog"),
        content=ft.Text("body"),
        actions=[ft.TextButton("OK"), ft.TextButton("Cancel")],
    )

    actions = []
    if page.platform in ["ios", "macos"]:
        actions = [
            ft.CupertinoDialogAction("OK"),
            ft.CupertinoDialogAction("Cancel"),
        ]
    else:
        actions = [ft.TextButton("OK"), ft.TextButton("Cancel")]

    adaptive_alert_dialog = ft.AlertDialog(
        adaptive=True,
        title=ft.Text("Adaptive Alert Dialog"),
        content=ft.Text("body"),
        actions=actions,
    )

    def open_cupertino_dialog(e):
        page.dialog = cupertino_alert_dialog
        cupertino_alert_dialog.open = True
        page.update()

    def open_material_dialog(e):
        page.dialog = alert_dialog
        alert_dialog.open = True
        page.update()

    def open_adaptive_dialog(e):
        page.dialog = adaptive_alert_dialog
        adaptive_alert_dialog.open = True
        page.update()

    page.add(
        ft.OutlinedButton("Open Cupertino Dialog", on_click=open_cupertino_dialog),
        ft.OutlinedButton("Open Material Dialog", on_click=open_material_dialog),
        ft.OutlinedButton("Open Adaptive Dialog", on_click=open_adaptive_dialog),
    )


ft.app(target=main)