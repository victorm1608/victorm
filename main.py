import flet as ft
from flet_core.types import ImageFit

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"Tu IMC es de: {imc:.2f}"
        page.update()
        
        
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()

        if imc<18.5:

            dialog=ft.AlertDialog(
                title="Bajo de peso",
                content="Tu IMC indica que estas bajo de peso",
                actions=[
                    ft.TextButton(text="cerrrar",on_click=cerrar_dialogo)
                ]
            )
    
        elif imc>=18.5 and imc<24.9:
            dialog=ft.AlertDialog(
                title="Pso Normal",
                content="Tu IMC indica que tienes un peso normal",
                actions=[
                    ft.TextButton(text="cerrrar",on_click=cerrar_dialogo)
                ]
            )

        elif imc>=25 and imc<=30:
            dialog=ft.AlertDialog(
                title="Sobrepeso",
                content="Tu IMC indica que tienes peso elevado",
                actions=[
                    ft.TextButton(text="cerrrar",on_click=cerrar_dialogo)
                ]
            ) 

        else:
            dialog=ft.AlertDialog(
                title="Obesidad",
                content="Tu IMC indica que tines obecidad,acude a tu medico",
                actions=[
                    ft.TextButton(text="cerrrar",on_click=cerrar_dialogo)
                ]
            )

        page.dialog=dialog
        page.dialog.open=True
        page.update()

    except ValueError:
        page.dialog.open=False
        page.update()

def main(page: ft.Page):
    page.title="Calculadora de IMC"
    page.bgcolor="orange"
    
    txtPeso=ft.TextField(label="Ingresa tu peso: ")
    txtAltura=ft.TextField(label="Ingresa tu altura: ")
    lblIMC=ft.Text("Tu IMC es de: ")

    img=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ImageFit.CONTAIN
    )


    def on_calcular(e):
        calcular_imc(txtPeso,txtAltura,lblIMC,page)
        
    def limpiar(e):
        txtPeso.value=""
        txtAltura.value=""
        lblIMC.value="Tu IMC es de: "
        page.update()


    btnCalcular=ft.ElevatedButton(text="Calcular")
    btnLimpiar=ft.ElevatedButton(text="LImpiar")

    page.add(
    ft.Column(
        controls=[
            txtPeso,txtAltura,lblIMC
        ],alignment="CENTER"),
    ft.Row(
        controls=[
            img
        ],alignment="CENTER"),
    ft.Row(
        controls=[
            btnCalcular,btnLimpiar
        ],alignment="CENTER")
    )
    
    



ft.app(target=main,view=ft.AppView.WEB_BROWSER)
