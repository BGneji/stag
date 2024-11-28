import os
import json
from datetime import datetime
from pathlib import Path
import pandas as pd

file_path = './файлы/'
current_data = datetime.now().strftime('%d-%m-%Y_%H-%M')


class PriceMachine:

    def __init__(self):
        self.data = pd.DataFrame()
        self.result = ''
        self.name_length = 0
        self.dataframes = []
        self.l_name = ['товар', 'название', 'наименование', 'продукт', 'розница', 'цена', 'вес', 'масса', 'фасовка']
        self.path = Path(file_path)

    """Чтение данных из файла и преобразование к одному формату"""

    def load_prices(self):
        for file in self.path.rglob('*'):
            if 'price' in file.name:
                df = pd.read_csv(file)
                existing_columns = [col for col in self.l_name if col in df.columns]
                filtered_df = df[existing_columns].copy()
                new_column_name = ['товар', 'цена', 'вес']
                filtered_df.columns = new_column_name
                filtered_df['цена за кг'] = (filtered_df['цена'] / filtered_df['вес']).round(2)
                filtered_df.loc[:, 'имя_файла'] = file.name
                self.dataframes.append(filtered_df)

        self.data = pd.concat(self.dataframes, ignore_index=True)
        res = self.data['товар'].unique().tolist()
        print('Все товары из файлов')
        for i in range(0, len(res), 10):
            print(res[i:i + 10])

    """Формируем файл html изо всех файлов"""

    def export_to_html(self, out_file='output.html'):
        self.data.to_html(out_file, index=False)

    """поиск по dataframe"""

    def find_text(self, text):
        if isinstance(text, str):
            result = self.data[self.data['товар'].str.contains(f'{text}', case=False)]
            result = result.sort_values(by='цена за кг')
            num_rows = len(result)
            new_column = range(1, num_rows + 1)
            result.insert(0, 'Номер', new_column)
            if result.empty:
                print('Нечего не нашел')
            else:
                print(result)
                print('Хотите сохранить поиск?')

                answer_user = input('Ведите да или нет: ')
                if answer_user.lower() == 'да':
                    self.export_to_html(f'{text}_{current_data}.html')
                    print(f"Поиск сохранен  в файл: {text}_{current_data}.html")
                else:
                    print("Поиск не сохранен.")


pm = PriceMachine()
pm.load_prices()
n = ''
while True:
    print()
    print('exit для завершение работы ')
    n = input('Введите запрос: ')
    print()
    if n.lower() == 'exit':
        break
    pm.find_text(n)
print('the end')
pm.export_to_html()
