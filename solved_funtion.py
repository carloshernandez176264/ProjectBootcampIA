PRECIOS = {
    'electronica': {
        'Laptop': 1000,
        'Smartphone': 600,
        'Tablet': 300
    },
    'ropa': {
        'Camisa': 30,
        'Pantalón': 50,
        'Chaqueta': 80
    },
    'comida': {
        'Manzanas': 2,
        'Pan': 1,
        'Leche': 1.5
    }
}

IMPUESTOS = {
    'electronica': 0.21,
    'ropa': 0.0,
    'comida': 0.0
}

def obtener_precio(producto):
    return PRECIOS.get(producto['categoria'], {}).get(producto['nombre'], 0)

def aplicar_impuesto(precio, categoria):
    return precio * (1 + IMPUESTOS.get(categoria, 0))

def calcular_precio_producto(producto):
    base = obtener_precio(producto)
    return aplicar_impuesto(base, producto['categoria'])

def calcular_precio_total(productos):
    return sum(calcular_precio_producto(p) for p in productos)

def main():
    productos = [
        {'categoria': 'electronica', 'nombre': 'Laptop'},
        {'categoria': 'electronica', 'nombre': 'Smartphone'},
        {'categoria': 'electronica', 'nombre': 'Tablet'},
        {'categoria': 'ropa', 'nombre': 'Camisa'},
        {'categoria': 'ropa', 'nombre': 'Pantalón'},
        {'categoria': 'ropa', 'nombre': 'Chaqueta'},
        {'categoria': 'comida', 'nombre': 'Manzanas'},
        {'categoria': 'comida', 'nombre': 'Pan'},
        {'categoria': 'comida', 'nombre': 'Leche'}
    ]
    print("Total calculado:", calcular_precio_total(productos))

if __name__ == "__main__":
    main()
