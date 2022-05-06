import tabula
from datetime import datetime
from tkinter import messagebox
import webbrowser

def table_pdf_to_xlsx(filename, destination):
    if filename == '' or destination == '':
        messagebox.showwarning(title="Campos Vazios", message="Por favor, selecione os dois campos.")
    else:
        print(f'Filename: {filename}')
        tables = tabula.read_pdf(filename, pages='all')
        print(f'Destination: {destination}')
        now = datetime.now()
        now_adjusted = now.strftime('%d_%m_%Y_%H_%M_%S')
        print(tables[0].to_excel(f'{destination}\{now_adjusted}.xlsx', index=False))
        messagebox.showinfo('Sucesso', message=f"Salvo com sucesso em {destination}")



def open_browser(url):
    webbrowser.open_new(url)
