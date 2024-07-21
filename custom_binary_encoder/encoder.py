import pandas as pd
import math

import itertools

def generate_binary_combinations(n):
    # Используем itertools.product для генерации всех возможных комбинаций
    combinations = list(itertools.product([0, 1], repeat=n))
    return combinations

# # Пример для n=2
# n = 2
# combinations = generate_binary_combinations(n)
# for combo in combinations:
#     print(combo)

def custom_binary_encoder(categories):
    """
    Функция для выполнения пользовательского бинарного кодирования категориальных признаков.

    Аргументы:
    categories -- список уникальных категорий.

    Возвращает:
    encoding_map -- словарь, сопоставляющий каждую категорию с уникальным бинарным вектором.
    """
    # Вычислить минимальное значение n
    num_categories = len(categories)
    n = math.ceil(math.log2(num_categories))

    combinations = generate_binary_combinations(n)

    # Сгенерировать бинарные векторы длины n
    binary_vectors = []
    for i in range(num_categories):
        # Преобразовать i в бинарный вектор длины n
        binary_vector = list(combinations[i])
        binary_vectors.append(binary_vector)

    # Присвоить векторы категориям
    encoding_map = {category: binary_vectors[i] for i, category in enumerate(categories)}

    return encoding_map


def apply_custom_binary_encoding(data, column):
    """
    Функция для применения пользовательского бинарного кодирования к DataFrame.

    Аргументы:
    data -- DataFrame, содержащий данные.
    column -- название столбца, содержащего категориальные признаки для кодирования.

    Возвращает:
    encoded_data -- DataFrame с закодированным столбцом.
    """
    unique_categories = data[column].unique()
    encoding_map = custom_binary_encoder(unique_categories)
    # Применение кодирования
    encoded_columns = data[column].map(encoding_map).apply(pd.Series)
    encoded_columns.columns = [f"{column}_{i}" for i in range(encoded_columns.shape[1])]

    return pd.concat([data.drop(columns=[column]), encoded_columns], axis=1)
