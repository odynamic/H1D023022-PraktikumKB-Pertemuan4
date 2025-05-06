from tkinter import *
from pyswip import Prolog

prolog = Prolog()
prolog.consult("pakar_anak.pl")

# Gejala dan Pertanyaan
gejala_pertanyaan = {
    'tidak_merespons_saat_dipanggil': "Apakah anak tidak merespons saat dipanggil?",
    'menghindari_kontak_mata': "Apakah anak menghindari kontak mata?",
    'gerakan_berulang': "Apakah anak melakukan gerakan berulang seperti flapping atau rocking?",
    'rutinitas_sangat_kaku': "Apakah anak memiliki rutinitas yang sangat kaku?",
    'terlambat_bicara': "Apakah anak terlambat dalam berbicara?",
    'tidak_menunjukkan_ekspresi_wajah': "Apakah anak tidak menunjukkan ekspresi wajah?",
    'kesulitan_berbicara_atau_membentuk_kalimat': "Apakah anak kesulitan berbicara atau membentuk kalimat?",
    'sulit_memahami_perintah_sederhana': "Apakah anak sulit memahami perintah sederhana?",
    'gagap_atau_terbata_bata': "Apakah anak gagap atau terbata-bata?",
    'sulit_fokus': "Apakah anak sulit fokus?",
    'hiperaktif': "Apakah anak hiperaktif?",
    'impulsif': "Apakah anak impulsif?",
    'sering_interupsi_saat_orang_bicara': "Apakah anak sering menginterupsi saat orang berbicara?",
    'sering_kehilangan_barang': "Apakah anak sering kehilangan barang?",
    'mudah_terdistraksi': "Apakah anak mudah terdistraksi?",
    'kesulitan_membaca': "Apakah anak kesulitan membaca?",
    'membolak_balik_huruf': "Apakah anak membolak-balik huruf?",
    'kesulitan_mengeja': "Apakah anak kesulitan mengeja?",
    'lambat_memahami_bacaan': "Apakah anak lambat memahami bacaan?",
    'gerakan_tubuh_tidak_terkoordinasi': "Apakah gerakan tubuh anak tidak terkoordinasi?",
    'sering_menjatuhkan_benda': "Apakah anak sering menjatuhkan benda?",
    'susah_mengikat_tali_sepatu_atau_menulis': "Apakah anak susah mengikat tali sepatu atau menulis?",
    'sensitif_terhadap_suara_cahaya_atau_sentuhan': "Apakah anak sensitif terhadap suara, cahaya, atau sentuhan?",
    'tidak_nyaman_dengan_pakaian_tertentu': "Apakah anak tidak nyaman dengan pakaian tertentu?",
    'menolak_disentuh': "Apakah anak menolak disentuh?"
}

# Pengaturan GUI
root = Tk()
root.title("Sistem Pakar Diagnosis Gangguan Perkembangan Anak")
root.geometry("800x600")

Label(root, text="Checklist Gejala yang Dialami Anak:", font=("Helvetica", 12, "bold")).pack(pady=(10, 5))

canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=(10, 0))
scrollbar.pack(side="right", fill="y")

checkbox_vars = {}
for gejala, pertanyaan in gejala_pertanyaan.items():
    var = BooleanVar()
    checkbox = Checkbutton(scrollable_frame, text=pertanyaan, variable=var, wraplength=600, justify="left", font=("Helvetica", 9))
    checkbox.pack(anchor="w", padx=5, pady=1)
    checkbox_vars[gejala] = var

# Frame Output
frame_hasil = Frame(root)
frame_hasil.pack(pady=10, padx=20, fill="both", expand=True)

Label(frame_hasil, text="Kemungkinan Diagnosis:", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(10, 0))
diagnosis_label = Label(frame_hasil, text="", font=("Helvetica", 10), wraplength=600, justify="left", fg="black")
diagnosis_label.pack(anchor="w", pady=(5, 10))

Label(frame_hasil, text="Saran:", font=("Helvetica", 12, "bold")).pack(anchor="w")
saran_label = Label(frame_hasil, text="", font=("Helvetica", 10), wraplength=600, justify="left", fg="black")
saran_label.pack(anchor="w", pady=(5, 10))

# Tombol
frame_button = Frame(root)
frame_button.pack(pady=10)

def diagnosa():
    selected_gejala = [gejala for gejala, var in checkbox_vars.items() if var.get()]
    gejala_list = "[" + ",".join(selected_gejala) + "]"
    hasil = list(prolog.query(f"diagnosa({gejala_list}, Penyakit)"))

    if hasil:
        penyakit_terdiagnosa = sorted(set(x["Penyakit"] for x in hasil))
        formatted = []
        saran_text = ""

        for penyakit in penyakit_terdiagnosa:
            nama = list(prolog.query(f"nama_penyakit({penyakit}, Nama)"))
            if nama:
                formatted.append(nama[0]["Nama"])
            else:
                formatted.append(penyakit.replace("_", " ").capitalize())

            saran_hasil = list(prolog.query(f"dapatkan_saran('{penyakit}', Saran)"))
            if saran_hasil:
                saran_text += f"— {saran_hasil[0]['Saran']}\n"

        diagnosis_label.config(text=", ".join(formatted))
        saran_label.config(text=saran_text)
    else:
        diagnosis_label.config(text="Tidak ditemukan diagnosis berdasarkan gejala yang dipilih.")
        saran_label.config(text="")

def reset():
    for var in checkbox_vars.values():
        var.set(False)
    diagnosis_label.config(text="")
    saran_label.config(text="")

Button(frame_button, text="Diagnosa", command=diagnosa, width=15).pack(side=LEFT, padx=10)
Button(frame_button, text="Reset", command=reset, width=15).pack(side=LEFT, padx=10)

root.mainloop()
