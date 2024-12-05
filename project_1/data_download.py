import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    print(data)
    data.to_excel('max_dates.xlsx', index=False)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data, ticker):
    """Вывод средней цены за период"""
    avg_close = round(data['Close'].mean(), 4)
    print(f'Средняя цена закрытия акций {ticker}: {avg_close}')
    print()

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
