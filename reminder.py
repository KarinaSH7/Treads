"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""

import threading
import time
def reminder():
    remind = input('О чём необходимо напомнить ?')
    seconds = int(input('Через скколько секунд нужно напомнить ?'))
    time.sleep(seconds)
    print(f"Напоминаю: {remind}")

reminder_thread = threading.Thread(target=reminder)
reminder_thread.start()

time.sleep(10)
print('Завершение программы')