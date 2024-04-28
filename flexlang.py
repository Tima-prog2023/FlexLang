import tkinter as tk
from tkinter import font, messagebox
import re
import webbrowser

class MyInterpreter:
    def __init__(self, text_area, output_area):
        self.text_area = text_area
        self.output_area = output_area
        self.commands = {
            'print.str': self.print_str
            # Добавьте здесь другие команды и их соответствующие функции
        }

    def parse_code(self, code):
        tokens = re.findall(r'([a-zA-Z.]+)\("([^"]*)"\)|([();])', code)
        return tokens

    def execute_code(self):
        code = self.text_area.get("1.0", tk.END).strip()  # Удаляем символ новой строки
        tokens = self.parse_code(code)
        for token in tokens:
            command = token[0]
            argument = token[1]
            if command:  # Проверяем, не является ли команда пустой строкой
                if command in self.commands:
                    self.commands[command](argument)
                else:
                    print("Ошибка: Несуществующая команда -", command)

    def print_str(self, argument):
        self.output_area.insert(tk.END, argument + '\n')

def execute_code():
    output_area.delete("1.0", tk.END)  # Очищаем вывод перед каждым выполнением кода
    interpreter.execute_code()

def set_syntax_highlighting():
    # Определяем ключевые слова и строковые литералы
    keywords = ["print", "if", "else", "while", "for", "def", "class", "return"]
    string_literals = re.findall(r'"([^"]*)"', interpreter.text_area.get("1.0", tk.END))

    # Подсвечиваем ключевые слова
    for keyword in keywords:
        start = "1.0"
        while True:
            start = interpreter.text_area.search(keyword, start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(keyword)}c"
            interpreter.text_area.tag_add("keyword", start, end)
            start = end

    # Подсвечиваем строковые литералы
    for string_literal in string_literals:
        start = "1.0"
        while True:
            start = interpreter.text_area.search(f'"{string_literal}"', start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(string_literal) + 2}c"  # Учитываем кавычки
            interpreter.text_area.tag_add("string", start, end)
            start = end

def open_github():
    webbrowser.open_new_tab("https://github.com/your_username/flexlang")

def open_official_site():
    webbrowser.open_new_tab("https://your_website.com")

def show_about_info():
    about_info = """
    FlexLang 1.0.0(test)
    Github: click to open
    Official Site: click to open
    """
    tk.messagebox.showinfo("About FlexLang", about_info)

root = tk.Tk()
root.title("FlexLang")
root.geometry("1280x720")

# Добавляем иконку
root.iconbitmap(r"C:\Users\Admin\Desktop\Тимоша\python_projects\flexlang_logo.ico")

# Добавляем шрифт JetBrains Mono
font_style = font.Font(family="JetBrains Mono", size=12)

text_area = tk.Text(root, font=font_style)
text_area.pack(expand=True, fill='both')

output_area = tk.Text(root, font=font_style)
output_area.pack(expand=True, fill='both')

interpreter = MyInterpreter(text_area, output_area)

# Создаем меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Добавляем пункт меню "Run Code"
run_menu = tk.Menu(menu_bar, tearoff=0)
run_menu.add_command(label="Run Code", command=execute_code)
menu_bar.add_cascade(label="Run", menu=run_menu)

# Добавляем пункт меню "Syntax Highlighting"
menu_bar.add_command(label="Syntax Highlighting", command=set_syntax_highlighting)

# Добавляем пункт меню "About FlexLang"
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About FlexLang", command=show_about_info)
about_menu.add_command(label="Github", command=open_github)
about_menu.add_command(label="Official Site", command=open_official_site)
menu_bar.add_cascade(label="About", menu=about_menu)

# Создаем теги для подсветки синтаксиса
text_area.tag_configure("keyword", foreground="blue")
text_area.tag_configure("string", foreground="green")

root.mainloop()
