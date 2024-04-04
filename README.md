# Описание работы "Телефонный справочник с использованием ООП и файлового ввода-вывода"

## Описание
Данный проект представляет собой программу для работы с телефонным справочником. В программе реализована возможность добавления, отображения, экспорта и импорта контактов в формате `.csv`.

## Функциональность
1. **Добавление контакта**: Пользователь может добавлять новые контакты, вводя имя, фамилию и номер телефона. Валидация вводимых данных проводится с использованием пользовательского исключения.
2. **Отображение контактов**: Пользователь может просматривать список всех контактов, сохраненных в телефонной книге.
3. **Экспорт контактов**: Программа позволяет экспортировать контакты из телефонной книги в файл формата `.csv`.
4. **Импорт контактов**: Пользователь может импортировать контакты из файла формата `.csv` в телефонную книгу.

## Организация кода
1. **Класс `Contact`**: Определяет структуру контакта с полями: имя, фамилия, номер телефона.
2. **Класс `PhoneBook`**: Представляет собой телефонную книгу, в которой хранятся контакты. Реализует методы для добавления контактов, отображения всех контактов и поиска контактов по имени или фамилии.
3. **Класс `FileHandler`**: Обеспечивает чтение и запись контактов в файл формата `.csv`. Реализует методы для чтения контактов из файла, записи контактов в файл, экспорта и импорта контактов.

## Технические детали
- Проект реализован с использованием языка программирования Python.
- Используется объектно-ориентированный подход для более удобного и структурированного кода.
- Для работы с файлами в формате `.csv` используются стандартные библиотеки Python: `csv`, `os`.
