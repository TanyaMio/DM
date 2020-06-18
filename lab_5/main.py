from tkinter import *
import random


def variant(nzk):
    return (nzk % 26) +1


def student():
    slave = Toplevel(root)
    slave.title('Варіант')
    slave.grab_set()
    slave.focus_set()
    slave.minsize(200, 80)
    slave.maxsize(200, 80)
    nzk = 8113
    g = 81
    Label(slave, text='Дьяченко Тетяна\n'
                      'група ІВ-{}\n'
                      'варіант {}'.format(g, variant(nzk)),
          justify=LEFT, font="Arial 14").pack(fill='both')


def n_s_error():
    slave = Toplevel(root)
    slave.grab_set()
    slave.focus_set()
    slave.minsize(800, 80)
    slave.maxsize(800, 80)
    Label(slave, text='Кількість елементів або перестановок задано некоректно!',
          justify=LEFT, font="Arial 14").pack(fill='both')


def try_swap(i):

    global n, p_list, p

    j = 0
    while not p[j] > p[i]:
        j += 1

    if j > i:
        t = p[i]
        p[i] = p[j]
        p[j] = t
    else:
        k = 0
        while k == i or k == j or (p[k] > p[i] and k < i) or (p[k] > p[j] and k < j):
            k += 1

        r = j
        while p[r] > p[k] and r < k:
            r += 1

        t = p[k]
        p[k] = p[r]
        p[r] = t

        m = k - j - 1
        while m > 0:
            m -= 1
            if p[i] < p[j]:
                t = p[i]
                p[i] = p[j]
                p[j] = t

                i -= 1

    ident = 0
    ident_one = 0
    for per in p_list:
        for index in range(0, len(per)):
            if not per[index] == p[index]:
                ident_one -= 1
        if ident_one == 0:
            ident += 1
        ident_one = 0

    if ident == 0:
        p_new = list()

        for el in p:
            p_new.append(el)

        p_list.append(p_new)


def generP():

    global n, s, p_list, n_max, p

    if str(entn.get()).isdigit() and str(ents.get()).isdigit() and str(entn.get()) and str(ents.get()):
        n = int(str(entn.get()))
        s = int(str(ents.get()))
        if n > n_max or n < 1 or s > n or s < 1:
            n_s_error()
    else:
        n_s_error()

    p_list = list()
    p = list()
    random.seed()
    for i in range(0, n):
        el = random.randint(1, 100)
        while set(p).intersection(set([el, el])) == set([el, el]):
            el = random.randint(1, 100)
        p.append(el)

    p_new = list()

    for el in p:
        p_new.append(el)

    p_list.append(p_new)

    s -= 1

    while not s == 0:

        i = 0

        while p[i] > p[i + 1] and i < n-2:
                i += 1

        if p[i] < p[i+1]:
            try_swap(i)
            s -= 1
        else:
            break

    window2()


def window2():
    global n, s, p_list

    slave = Toplevel(root)
    slave.title('Отримані перестановки')
    slave.minsize(500, 250)
    slave.maxsize(500, 250)
    scrollbary = Scrollbar(slave)
    scrollbary.pack(side=RIGHT, fill=Y)

    mylist = Listbox(slave, yscrollcommand=scrollbary.set)
    for el in p_list:
        mylist.insert(END, str(el))

    mylist.pack(side=RIGHT, fill=BOTH, expand=TRUE)
    scrollbary.config(command=mylist.yview)


root = Tk()
root.title('Задати параметри')
root.minsize(680, 400)

n_max = 10 + 8113%11
n = 0
s = 0
p_list = list()
p = []

but_student = Button(root, text='Студент', font='Arial 12',
                     command=student, width = 20)
but_student.pack()

Label(root, text='Кількість елементів (n, максимальне значення - {}):'.format(n_max)).pack()
entn = Entry(root, width=10, bd=3, state=NORMAL)
entn.pack()

Label(root, text='Кількість перестановок (s):').pack()
ents = Entry(root, width=10, bd=3, state=NORMAL)
ents.pack()


but_OK = Button(root, text='Згенерувати перестановки', font='Arial 12', command=generP)
but_OK.pack()


root.mainloop()
