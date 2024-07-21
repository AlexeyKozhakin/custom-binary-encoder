# custom-binary-encoder
## Overview

The `Custom Binary Encoder` library provides a custom implementation for binary encoding of categorical features in machine learning. It dynamically generates binary vectors based on the number of unique categories in the dataset. This approach is useful when you need to convert categorical data into a binary format for machine learning models.

## Features

- **Dynamic Encoding:** Automatically determines the length of the binary vectors based on the number of unique categories.
- **Easy Integration:** Simple functions to apply binary encoding to a DataFrame.

## Installation

Simple installation :

```bash
pip install git+https://github.com/AlexeyKozhakin/custom-binary-encoder.git
```

## Usage

```
from custom_binary_encoder.encoder import apply_custom_binary_encoding

import pandas as pd

# Пример данных
data = pd.DataFrame({'Color': ['red', 'green', 'blue', 'yellow']})

# Применение пользовательского бинарного кодирования
encoded_data = apply_custom_binary_encoding(data, 'Color')
print(encoded_data)
```