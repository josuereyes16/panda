import pandas as pd
import random
from datetime import datetime, timedelta

# Helper functions to generate random data
def random_date(start, end):
    """Generate a random date between two given dates."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_choice(choices):
    """Select a random item from a list of choices."""
    return random.choice(choices)

# Data to use for random generation
sections = ["Corte", "Ensamblado", "Terminado"]
defects = ["Despegue de suela", "Costura mal hecha", "Color incorrecto", "Tamaño desigual", "Fallo en adhesión"]
severity_levels = ["Crítico", "Medio", "Bajo"]
stoppage_reasons = ["Mantenimiento", "Error humano", "Falta de material", "Ajuste de máquina", "Desconocido"]
areas = ["Producción", "Control de calidad", "Distribución"]
product_types = ["Bota", "Zapatilla", "Sandalia", "Mocasín", "Zapato formal"]
satisfaction_levels = [1, 2, 3, 4, 5]

# Generate 100-150 random records
num_records = random.randint(100, 150)

# Create a DataFrame with the appropriate columns
data = {
    "Fecha": [random_date(datetime(2024, 1, 1), datetime(2024, 10, 28)).strftime('%Y-%m-%d') for _ in range(num_records)],
    "Sección_Producción": [random_choice(sections) for _ in range(num_records)],
    "Operario_ID": [f"OP-{random.randint(1, 50):03d}" for _ in range(num_records)],
    "Máquina_ID": [f"MAQ-{random.randint(1, 10):02d}" for _ in range(num_records)],
    "Producto_ID": [random_choice(product_types) for _ in range(num_records)],
    "Tiempo_Ejecución_min": [random.randint(20, 180) for _ in range(num_records)],
    "Tiempo_Paradas_min": [random.randint(0, 30) for _ in range(num_records)],
    "Unidades_Producidas": [random.randint(50, 300) for _ in range(num_records)],
    "Unidades_Defectuosas": [random.randint(0, 20) for _ in range(num_records)],
    "Motivo_Parada": [random_choice(stoppage_reasons) for _ in range(num_records)],
    "Tipo_Defecto": [random_choice(defects) for _ in range(num_records)],
    "Nivel_Defecto": [random_choice(severity_levels) for _ in range(num_records)],
    "Causa_Raíz": [random_choice(["Sí", "No"]) for _ in range(num_records)],
    "Área_Afectada": [random_choice(areas) for _ in range(num_records)],
    "Acción_Correctiva": [random_choice(["Sí", "No"]) for _ in range(num_records)],
    "Satisfacción_Operario": [random_choice(satisfaction_levels) for _ in range(num_records)],
    "Reclamo_Cliente": [random_choice(["Sí", "No"]) for _ in range(num_records)],
    "Costo_Producción_USD": [round(random.uniform(10, 50), 2) for _ in range(num_records)],
    "Ventas_USD": [round(random.uniform(2000, 10000), 2) for _ in range(num_records)],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Optional: Print the first few rows of the DataFrame to check
print(df.head())

# Save to CSV with UTF-8 encoding
df.to_csv("C:/Users/anton/synthetic_shoe_factory_data.csv", index=False, encoding='utf-8')
print("Dataset created successfully!")
