import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period_start, period_end, filename=None):
    plt.figure(figsize=(15, 10))
    style = input('Выберите тему для графика 1 посмотреть все доступные темы ')
    if style == '1':
        print("Доступные стили")
        print('bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8')
        style = input('Введите тему которую выбрали: например fast: ')
        plt.style.use(style=style)

    style = 'classic'
    plt.style.use(style=style)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['RSI_Close'].values, label='RSI_Close')
            plt.plot(dates, data['RSI_High'].values, label='RSI_High')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['RSI_Close'], label='RSI_Close')
        plt.plot(data['Date'], data['RSI_High'], label='RSI_High')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        style = 'ggplot'

    plt.title(f"{ticker} Цена акций с течением времени, применен стиль {style}")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_c {period_start} по {period_end}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
