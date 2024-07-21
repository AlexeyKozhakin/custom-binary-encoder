import pandas as pd
from custom_binary_encoder import apply_custom_binary_encoding
# Пример данных

data = pd.DataFrame({'Цвет': ['красный', 'зеленый', 'синий', 'желтый','фиалетовый']})

# Применение пользовательского бинарного кодирования
encoded_data = apply_custom_binary_encoding(data, 'Цвет')
print(encoded_data)
print(data)