import tkinter as tk
from tkinter import filedialog as fd, messagebox

from functools import partial
import os

from services.functions import table_pdf_to_xlsx, open_browser


def callback():
    '''
    Callback do Repositório Selcionado para o Pegar o PDF
    '''
    global filename
    filename = fd.askopenfilename()
    extension = os.path.splitext(filename)
    if extension[1] != '.pdf':
        print('Erro, Usuário inseriu um formato não suportado.')
        messagebox.showerror(title="Erro no Formato", message="Por favor, seleciona um arquivo do tipo PDF.")
    else:
        ent_where.insert(0, filename)


def calldirectory():
    '''
    Callback da Path de Destino do Arquivo Processado
    '''
    global destination
    destination = fd.askdirectory()
    ent_dest.insert(0, destination)


filename = ''
destination = ''

# Create a window
window = tk.Tk()
window.title('Projetos - LATERMO')

# Frame do Body
frm_body= tk.Frame(master=window)
frm_body.pack(pady=(0, 10))

body_header = tk.Label(master=frm_body, text='Extrator de tabela do PDF', font=10, pady=20)
body_header.pack()

# Frame Origin and Components
frm_origin = tk.Frame(master=frm_body)
frm_origin.pack()

lbl_where = tk.Label(master=frm_origin, text='Selecione o PDF de Origem:', width=20)
lbl_where.pack(fill=tk.Y, side=tk.LEFT)
ent_where = tk.Entry(master=frm_origin)
ent_where.pack(fill=tk.Y, side=tk.LEFT, padx=10)
btn_where = tk.Button(master=frm_origin, text='Procurar...',command=callback)
btn_where.pack(fill=tk.Y, side=tk.LEFT)

# Frame Destination and Components
frm_destination = tk.Frame(master=frm_body)
frm_destination.pack(pady=(5,0))
lbl_dest = tk.Label(master=frm_destination, text='Selecione o Destino:', width=20)
lbl_dest.pack(fill=tk.Y, side=tk.LEFT)
ent_dest = tk.Entry(master=frm_destination)
ent_dest.pack(fill=tk.Y, side=tk.LEFT, padx=10)
btn_dest = tk.Button(master=frm_destination, text='Procurar...',command=calldirectory)
btn_dest.pack(fill=tk.Y, side=tk.LEFT)

# Frame to Finish Button
frm_finish = tk.Frame(master=frm_body)
frm_finish.pack(pady=(10,0))
btn_extract = tk.Button(master=frm_finish, text='Extract', font=8, foreground='blue', command= lambda: table_pdf_to_xlsx(filename, destination))
btn_extract.pack()

# Frame Footer and Components
frm_footer = tk.Frame(master=window)
frm_footer.pack(pady=(1,0))

link2 = tk.Label(master =frm_footer, text="Ajuda", fg="#31a4f0", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: open_browser("http://www.pgmec.uff.br/labs_de_pesquisa/laboratorio-de-analise-de-tensoes-3/"))

