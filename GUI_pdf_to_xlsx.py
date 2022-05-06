import tkinter as tk
from tkinter import filedialog as fd
import tabula

# Programa para extrair tabelas de um pdf.
window = tk.Tk()
window.title('Latermo')
tk.Label(text='Extract tables from pdf to Excel', font=10).pack()
frm_main = tk.Frame(master=window)
frm_main.pack()
lbl_where = tk.Label(master=frm_main, text='Select the file:', width=15)
lbl_where.pack(fill=tk.Y, side=tk.LEFT)
ent_where = tk.Entry(master=frm_main)
ent_where.pack(fill=tk.Y, side=tk.LEFT, padx=10)
def callback():
    global filename
    filename = fd.askopenfilename()
    ent_where.insert(0, filename)
btn_where = tk.Button(master=frm_main, text='Browse...',command=callback)
btn_where.pack(fill=tk.Y, side=tk.LEFT)

frm_second = tk.Frame(master=window)
frm_second.pack()
lbl_dest = tk.Label(master=frm_second, text='Select the local:', width=15)
lbl_dest.pack(fill=tk.Y, side=tk.LEFT)
ent_dest = tk.Entry(master=frm_second)
ent_dest.pack(fill=tk.Y, side=tk.LEFT, padx=10)
def calldirectory():
    global destination
    destination = fd.askdirectory()
    ent_dest.insert(0, destination)
btn_dest = tk.Button(master=frm_second, text='Browse...',command=calldirectory)
btn_dest.pack(fill=tk.Y, side=tk.LEFT)

def table_pdf_to_xlsx():
    tables = tabula.read_pdf(filename, pages='all')
    print(tables[0].to_excel(f'{destination}\output.xlsx', index=False))
tk.Button(text='Extract', font=8, foreground='blue', command=table_pdf_to_xlsx).pack()

window.geometry('350x130')
window.mainloop()
