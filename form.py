import tkinter as tk
from tkinter import ttk, messagebox 

def popup_sukses(nama, ttgl, email, gender, jurusan):
   
    pop = tk.Toplevel(root)
    pop.title("Konfirmasi Pendaftaran")
    pop.geometry("400x320")
    pop.resizable(False, False)
    pop.configure(bg="#ffffff")

    pop.transient(root)
    pop.grab_set()

    lbl_header = tk.Label(
        pop,
        text="Pendaftaran Berhasil!",
        font=("Helvetica", 14, "bold"),
        fg="#006aff",
        bg="#2200FF",
        pady=12
    )
    lbl_header.pack(fill="x")

    frame_data = tk.Frame(pop, bg="ffffff", padx=25, pady=20)
    frame_data.pack(fill="both", expand=True)

    list_data = [
        ("Nama", nama),
        ("TTL", ttgl),
        ("Email", email),
        ("Jenis Kelamin", gender),
        ("Jurusan", jurusan)
    ]

    for i, (label, val) in enumerate (list_data):
        tk.Label(
            frame_data, text=label, font=("Helvetica", 10, "bold"),
            bg="ffffff", fg="#0B2AF5", anchor="w"
            ).grid(row=i, column=0, sticky="w", pady=4)

        tk.Label(
            frame_data, text=":", font=("Helvetica", 10, "bold"),
            bg="ffffff", fg="#94A2EA"
            ).grid(row=i, column=1, padx=8, pady=4)

        tk.Label(
            frame_data, text=val, font=("Helvetica", 10),
            bg="ffffff", fg="555555", anchor="w"
            ).grid(row=i, column=2, sticky="w", pady=4)

        btn_ok = tk.Button(
            pop,
            text="OK",
            font=("Helvetica", 10, "bold"),
            bg="#7092fa",
            fg="white",
            width=12,
            bd=0,
            cursor="hand2",
            command=pop.destroy
            )
        btn_ok.pack(pady=(0, 20))


def simpan_data():
    nama = entry_nama.get()
    ttgl = entry_ttgl.get()
    email = entry_email.get()
    gender = var_gender.get()
    jurusan = combo_jurusan.get()

    if not nama or not ttgl or not email or jurusan == "-- Pilih Jurusan --":
        messagebox.showwarning ("Peringatan", "Mohon isi semua data yang diperlukan!")
    return
            

    popup_sukses(nama, ttgl, email, gender, jurusan)

    reset_form()

def reset_form():
        entry_nama.delete(0, tk.END)
        entry_ttgl.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        var_gender.set("Laki-laki")
        combo_jurusan.current(0)

root = tk.Tk()
root.title("Form Pendaftaran GUI")
root.geometry("600x520")
root.resizable(True, True)
root.state('zoomed') 

label_judul = tk.Label(root, text="FORM PENDAFTARAN MAHASISWA", bg="#0a0ab9", fg="#ffffff", font=("Helvetica", 14, "bold"))
label_judul.pack(fill="x", pady=15)

frame_form = tk.Frame(root, bg="#240ab9", padx=20, pady=10)
frame_form.pack(fill="both", expand=True) # both = melebar (sumbu X) dan meninggi (sumbu Y)


lbl_nama = tk.Label(frame_form, font=("Helvetica", 10))
lbl_nama.pack(fill="x", pady=(15, 0))

entry_nama = tk.Entry(frame_form, font=('Helvetica, 10'))
entry_nama.pack(fill="x", pady=(0, 10))


lbl_ttgl =tk.Label(frame_form, bg="#8f8dfb", text="Tempat/Tanggal Lahir:", font="bold", anchor="w")
lbl_ttgl.pack(fill="x", pady=(5,0))

entry_ttgl = tk.Entry(frame_form, font=("Helvetica", 10))
entry_ttgl.pack(fill="x", pady=(0,10))


lbl_email = tk.Label(frame_form, bg="#8db2fb", text="Email:", font="bold", anchor="w")
lbl_email.pack(fill="x", pady=(5, 0))

entry_email = tk.Entry(frame_form, font=("Helvetica", 10))
entry_email.pack(fill="x", pady=(0,10))


lbl_gender = tk.Label(frame_form, bg="#8dc9fb", text="Jenis Kelamin:", font="bold", anchor="w")
lbl_gender.pack(fill="x", pady=(5, 0))

var_gender = tk.StringVar(value="Laki-laki")
frame_gender = tk.Frame(frame_form, bg="#f8f2f9", highlightbackground="#cccccc", padx=20, pady=10)
frame_gender.pack(fill="x", pady=(0,10))

rb_pria = tk.Radiobutton(frame_gender, text="Laki-laki", font="bold", variable=var_gender, value="Laki-laki")
rb_pria.pack(side="left", padx=(0,10))

rb_wanita =tk.Radiobutton(frame_gender, text="Perempuan", font="bold", variable=var_gender, value="Perempuan")
rb_wanita.pack(side="left")


lbl_jurusan = tk.Label(frame_form, text="Jurusan / Pilihan:", font="bold", anchor="w")
lbl_jurusan.pack(fill="x", pady=(5,0))

root.option_add("*TCombobox*Listbox.font", ("Helvetica", 12))

daftar_jurusan = ["--Pilih Jurusan--", "Teknik Kimia", "Farmasi", "Kedokteran", "Teknik Industri"]
combo_jurusan = ttk.Combobox(frame_form, values="daftar_jurusan", state="readonly", font=("Helvetica", 12))
combo_jurusan.current(0)
combo_jurusan.pack(fill="x", pady=(0, 20))

frame_tombol = tk.Frame(frame_form, bg="#0a0ab9")
frame_tombol.pack(fill="x")

btn_simpan = tk.Button(frame_tombol, text="Daftar", bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), command=simpan_data)
btn_simpan.pack(side="left", fill="x", expand=True, padx=(0, 40))

btn_reset = tk.Button(frame_tombol, text="Reset", bg="#f44336", fg="white", font=("Helvetica", 10, "bold"), command=reset_form)
btn_reset.pack(side="right", fill="x", expand=True, padx=(40,0))


root.mainloop() 