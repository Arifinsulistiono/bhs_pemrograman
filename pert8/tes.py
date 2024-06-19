try:
    import tkinter as tk
    from tkinter import Frame, Label, LabelFrame, Toplevel, ttk,messagebox
    from datetime import datetime
    from tkcalendar import Calendar
    from PIL import Image, ImageTk
except ImportError as err:
    print( str(err) )

# __KONSTANTA__
PIL1 = "Cuci Kering"
PIL2 = "Cuci Basah"
PIL3 = "Cuci Setrika"
PIL4 = "Tunai"
PIL5 = "Qris"
DEFAULT_FONT = "Helvetica",12
TITLE_FONT = "Helvetica",12,"bold"
BGCOLOR = "#B8ECFD"
CALENDERIME = "assets/calendar.png"
QRISIMAGE = "assets/qris.png"
# __VARIABLES__
jenis_layanan = 0
pesanan = []

# __FUNCTIONS__
def ubah_state(enabled):
    if enabled:
        nama_entry.config(state=tk.NORMAL)
        no_telepon_entry.config(state=tk.NORMAL)
        jenis_combobox.config(state=tk.NORMAL)
        jumlah_combobox.config(state=tk.NORMAL)
        metode_pembayaran_combobox.config(state=tk.NORMAL)
        tanggal_pengambilan_entry.config(state=tk.NORMAL)
        alamat_entry.config(state=tk.NORMAL)
    else:
        nama_entry.config(state=tk.DISABLED)
        no_telepon_entry.config(state=tk.DISABLED)
        jenis_combobox.config(state=tk.DISABLED)
        jumlah_combobox.config(state=tk.DISABLED)
        metode_pembayaran_combobox.config(state=tk.DISABLED)
        tanggal_pengambilan_entry.config(state=tk.DISABLED)
        alamat_entry.config(state=tk.DISABLED)
def pesan_clicked():
    nama = nama_entry.get()
    no_telepon = no_telepon_entry.get()
    tanggal_pengambilan = tanggal_pengambilan_entry.get()
    jenis = jenis_combobox.get()
    jumlah = jumlah_combobox.get()
    metode_pembayaran = metode_pembayaran_combobox.get()
    total = total_entry.get()
    if nama and no_telepon and tanggal_pengambilan and jenis and jumlah and metode_pembayaran and total:
        tanggal_pesan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not jenis == PIL1 and not jenis == PIL2 and not jenis == PIL3:
            messagebox.showerror("Salah data","Mohon inputkan yang benar")
            return
        pesanan.append((tanggal_pesan,nama,no_telepon,jenis,jumlah,metode_pembayaran,total,tanggal_pengambilan))
        update_invoice(nama,jenis,jumlah,total,tanggal_pengambilan,metode_pembayaran,tanggal_pesan)
        batal_pesan_clicked()
        invoice_frame.pack(padx=5,pady=(0,10)) 
        if metode_pembayaran == PIL5:
            bayar_method_title.config(text="QRIS")
            bayar_method_tunai.grid_forget()
            bayar_method_content.grid(row=1,column=0, sticky='n',pady=10,padx=(0,5))
        else:
            bayar_method_title.config(text="TUNAI")
            bayar_method_content.grid_forget()
            bayar_method_tunai.grid(row=1,column=0, sticky='n',pady=10,padx=5)
        pesan_button.grid_forget()
        batal_pesan_button.grid_forget()
        pesan_ulang_button.grid(row=8, column=0, padx=5, pady=10,sticky="ew",columnspan=2)
        ubah_state(False)
    else:
        messagebox.showerror("Error", "Harap isi semua kolom!")
def update_invoice(nama, jenis, jumlah, total, tanggal_pengambilan, metode_pembayaran,tanggal_pesan):
    invoice_text.config(state=tk.NORMAL)
    invoice_text.delete(1.0, tk.END)
    invoice_text.insert(tk.END, f"Tanggal Pesan: {tanggal_pesan}\n")
    invoice_text.insert(tk.END, f"Nama: {nama}\n")
    invoice_text.insert(tk.END, f"Jenis Laundry: {jenis}\n")
    invoice_text.insert(tk.END, f"Jumlah (kg): {jumlah}\n")
    invoice_text.insert(tk.END, f"Total Harga: {total}\n")
    invoice_text.insert(tk.END, f"Tanggal Pengambilan: {tanggal_pengambilan}\n")
    invoice_text.insert(tk.END, f"Jenis Pembayaran: {metode_pembayaran}\n")
    invoice_text.insert(tk.END, "\nTERIMAKASIH TELAH MENGGUNAKAN JASA KAMI")
    invoice_text.config(state=tk.DISABLED)
def batal_pesan_clicked():
    global jenis_layanan
    nama_entry.delete(0, tk.END)
    no_telepon_entry.delete(0, tk.END)
    tanggal_pengambilan_entry.delete(0, tk.END)
    alamat_entry.delete(0,tk.END)
    jenis_combobox.set("")
    jumlah_combobox.set("")
    metode_pembayaran_combobox.set("")
    total_entry.config(state=tk.NORMAL)
    total_entry.delete(0,tk.END)
    total_entry.config(state=tk.DISABLED)
    jenis_layanan = 0
def pesan_ulang_cilcked():
    batal_pesan_clicked()
    ubah_state(True)
    pesan_ulang_button.grid_forget()
    invoice_frame.pack_forget()
    pesan_button.grid(row=8, column=0, padx=5, pady=10,sticky="ew")
    batal_pesan_button.grid(row=8, column=1, padx=5, pady=10,sticky="ew")
def jenis_selected(event):
    global jenis_layanan
    selected_item = jenis_combobox.get()
    if selected_item == PIL1:
        jenis_layanan = 8000
    elif selected_item == PIL2:
        jenis_layanan = 9000
    elif selected_item == PIL3:
        jenis_layanan = 10000

    if not jumlah_combobox.get() == "":
        total = jenis_layanan * int(jumlah_combobox.get())
        total_entry.config(state=tk.NORMAL)
        total_entry.delete(0,tk.END)
        total_entry.insert(0,str(total))
        total_entry.config(state=tk.DISABLED)
def jumlah_selected(event):
    global jenis_layanan
    total = jenis_layanan * int(jumlah_combobox.get())
    total_entry.config(state=tk.NORMAL)
    total_entry.delete(0,tk.END)
    if not total == 0:
        total_entry.insert(0,str(total))
    total_entry.config(state=tk.DISABLED)
def pick_date():
    # Purpose: Menampilkan date picker
    global cal
    date_win = Toplevel()
    date_win.grab_set()
    date_win.title("Pilih Tanggal Ambil")
    l = window.winfo_x() + 410
    t = window.winfo_y() + 240
    date_win.geometry(f'250x220+{l}+{t}')        
    date_win.resizable(False,False)
    cal = Calendar(date_win, selectmode='day', year=2024, month=5, day=31)
    cal.pack(pady=20)
    cal.bind("<<CalendarSelected>>", on_date_select)
def on_date_select(event):
    selected_date = cal.selection_get()
    tanggal_pengambilan_entry.delete(0,tk.END)
    tanggal_pengambilan_entry.insert(tk.END, str(selected_date))
def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.Resampling.LANCZOS)
    return resized_image
window = tk.Tk()
window.title("VANDA LAUNDRY")
window.config(bg=BGCOLOR)
style = ttk.Style()
style.configure("Background.TLabel",background=BGCOLOR)

# TITLE WIDGET
title_app = Label(window,text="VANDA LAUNDRY",font=TITLE_FONT, background=BGCOLOR)
title_app.pack(pady=(10,0))

# PESAN WIDGETS
pesan_frame = Frame(window, bg=BGCOLOR)
pesan_frame.pack()

# Frame content
content_frame = tk.Frame(pesan_frame, bg=BGCOLOR)
content_frame.pack(padx=20, pady=10)

# Label Nama
nama_label = tk.Label(content_frame, text="Nama", font=DEFAULT_FONT,background=BGCOLOR)
nama_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Entry Nama
nama_entry = ttk.Entry(content_frame, font=DEFAULT_FONT,background=BGCOLOR, width=22)
nama_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Label No. Telepon
no_telepon_label = tk.Label(content_frame, text="No. Telepon", font=DEFAULT_FONT,background=BGCOLOR)
no_telepon_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Entry No. Telepon
no_telepon_entry = ttk.Entry(content_frame, font=DEFAULT_FONT,background=BGCOLOR, width=22)
no_telepon_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Label Alamat
alamat_label = tk.Label(content_frame, text="Alamat", font=DEFAULT_FONT,background=BGCOLOR)
alamat_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Entry Alamat
alamat_entry = ttk.Entry(content_frame, font=DEFAULT_FONT,background=BGCOLOR, width=22)
alamat_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Label Tanggal Pengambilan
tanggal_pengambilan_label = tk.Label(content_frame, text="Tanggal Pengambilan", font=DEFAULT_FONT,background=BGCOLOR)
tanggal_pengambilan_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

# Entry Tanggal Pengambilan
tanggal_pengambilan_entry = ttk.Entry(content_frame, font=DEFAULT_FONT,background=BGCOLOR, width=22)
tanggal_pengambilan_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Button Calendar
calendarImg = resize_image(CALENDERIME, 15,15)
calndarresized = ImageTk.PhotoImage(calendarImg)
calendar_button = ttk.Button(content_frame, image=calndarresized,command=pick_date,style="Background.TLabel")
calendar_button.grid(row=3, column=2, padx=5, pady=5)

# Label Jenis
jenis_label = tk.Label(content_frame, text="Jenis", font=DEFAULT_FONT,background=BGCOLOR)
jenis_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

# Combobox Jenis
jenis_combobox = ttk.Combobox(content_frame, values=[PIL1, PIL2, PIL3], font=DEFAULT_FONT,background=BGCOLOR)
jenis_combobox.grid(row=4, column=1, padx=5, pady=5, sticky="w")
jenis_combobox.bind("<<ComboboxSelected>>", jenis_selected)

# Label Jumlah
jumlah_label = tk.Label(content_frame, text="Jumlah (kg)", font=DEFAULT_FONT,background=BGCOLOR)
jumlah_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

# Combobox Jumlah
jumlah_combobox = ttk.Combobox(content_frame, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], font=DEFAULT_FONT,background=BGCOLOR)
jumlah_combobox.grid(row=5, column=1, padx=5, pady=5, sticky="w")
jumlah_combobox.bind("<<ComboboxSelected>>", jumlah_selected)
# Label Total
total_label = tk.Label(content_frame, text="Total", font=DEFAULT_FONT,background=BGCOLOR)
total_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

# Entry Total
total_entry = ttk.Entry(content_frame, font=DEFAULT_FONT,background=BGCOLOR, width=22, state=tk.DISABLED)
total_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

# Label Metode Pembayaran
metode_pembayaran_label = tk.Label(content_frame, text="Metode pembayaran", font=DEFAULT_FONT,background=BGCOLOR)
metode_pembayaran_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

# Combobox Metode Pembayaran
metode_pembayaran_combobox = ttk.Combobox(content_frame, values=[PIL4, PIL5], font=DEFAULT_FONT,background=BGCOLOR)
metode_pembayaran_combobox.grid(row=7, column=1, padx=5, pady=5, sticky="w")

# Button Pesan
pesan_button = ttk.Button(content_frame, text="Pesan", command=pesan_clicked)
pesan_button.grid(row=8, column=0, padx=5, pady=10,sticky="ew")
# Button Batal Pesan
batal_pesan_button = ttk.Button(content_frame, text="Batal Pesan", command=batal_pesan_clicked)
batal_pesan_button.grid(row=8, column=1, padx=5, pady=10,sticky="ew")
# Button Pesan Ulang
pesan_ulang_button = ttk.Button(content_frame, text="Pesan Ulang", command=pesan_ulang_cilcked)
# Frame invoice
invoice_frame = LabelFrame(pesan_frame,text="Invoice",bg=BGCOLOR)
invoice_text = tk.Text(invoice_frame,height=10)
invoice_text.grid(row=0,column=0,padx=5)
bayar_method_frame = Frame(invoice_frame, bg=BGCOLOR)
bayar_method_frame.grid(row=0,column=1,sticky='ns')
bayar_method_title = tk.Label(bayar_method_frame, text="QRIS",background=BGCOLOR)
bayar_method_title.grid(row=0,column=0,sticky="n")
qrisImg = resize_image(QRISIMAGE, 100,100)
qrisResized = ImageTk.PhotoImage(qrisImg)
bayar_method_content = tk.Label(bayar_method_frame, image=qrisResized)
bayar_method_tunai = tk.Label(bayar_method_frame,text="Harap pembayaran\ndi kasir pada saat\ntanggal\npengambilan\nLaundry.\n\nTerimakasih",background=BGCOLOR)
# __RIWAYAT WIDGETS__
riwayat_frame = Frame(window)
tree_riwayat = ttk.Treeview(riwayat_frame, columns=("Tanggal Pesan", "Nama", "No Telepon", "Jenis Layanan", "Jumlah (Kg)", "Metode Pembayaran", "Total Harga", "Tanggal Diambil"), show='headings',height=23)
tree_riwayat.heading("Tanggal Pesan", text="Tanggal Pesan")
tree_riwayat.heading("Nama", text="Nama")
tree_riwayat.heading("No Telepon", text="No Telepon")
tree_riwayat.heading("Jenis Layanan", text="Jenis Layanan")
tree_riwayat.heading("Jumlah (Kg)", text="Jumlah (Kg)")
tree_riwayat.heading("Metode Pembayaran", text="Metode Pembayaran")
tree_riwayat.heading("Total Harga", text="Total Harga")
tree_riwayat.heading("Tanggal Diambil", text="Tanggal Diambil")
tree_riwayat.column("Tanggal Pesan", width=150)
tree_riwayat.column("Nama", width=100)
tree_riwayat.column("No Telepon", width=100)
tree_riwayat.column("Jenis Layanan", width=100)
tree_riwayat.column("Jumlah (Kg)", width=100)
tree_riwayat.column("Metode Pembayaran", width=150)
tree_riwayat.column("Total Harga", width=100)
tree_riwayat.column("Tanggal Diambil", width=150)
# Update riwayat pembelian setiap kali masuk ke halaman riwayat
def update_riwayat():
    """Update riwayat pembelian pada treeview"""
    for item in tree_riwayat.get_children():
        tree_riwayat.delete(item)
    for pesan in pesanan:
        tree_riwayat.insert("", tk.END, values=pesan)
tree_riwayat.bind("<Visibility>", lambda event: update_riwayat())
tree_riwayat.pack()
# Membuat menu bar
def quit():
    window.quit()
def hide():
    pesan_frame.pack_forget()
    riwayat_frame.pack_forget()
def show_pesan():
    hide()
    pesan_frame.pack(padx=10)
def show_riwayat():
    """
    Purpose: Menampilkan Page Riwayat Pesanan
    """
    hide()
    riwayat_frame.pack(padx=10,pady=10)
def help():
    """
    Purpose: Memapilkan help box
    """
    messagebox.showinfo("Help","Apabila ada kendala\ndan memerlukan\ninformasi lebih\nlanjut. Hubungi\nnomor di bawah ini :\n\n08819097932")
# end def
menubar = tk.Menu(window)
submenu = tk.Menu(menubar, tearoff=0)   
submenu.add_command(label='Pesan', command=show_pesan)
submenu.add_command(label='Riwayat', command=show_riwayat)
submenu.add_separator()
submenu.add_command(label='Quit', command=quit)            
menubar.add_cascade(label="Menu", menu=submenu)
menubar.add_command(label="Help",command=help)
window.config(menu=menubar)
window.mainloop()