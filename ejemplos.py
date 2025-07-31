def calcular_precio_total(productos):
    total = 0
    for producto in productos:
        if 'categoria' in producto and 'nombre' in producto and 'precio' in producto:
            if producto['categoria'] == 'electronica':
                if producto['nombre'] == 'Laptop':
                    total += producto['precio'] * 1.21
                elif producto['nombre'] == 'Smartphone':
                    total += producto['precio'] * 1.21
                elif producto['nombre'] == 'Tablet':
                    total += producto['precio'] * 1.21
                else:
                    total += producto['precio']
            elif producto['categoria'] == 'ropa':
                if producto['nombre'] == 'Camisa':
                    total += producto['precio']
                elif producto['nombre'] == 'Pantalón':
                    total += producto['precio']
                elif producto['nombre'] == 'Chaqueta':
                    total += producto['precio']
                else:
                    total += producto['precio']
            elif producto['categoria'] == 'comida':
                if producto['nombre'] == 'Manzanas':
                    total += producto['precio']
                elif producto['nombre'] == 'Pan':
                    total += producto['precio']
                elif producto['nombre'] == 'Leche':
                    total += producto['precio']
                else:
                    total += producto['precio']
    return total

def main():
    productos = [
        {'categoria': 'electronica', 'nombre': 'Laptop', 'precio': 1000},
        {'categoria': 'electronica', 'nombre': 'Smartphone', 'precio': 600},
        {'categoria': 'electronica', 'nombre': 'Tablet', 'precio': 300},
        {'categoria': 'ropa', 'nombre': 'Camisa', 'precio': 30},
        {'categoria': 'ropa', 'nombre': 'Pantalón', 'precio': 50},
        {'categoria': 'ropa', 'nombre': 'Chaqueta', 'precio': 80},
        {'categoria': 'comida', 'nombre': 'Manzanas', 'precio': 2},
        {'categoria': 'comida', 'nombre': 'Pan', 'precio': 1},
        {'categoria': 'comida', 'nombre': 'Leche', 'precio': 1.5}
    ]
    resultado = calcular_precio_total(productos)
    print("Total calculado:", resultado)

if __name__ == "__main__":
    main()




