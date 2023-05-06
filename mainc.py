import tkinter as tk
from tkinter import messagebox


def patient_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "Олжас" and password == "123":
        messagebox.showinfo("Успешная авторизация", "Добро пожаловать, пациент!")
        show_main_window()
    else:
        messagebox.showerror("Ошибка авторизации", "Неверный логин или пароль")


def view_tests():
    clear_window()

    label_title = tk.Label(window, text="Список анализов", font=("Arial", 16))
    label_title.pack(pady=20)

    tests = [
        "Кровь",
        "Моча",
        "Рентген",
        "Узи",
        "ЭКГ"
    ]

    for test in tests:
        label_test = tk.Label(window, text=test)
        label_test.pack()


def view_results():
    clear_window()

    label_title = tk.Label(window, text="Результаты анализов", font=("Arial", 16))
    label_title.pack(pady=20)

    results = [
        "Анализ крови:Гемоглобин: 12 г/дл (норма: 12-16 г/дл) Лейкоциты: 8,000/мкл (норма: 4,000-11,000/мкл), Глюкоза: 95 мг/дл (норма: 70-100 мг/дл), Холестерин: 180 мг/дл (норма: менее 200 мг/дл)",
        "Анализ мочи:   Цвет: светло-желтый, Прозрачность: прозрачная, Плотность: 1.020 (норма: 1.005-1.030), Белок: отсутствует, Глюкоза: отсутствует,Кетоны: отсутствуют",
        "Кетоны: отсутствуют Кетоны: отсутствуют",
        "УЗИ Кетоны: отсутствуют, УЗИ почек: нормальный размер и структура, отсутствие опухолей",
        "Электрокардиограмма (ЭКГ): Сердечный ритм: синусовый, Сердечный ритм: синусовый, Отсутствие признаков аритмии или ишемии"
    ]

    for result in results:
        label_result = tk.Label(window, text=result)
        label_result.pack()


def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


def show_main_window():
    clear_window()

    header_frame = tk.Frame(window)
    header_frame.pack(pady=20)

    label_logo = tk.Label(header_frame, text="Логотип", font=("Arial", 24, "bold"))
    label_logo.pack(side=tk.LEFT)

    label_title = tk.Label(header_frame, text="МедКарта", font=("Arial", 24, "bold"))
    label_title.pack(side=tk.LEFT)

    label_welcome = tk.Label(window, text="Добро пожаловать, пациент!", font=("Arial", 16))
    label_welcome.pack(pady=20)

    button_view_tests = tk.Button(window, text="Просмотр анализов", command=view_tests)
    button_view_tests.pack(pady=10)

    button_view_results = tk.Button(window, text="Просмотр результатов", command=view_results)
    button_view_results.pack(pady=10)


# Создание главного окна приложения
window = tk.Tk()
window.title("МедКарта")

# Создание виджетов для окна входа пациента
label_username = tk.Label(window, text="Логин")
label_password = tk.Label(window, text="Пароль")
entry_username = tk.Entry(window)
entry_password = tk.Entry(window, show="*")
button_patient_login = tk.Button(window, text="Вход для пациента", command=patient_login)

label_username.pack(pady=10)
entry_username.pack()
label_password.pack(pady=10)
entry_password.pack()
button_patient_login.pack(pady=5)

# Запуск главного цикла приложения
window.mainloop()
