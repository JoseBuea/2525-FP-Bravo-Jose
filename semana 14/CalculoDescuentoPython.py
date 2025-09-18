# descuento.py

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento dado un monto total y un porcentaje.
    :param monto_total: float -> valor total de la compra
    :param porcentaje_descuento: float -> porcentaje de descuento (10% por defecto)
    :return: float -> monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primera llamada (solo monto, usa 10% por defecto)
    monto1 = 3450
    descuento1 = calcular_descuento(monto1)
    print(f"Compra: ${monto1}")
    print(f"Descuento aplicado: ${descuento1}")
    print(f"Monto final a pagar: ${monto1 - descuento1}\n")

    # Segunda llamada (monto + porcentaje específico)
    monto2 = 100
    descuento2 = calcular_descuento(monto2, 20)
    print(f"Compra: ${monto2}")
    print(f"Descuento aplicado: ${descuento2}")
    print(f"Monto final a pagar: ${monto2 - descuento2}")
