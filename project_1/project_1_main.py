import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet "
        "Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, "
        "с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period_start = input("Введите дату начало периода в формате «2024-12-12»: ")
    period_end = input("Введите дату конца периода в формате «2024-12-12»: ")
    threshold = int(input("Введите значение порога колебания: "))

    """Получить данные"""
    stock_data = dd.fetch_stock_data(ticker, period_start, period_end)

    """данные за определенный период """
    stock_data_file = stock_data

    std_close = dd.standard_deviation(stock_data)

    """Вывод средней цены за период"""
    stock_data_avg = dd.calculate_and_display_average_price(stock_data, ticker)

    """Уведомление о сильных колебаниях, указать порог"""
    stock_fluctuations = dd.check_price_difference(stock_data, threshold)

    """Добавьте скользящее среднее к данным"""
    stock_data = dd.add_moving_average(stock_data)

    """RSI дял Close, Low, High"""
    close_column = 'Close'
    high_column = 'High'
    """Добавления столбцов RSI_Close и RSI_High в DF"""
    stock_data['RSI_Close'] = dd.upeman_downeman(stock_data, close_column)
    stock_data['RSI_High'] = dd.upeman_downeman(stock_data, high_column)
    # print(stock_data)

    """Запись данных в файл"""
    list_on_xlsx = [stock_data_file, stock_data_avg, stock_fluctuations]
    answer = input("Хотите записать данные в файл? (ДА|НЕТ) ")

    if answer.lower() == 'да':
        filename = input('Введите название файла: ')
        print(type(filename))
        if filename != '':
            dd.export_data_to_csv(list_on_xlsx, filename=filename)
        else:
            dd.export_data_to_csv(list_on_xlsx, filename='output_file')
    else:
        print('Файлы не созданы')

    """Создание графика"""
    dplt.create_and_save_plot(stock_data, ticker, period_start, period_end, std_close)


if __name__ == "__main__":
    main()
