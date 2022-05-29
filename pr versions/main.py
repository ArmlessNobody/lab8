from tkinter import *;
from tkinter import messagebox;
from tkinter.ttk import Combobox

class File(object):
    def __init__(self, name, begin ,end):
        self.name = name;
        self.begin = begin;
        self.end = end;

def window_deleted():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        window.destroy()

def show_window():
    row = 0;
    for i in range(0, len(list_files)):
        row += 1;
    i = 0;
    while i < len(list_memory_cell):
        if list_memory_cell[i] != "None":
            print("i = ", i, " = None");
            i= i +1;
        else:
            print("Else");
            j = i
            while j < len(list_memory_cell):
                if list_memory_cell == "None":
                    j = j +1;
                else:
                    row += 1;
                    i = j;
                    break;
    temp_text = "В таблицу будет " + str(row) + " строк!";
    info_window(temp_text);

def info_window(temp_text):
    new_window = Toplevel()
    new_window.title("Explorer.Dialog");
    new_window.geometry('450x100');
    lbl = Label(new_window, text= temp_text, font='Times 13');
    lbl.pack(side='top', anchor=N, ipadx=4, padx=1, ipady=3, pady=3);
    destroy_window_btn = Button(new_window, text="ОК", width=25, command = new_window.destroy, font='Times 13');
    destroy_window_btn.pack(side='top',  fill = X, ipadx=6, padx=4, ipady=5, pady=5);
    new_window.focus_set()
    new_window.grab_set()
    new_window.wait_window()
    new_window.mainloop();

def delete_file():

    if txt2.get() == "":
        info_window("Ввведите названия файла, который хотите удалить!")
    else:
        for i in range(0, len(list_files)):
            if list_files[i].name == txt2.get():
                temp_text = "Файл '" + list_files[i].name + "' размером '" + str(list_files[i].end  - list_files[i].begin) + " Кбайт' был успешно удален!";
                info_window(temp_text);
                break;
        else:
            temp_text = "Файл c названием'" + list_files[i].name + "' не существует, поэтому не был удалён!";
            info_window(temp_text);
        for j in range(list_files[i].begin, list_files[i].end):
            list_memory_cell[j] = "None";



def save_file():
    size_of_memory = 0;
    flag_save = 0;

    if txt.get() == "" or combo.get() == "None":
        txt.delete(0, END);
        info_window("Ввведите названия файла и его размер!")
    else:
        length = int(combo.get());
        print("size = ", combo.get());
        txt.delete(0, END);
        while i < len(list_memory_cell):
            j = i;
            print("i posle while ", i);
            while j < len(list_memory_cell):
                j = j + 1;
                if list_memory_cell[j] == "None":
                    size_of_memory += 1;
                    if size_of_memory == length:
                        for k in range(i, j):
                            list_memory_cell[k] = "No none";
                        file = File(txt.get(), i, j);
                        print("i = ", i, "j = ", j)
                        list_files.append(file);
                        flag_save = 1;
                        break;
            i = j;
            print("i posle  ", i);
            if flag_save == 1:
                temp_text = "Файл '" + txt.get() + "' размером '" + combo.get() + " Кбайт' был успешно сохранен!";

                info_window(temp_text);
            else:
                temp_text = "Файл '" + txt.get() + "' размером '" + combo.get() + " Кбайт' не был сохранен!";
                print("eror");
                info_window(temp_text);
                break;

    for i in range(0, 50):
        print(list_memory_cell[i]);




list_memory_cell = [];
for i in range(0, 50):
    list_memory_cell.append("None");



list_files = [];

window = Tk()



window.title("Explorer");
window.geometry('500x280');

lbl = Label(window, text="Введите название файла и выберите его размер в Кбайтах :", font='Times 14');
lbl.pack(side='top', anchor=W, ipadx=4, padx=1, ipady=3, pady=3);
f = Frame()
f.pack(side = TOP);
txt = Entry(f, width = 40, font='Times 14');
txt.pack(side= LEFT, anchor=N, fill='x', ipadx=7, padx=5, ipady=7, pady=1);
combo = Combobox(f,  state = "readonly")
combo['values'] = ("None", 3, 19, 20, 21, 21, 23, 24,25,26,27,28,29,30,31,32);
combo.current(0)
combo.pack(side = LEFT,  ipadx=7, padx=5, ipady=7, pady=1);
insert_btn = Button(window, text="Записать файл на диск", width=25, command = save_file, font='Times 13');
insert_btn.pack(side='top',  fill = X, ipadx=6, padx=4, ipady=7, pady=5);
lbl.pack(side='top', anchor=W, ipadx=4, padx=1, ipady=3, pady=3);
txt2 = Entry(window, font='Times 14');
txt2.pack(side= TOP, anchor=N, fill='x', ipadx=7, padx=5, ipady=7, pady=1);
veiw_btn = Button(window, text="Удалить", width=25, command = delete_file, font='Times 13');
veiw_btn.pack(side='top',  fill = X, ipadx=6, padx=4, ipady=7, pady=5);
txt2.pack(side= TOP, anchor=N, fill='x', ipadx=7, padx=5, ipady=7, pady=1);
veiw_btn = Button(window, text="Показать все файлы", width=25, command = show_window, font='Times 13');
veiw_btn.pack(side='top',  fill = X, ipadx=6, padx=4, ipady=4, pady=0);





window.mainloop();