import pandas as pd

df = pd.read_excel('memory_card.xlsx')

# Предположим, у вас есть столбец с названием "Имя"
name = df.at[0, 'Вопросы']  # Первая строка в столбце "Имя"
print(name)