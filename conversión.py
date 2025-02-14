import requests

def obtener_tasa_de_cambio(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        raise Exception(f"Error en la solicitud: {data.get('error', 'Unknown error')}")
    
    tasa_de_cambio = data['rates'][target_currency]
    return tasa_de_cambio

def convertir_divisa(cantidad, base_currency, target_currency):
    tasa_de_cambio = obtener_tasa_de_cambio(base_currency, target_currency)
    cantidad_convertida = cantidad * tasa_de_cambio
    return cantidad_convertida

if __name__ == "__main__":
    base_currency = input("Introduce la divisa base (por ejemplo, USD): ")
    target_currency = input("Introduce la divisa objetivo (por ejemplo, EUR): ")
    cantidad = float(input("Introduce la cantidad a convertir: "))
    
    try:
        resultado = convertir_divisa(cantidad, base_currency, target_currency)
        print(f"{cantidad} {base_currency} son {resultado:.2f} {target_currency}")
    except Exception as e:
        print(f"Error: {e}")