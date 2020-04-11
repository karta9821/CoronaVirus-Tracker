import tkinter as tk
import Data



class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master.geometry('400x400')
        self.master.title('CoronaVirus Stats App')
        self.master.resizable(width=False, height=False)
        self.background = Background(self.master)

        self.list = Listbox(self.master)

        self.Info = Label(self.master, 'Choose Country:', padx=4, pady=2, relx=0.1, rely=0.1, color='#ace3fd')
        self.country_name = Label(self.master, 'Worlwide', padx=4, pady=4, relx=0.1, rely=0.65, color='#ace3fd')
        self.cases_label = Label(self.master, f'All cases: {Data.worldwide()[0]}', padx=4, pady=4,
                                 relx=0.1, rely=0.7, color='#ace3fd')
        self.deaths_label = Label(self.master, f'All deaths: {Data.worldwide()[1]}', padx=4, pady=4,
                                 relx=0.1, rely=0.75, color='#ace3fd')
        self.recovered_label = Label(self.master, f'All Recovered: {Data.worldwide()[2]}', padx=4, pady=4,
                                 relx=0.1, rely=0.8, color='#ace3fd')
        self.look_btn = Button(self.master, 'Search', relx=0.4, rely=0.1,
                               command=lambda: self.list.update(self.country_name, self.cases_label,
                                                        self.deaths_label, self.recovered_label))



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
        super(Label, self).__init__(master, padx=padx, pady=pady, bg=color, textvariable=self.text, width=15,
                                    justify='right')
        self.place(relx=relx, rely=rely)


class Listbox(tk.Listbox):
    def __init__(self, master):
        super(Listbox, self).__init__(master)
        self.dic_country = Data.available_countries()
        for k in  self.dic_country:
            self.insert('end', k)
        self.place(relx=0.1, rely=0.2)

    def update(self, country, cases, deaths, recovered):
        selected_country = self.get(self.curselection())
        url = self.dic_country[selected_country]
        country.text.set(f'Country: {selected_country}')
        c, d, r = Data.get_country_info(url)
        cases.text.set(f'Cases: {c}')
        deaths.text.set(f'Deaths: {d}')
        recovered.text.set(f'Recovered: {r}')


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
