import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

ventas = data["ventas"]

## Total facturado

total_facturado = 0

for venta in ventas:
    total_facturado = total_facturado + (
        venta["cantidad"] * venta["precio_unitario"]
    )

print("Total facturado:", total_facturado, "€")

## Venta por categoria

ventas_categoria = {}

for venta in ventas:

    categoria = venta["categoria"]

    ventas_categoria[categoria] = (
        ventas_categoria.get(categoria, 0)
        + venta["cantidad"] * venta["precio_unitario"]
    )

print("\nVentas por categoría:")

for categoria, total in ventas_categoria.items():

    print(categoria, ":", total, "€")

## Producto más vendido

productos_vendidos = {}

for venta in ventas:

    producto = venta["producto"]

    productos_vendidos[producto] = (
        productos_vendidos.get(producto, 0)
        + venta["cantidad"]
    )

producto_mas_vendido = max(
    productos_vendidos,
    key=productos_vendidos.get
)

print("\nProducto más vendido:")
print(
    producto_mas_vendido,
    "-",
    productos_vendidos[producto_mas_vendido],
    "unidades"
)