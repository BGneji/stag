import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker, start, end):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start, end=end)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data, ticker):
    """Вывод средней цены за период"""
    avg_close = round(data['Close'].mean(), 4)
    print(f'Средняя цена закрытия акций {ticker}: {avg_close}')
    print()
    results = pd.DataFrame({
        'Тикер': [ticker],
        'Средняя цена закрытия': [avg_close]
    })

    return results


def check_price_difference(data, threshold):
    """Уведомление о сильных колебаниях, указать порог"""
    max_close = data['Close'].max()
    min_close = data['Close'].min()
    difference = round((max_close - min_close), 4)
    print(f"Максимальная цена закрытия: {max_close}")
    print(f"Минимальная цена закрытия: {min_close}")
    print(f"Разница: {difference}")

    if difference > threshold:
        print(f"Уведомление: Разница {difference} превышает порог {threshold}.")
    else:
        print(f"Разница {difference} не превышает порог {threshold}.")

    results = pd.DataFrame({
        'Максимальная цена закрытия': [max_close],
        'Минимальная цена закрытия': [min_close],
        'Разница': [difference],
        'Порог': [threshold],
        'Превышает порог': [difference > threshold]
    })
    return results


def export_data_to_csv(data, filename):
    """Запись данных в файл"""
    with pd.ExcelWriter(f'{filename}.xlsx') as writer:
        for i, df in enumerate(data):
            df.to_excel(writer, sheet_name=f'Sheet{i + 1}', index=False)
    data[0].to_csv(f'csv_{filename}.csv', index=False)


def upeman_downeman(data, column, window_size=5):
    """Дополнительные технические индикаторы, например, RSI"""
    delta = data[column].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window_size).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window_size).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def standard_deviation(data):
    """Стандартного отклонения цены закрытия"""
    std_dev = data['Close'].std()

    return std_dev




