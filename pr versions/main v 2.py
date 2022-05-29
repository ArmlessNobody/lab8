from tkinter import *;
from tkinter import messagebox;
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
import matplotlib.pyplot as plt;


class File(object):
    def __init__(self, name, begin, end):
        self.name = name;
        self.begin = begin;
        self.end = end;


def window_deleted():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        window.destroy()


def address(value):
    value = str(hex(value)).upper();
    if value == "0x0":
        return "0x000000"
    elif len(value) == 3:
        temp_value = "0x00000";
    elif len(value) == 4:
        temp_value = "0x0000";
    elif len(value) == 5:
        temp_value = "0x000";
    elif len(value) == 6:
        temp_value = "0x00";

    for i in range(2, len(value)):
        temp_value += value[i];

    return temp_value;



def show_window():
    show_window = Toplevel();
    show_window.title("Explorer.ShowWindow");

    if len(list_files) != 0:
        lbl = Label(show_window, text="Название файла и адреса ячеек памяти, в которых они хранятся : ", font='Times 15');
        lbl.pack(side='top', fill=BOTH, anchor=N, ipadx=4, padx=1, ipady=3, pady=3, expand=True);
        for j in range(0, len(list_files)):
            temp_text = "'" + list_files[j].name + "' — " + address(list_files[j].begin) + "_" + address(list_files[j].end);
            lbl = Label(show_window, text=temp_text, font='Times 13');
            lbl.pack(side='top', fill=BOTH, anchor=N, ipadx=4, padx=1, ipady=3, pady=3, expand=True);

    i = 0;
    lbl = Label(show_window, text="Список свободных адресов памяти : ",
                font='Times 15');
    lbl.pack(side='top', fill=BOTH, anchor=N, ipadx=4, padx=1, ipady=3, pady=3, expand=True);
    while i < len(list_memory_cell):

        if list_memory_cell[i] == "None":

            j = i;
            while j < len(list_memory_cell):
                if list_memory_cell[j] == "None":
                    j = j + 1;


                    if j == len(list_memory_cell):
                        temp_text = address(i) + "_" + address(j);
                        lbl = Label(show_window, text=temp_text, font='Times 13');
                        lbl.pack(side='top', fill=BOTH, anchor=N, ipadx=4, padx=1, ipady=3, pady=3, expand=True);
                        i = j
                        print("BREAK");
                        break;

                else:
                    temp_text =  address(i) + "_" + address(j - 1);
                    lbl = Label(show_window, text=temp_text, font='Times 13');
                    lbl.pack(side='top', fill=BOTH, anchor=N, ipadx=4, padx=1, ipady=3, pady=3, expand=True);
                    i = j
                    break;
        else:
            i += 1;





    destroy_window_btn = Button(show_window, text="ОК", width=25, command=show_window.destroy, font='Times 13');
    destroy_window_btn.pack(side='top', fill=X, ipadx=6, padx=4, ipady=5, pady=5);
    show_window.focus_set()
    show_window.grab_set()
    show_window.mainloop();


def info_window(temp_text):
    info_window = Toplevel();
    info_window.title("Explorer.Dialog");
    lbl = Label(info_window, text=temp_text, font='Times 13');
    lbl.pack(side='top', anchor=N, ipadx=4, padx=1, ipady=3, pady=3);
    destroy_window_btn = Button(info_window, text="ОК",  command=info_window.destroy, font='Times 13');
    destroy_window_btn.pack(side='top', fill=BOTH, ipadx=6, padx=4, ipady=5, pady=5, expand = True);
    info_window.focus_set()
    info_window.grab_set()
    info_window.mainloop();




def delete_file():
    if txt2.get() == "":
        info_window("Ввведите названия файла, который хотите удалить!")
    else:
        for i in range(0, len(list_files)):
            if list_files[i].name == txt2.get():
                temp_text = "Файл '" + list_files[i].name + "' размером '" + str(
                    list_files[i].end - list_files[i].begin + 1) + " Кбайт' был успешно удален!";
                txt.delete(0, END);

                for j in range(list_files[i].begin, list_files[i].end + 1):
                    list_memory_cell[j] = "None";
                for k in range(0, len(list_memory_cell)):
                    print(list_memory_cell[k], " ", k);
                list_files.pop(i);
                info_window(temp_text);
                break;
        else:
            temp_text = "Файл c названием'" + list_files[i].name + "' не существует, поэтому не был удалён!";
            txt.delete(0, END);
            for i in range(0, len(list_memory_cell)):
                print(list_memory_cell[i], " ", i);
            info_window(temp_text);

def load():
    n = 0;
    try:
        file_name = fd.askopenfilename();
        with open(file_name, 'r') as file:

            list_files.clear();
            list_memory_cell.clear();


            str2 = file.readlines();

            for i in range(0, len(str2)):

                str = str2[i];
                name = "";
                begin = "";
                end = "";
                flag = 0;
                flag2 = 0;

                for i in range(0, len(str)):
                    if str[i] == " ":
                        break;
                    name += str[i];
                    flag = i + 2;
                for i in range(flag, len(str)):
                    if str[i] == " ":
                        break;
                    begin += str[i];
                    flag2 = i + 2;
                for i in range(flag2, len(str)):
                    if str[i] == " ":
                        break;
                    end += str[i];

                temp_file = File(name, int(begin), int(end));
                list_files.append(temp_file);

    except:
        n = 1;
        info_window('Файл не был выбран!')

    if n == 0:
        for i in range(0, 20):
            list_memory_cell.append("None");
        for i in range(0, len(list_files)):
            for j in range (list_files[i].begin, list_files[i].end + 1):
                list_memory_cell[j] = "No none"
        info_window('Данные успешно загружены из файла!');


def save():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),("HTML files", "*.html;*.htm"), ("All files", "*.*")))
    with open(file_name, 'w') as file:
        for i in range (0, len(list_files)):
            file.write(list_files[i].name + " " + str(list_files[i].begin) + " " + str(list_files[i].end) + "\n");

    file_name = "Данные сохранены в файл '" + file_name + "'!"
    info_window(file_name);
def save_file():
    flag_save = 0;
    flag_break = 0;
    if txt.get() == "" or combo.get() == "None":
        info_window("Ввведите названия файла и его размер!")
    else:
        for i in range(0,len(list_files)):
            if list_files[i].name == txt.get():
                flag_break = 1;
                break;
        if flag_break == 1:
            temp_text = "Файл с названием '" + txt.get() + "' уже существует!";
            txt.delete(0, END);
            info_window(temp_text);

        else:

            length = int(combo.get());

            for i in range(0, len(list_memory_cell)):
                j = i;
                print(list_memory_cell[i], " = ", i);
                if list_memory_cell[i] == "None":

                    size_of_memory = 0;
                    print ("Cycle");
                    print(list_memory_cell[i], " j ", j)
                    while j < len(list_memory_cell):
                        if list_memory_cell[j] == "None":

                            size_of_memory += 1;
                            if size_of_memory == length:
                                print("length = ", length, "size_of_memory = ", size_of_memory);
                                for k in range(i, j + 1):
                                    list_memory_cell[k] = "No none";
                                file = File(txt.get(), i, j);
                                print("i = ", i, "j = ", j)
                                list_files.append(file);
                                flag_save = 1;
                                print("break")
                                break;
                        else:
                            break;
                        j += 1;

                if flag_save == 1:
                    temp_text = "Файл '" + txt.get() + "' размером '" + combo.get() + " Кбайт' был успешно сохранен!";
                    txt.delete(0, END);
                    for l in range(0, len(list_memory_cell)):
                        print(list_memory_cell[l], " ", i);
                    info_window(temp_text);
                    break;

            if flag_save == 0:
                temp_text = "Файл '" + txt.get() + "' размером '" + combo.get() + " Кбайт' не был сохранен!";
                print("eror");
                for i in range(0, len(list_memory_cell)):
                    print(list_memory_cell[i], " ", i);
                txt.delete(0, END);
                info_window(temp_text);





list_memory_cell = [];
for i in range(0, 20):
    list_memory_cell.append("None");


list_files = [];

window = Tk()

window.title("Explorer");
window.geometry('500x280');

menu = Menu(window);
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новая резервная копия гибкого омагнитного диска!');
new_item.add_separator();
new_item.add_command(label='Загрузить данные из резервной копии гибкого магнитного диска!', command = load);
new_item.add_separator();
new_item.add_command(label='Cохранить резервную копию гибкого магнитного диска!', command = save) ;
menu.add_cascade(label='Меню', menu=new_item);
window.config(menu=menu);

lbl = Label(window, text="Введите название файла и выберите его размер в Кбайтах :", font='Times 14');
lbl.pack(side='top', anchor=W, ipadx=4, padx=1, ipady=3, pady=3);
f = Frame()
f.pack(side=TOP);
txt = Entry(f, width=40, font='Times 14');
txt.pack(side=LEFT, anchor=N, fill='x', ipadx=7, padx=5, ipady=7, pady=1);
combo = Combobox(f, state="readonly")
combo['values'] = (3, 4, 5, 21, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32);
combo.current(0)
combo.pack(side=LEFT, ipadx=7, padx=5, ipady=7, pady=1);
insert_btn = Button(window, text="Записать файл на диск", width=25, command=save_file, font='Times 13');
insert_btn.pack(side='top', fill=X, ipadx=6, padx=4, ipady=7, pady=5);
lbl.pack(side='top', anchor=W, ipadx=4, padx=1, ipady=3, pady=3);
txt2 = Entry(window, font='Times 14');
txt2.pack(side=TOP, anchor=N, fill='x', ipadx=7, padx=5, ipady=7, pady=1);
veiw_btn = Button(window, text="Удалить", width=25, command=delete_file, font='Times 13');
veiw_btn.pack(side='top', fill=X, ipadx=6, padx=4, ipady=7, pady=5);
txt2.pack(side=TOP, anchor=N, fill='x', ipadx=7, padx=5, ipady=7, pady=1);
veiw_btn = Button(window, text="Показать все файлы", width=25, command=show_window, font='Times 13');
veiw_btn.pack(side='top', fill=X, ipadx=6, padx=4, ipady=4, pady=0);

window.mainloop();