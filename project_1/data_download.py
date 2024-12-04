import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data, ticker):
    """Вывод средней цены за период"""
    avg_close = round(data['Close'].mean(), 4)
    print(f'Средняя цена закрытия акций {ticker}: {avg_close}')




