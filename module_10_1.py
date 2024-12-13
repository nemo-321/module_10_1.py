# Импортирование библиотек
import time  # Для работы со временем
from time import sleep  # Для создания пауз
from threading import Thread  # Для создания потоков


#  Определение функции wite_words
#  Функция принимает количество слов и имя файла.
#  Открывает файл для записи в формате UTF-8.
#  Записывает заданное количество слов с паузой 0.1 сек.
#  Сообщает о завершении записи.
def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for n in range(1, word_count + 1):
            file.write(f'Какое-то слово №{n}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл{file_name}')


#  Запуск функции wite_words и измерение времени выполнения записи в файлы.
start_time = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time = time.time()
print(f'Работа потоков{end_time - start_time :.6f} секунд')

# Создание и запуск потоков
# Создает потоки для выполнения функции wite_words с разными аргументами.
# Запускает потоки.
# Ждет их завершения с помощью join.
# Измеряет и выводит время работы потоков.
start_time = time.time()
thread1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thread2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thread3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thread4 = Thread(target=wite_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_time = time.time()
print(f'Работа потоков {end_time - start_time :.6f} секунд')
