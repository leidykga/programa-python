#Matriz de inventario:
#[Codigo,Nombre,Stock Actual ,Stock Minimo Requerido]

inventario =[
    ["A001","Cuadernos",12,20],
    ["A002","Lapiceros",30,25],
    ["A003","Borradores",8,15],
    ["A004","Marcadores",5,10],
    ["A005","Reglas",18,18]
]

#Funcion para determinar la cantidad exacta a pedir 
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0
    
#Mostar lista de pedidos
print("Lista de pedidos:")
print("-------------------")

for articulos in inventario:
    codigo = articulos[0]
    nombre = articulos[1]
    stock_actual = articulos[2]
    stock_minimo = articulos[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print(f"Articulo: {nombre} | Cantidad a pedir: {cantidad_pedir}")