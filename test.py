'''import pandas as pd

df = pd.read_excel('memory_card.xlsx')

# Предположим, у вас есть столбец с названием "Имя"

  
name = df.at[q, 'Вопросы']  # Первая строка в столбце "Имя"

column_name = 'Вопросы'  # Замените на нужное название столбца
count_non_empty = df[column_name].count()

for i in range(count_non_empty):
    name = df.at[i, 'Вопросы']
    print(name)'''
import pandas as pd

df = pd.read_excel('memory_card.xlsx')

# Количество непустых ячеек в конкретной строке по индексу
row_index = 1  # Первая строка (индексы с 0)
count_non_empty = df.iloc[1].count() #!
print(count_non_empty)