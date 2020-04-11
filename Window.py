import tkinter as tk
import Data
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master.geometry('400x400')
        self.master.title('CoronaVirus Stats App')
        self.master.resizable(width=False, height=False)
        self.background = Background(self.master)
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.list = Listbox(self.master)

        self.Info = Label(self.master, 'Choose Country:', padx=4, pady=2, relx=0.0, rely=0.1, color='#cefcff')

        self.worldwide = Data.get_country_info()
        self.country_name = Label(self.master, 'Worlwide', padx=8, pady=4, relx=0.55, rely=0.02, color='#cefcff')
        self.cases_label = Label(self.master, f'All cases: {self.worldwide[0]}', padx=8, pady=4,
                                 relx=0.55, rely=0.07, color='#ace3fd')
        self.deaths_label = Label(self.master, f'All deaths: {self.worldwide[1]}', padx=8, pady=4,
                                 relx=0.55, rely=0.12, color='#ace3fd')
        self.recovered_label = Label(self.master, f'All Recovered: {self.worldwide[2]}', padx=8, pady=4,
                                 relx=0.55, rely=0.17, color='#ace3fd')

        self.active_cases_label = Label(self.master, 'Active cases', padx=4, pady=4, relx=0.56, rely=0.25, color='#cefcff')
        self.active_cases = Label(self.master, f'Currently Infected Patients:\n {self.worldwide[3]}',
                                  padx=4, pady=4, relx=0.56, rely=0.31, color='#ace3fd')
        self.mild_cond = Label(self.master, f'In Mild Condition:\n {self.worldwide[4]} ({self.worldwide[5]}%)',
                                  padx=4, pady=4, relx=0.56, rely=0.41, color='#ace3fd')
        self.critical = Label(self.master, f'Serious or Critical:\n {self.worldwide[-4]} ({self.worldwide[-3]}%)',
                padx=4, pady=4, relx=0.56, rely=0.51, color='#ace3fd')

        self.closed_cases_label = Label(self.master, 'Closed cases', padx=4, pady=4, relx=0.56, rely=0.63,
                                        color='#cefcff')
        self.closed_cases = Label(self.master, f'Cases which had an outcome:\n {self.worldwide[6]}',
                                  padx=4, pady=4, relx=0.56, rely=0.68, color='#ace3fd')
        self.recovered = Label(self.master, f'Recovered / Discharged:\n {self.worldwide[7]} ({self.worldwide[8]}%)',
                               padx=4, pady=4, relx=0.56, rely=0.78, color='#ace3fd')
        self.deaths = Label(self.master, f'Deaths:\n {self.worldwide[-2]} ({self.worldwide[-1]}%)',
                              padx=4, pady=4, relx=0.56, rely=0.88, color='#ace3fd')


        self.look_btn = Button(self.master, 'Search', relx=0.42, rely=0.1,
                               command=lambda: self.list.update(self.country_name, self.cases_label,
                                                        self.deaths_label, self.recovered_label, self.active_cases,
                                                                self.mild_cond, self.critical, self.closed_cases,
                                                                self.recovered, self.deaths))



class Entry(tk.Entry):
    def __init__(self, master, relx, rely):
        self.text = tk.StringVar()
        super(Entry, self).__init__(master, textvariable=self.text, font=55)
        self.place(relx=relx, rely=rely)


class Background(tk.Label):
    def __init__(self, master):
        self.image = tk.PhotoImage(file='images/background.png')
        super(Background, self).__init__(master, image=self.image)
        self.place(relwidth=1, relheight=1)


class Button(tk.Button):
    def __init__(self, master, text,  command, relx, rely):
        super(Button, self).__init__(master, text=text, command=command, height=1)
        self.place(relx=relx, rely=rely)


class Label(tk.Label):
    def __init__(self, master, info, padx, pady, relx, rely, color='#0579fe'):
        self.text = tk.StringVar()
        self.text.set(info)
        super(Label, self).__init__(master, padx=padx, pady=pady, bg=color, textvariable=self.text, width=21,
                                    justify='center')
        self.place(relx=relx, rely=rely)


class Listbox(tk.Listbox):
    def __init__(self, master):
        super(Listbox, self).__init__(master)
        self.dic_country = Data.available_countries()
        for k in self.dic_country:
            self.insert('end', k)
        self.place(relx=0.0, rely=0.2)



    def update(self, country, cases, deaths, recovered, active, mild, critical, closed, closed_recovered, closed_deaths):
        try:
            selected_country = self.get(self.curselection())
            url = self.dic_country[selected_country]
            if len(selected_country) < 15:
                country.text.set(f'Country: {selected_country}')
            else:
                country.text.set(selected_country)
            data = Data.get_country_info(url)
            cases.text.set(f'Cases: {data[0]}')
            deaths.text.set(f'Deaths: {data[1]}')
            recovered.text.set(f'Recovered: {data[2]}')
            active.text.set(f'Currently Infected Patients:\n {data[3]}')
            mild.text.set(f'In Mild Condition:\n {data[4]} ({data[5]}%)')
            critical.text.set(f'Serious or Critical:\n {data[-4]} ({data[-3]}%)',)
            closed.text.set(f'Cases which had an outcome:\n {data[6]}')
            closed_recovered.text.set(f'Recovered / Discharged:\n {data[7]} ({data[8]}%)')
            closed_deaths.text.set(f'Deaths:\n {data[-2]} ({data[-1]}%)')
        except Exception:
            pass




class Menu(tk.Menu):
    def __init__(self, master):
        super(Menu, self).__init__(master, tearoff=0)
        self.add_command(label='Info', command=self.info)

    def info(self):
        messagebox.showinfo('Info', 'All data comes from:\n"https://www.worldometers.info/coronavirus/"')

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.mainloop()