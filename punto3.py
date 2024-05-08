import pandas as pd

# Crear una lista de datos
data = [
    [1, 116], [2, 133], [3, 139], [4, 157], [5, 154], [6, 159], [7, 162], [8, 172],
    [9, 163], [10, 163], [11, 164], [12, 191], [13, 201], [14, 219], [15, 207], [16, 205],
    [17, 210], [18, 207], [19, 225], [20, 223], [21, 257], [22, 232], [23, 240], [24, 241]
]


# Crear un DataFrame a partir de la lista
df = pd.DataFrame(data, columns=["Mes", "Ventas"])

# Calcular SMA con un tamaño de ventana de 4
df['SMA_4'] = df['Ventas'].rolling(window=4).mean()

# Definir el coeficiente de suavizado (alpha)
alpha = 0.28

# Inicializar los valores de pronóstico
df['Pronostico'] = df['Ventas'].iloc[0]

# Calcular pronósticos de suavizado exponencial
for i in range(1, len(df)):
    pronostico = alpha * df['Ventas'].iloc[i] + (1 - alpha) * df['Pronostico'].iloc[i - 1]
    df.loc[i, 'Pronostico'] = pronostico

# Imprimir el DataFrame con los valores de pronóstico
print(df)
