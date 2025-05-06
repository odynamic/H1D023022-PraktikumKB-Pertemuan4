% Fakta penyakit
penyakit(autisme).
penyakit(adhd).
penyakit(disleksia).
penyakit(gangguan_bahasa).
penyakit(gangguan_motorik).
penyakit(gangguan_sensorik).

% Nama penyakit untuk tampilan yang lebih user-friendly
nama_penyakit(autisme, 'Autisme').
nama_penyakit(adhd, 'Attention Deficit Hyperactivity Disorder (ADHD)').
nama_penyakit(disleksia, 'Disleksia').
nama_penyakit(gangguan_bahasa, 'Gangguan Bahasa').
nama_penyakit(gangguan_motorik, 'Gangguan Motorik').
nama_penyakit(gangguan_sensorik, 'Gangguan Sensorik').

% Gejala untuk masing-masing penyakit
gejala(tidak_merespons_saat_dipanggil, autisme).
gejala(menghindari_kontak_mata, autisme).
gejala(gerakan_berulang, autisme).
gejala(rutinitas_sangat_kaku, autisme).
gejala(terlambat_bicara, autisme).
gejala(tidak_menunjukkan_ekspresi_wajah, autisme).

gejala(terlambat_bicara, gangguan_bahasa).
gejala(kesulitan_berbicara_atau_membentuk_kalimat, gangguan_bahasa).
gejala(sulit_memahami_perintah_sederhana, gangguan_bahasa).
gejala(gagap_atau_terbata_bata, gangguan_bahasa).

gejala(sulit_fokus, adhd).
gejala(hiperaktif, adhd).
gejala(impulsif, adhd).
gejala(sering_interupsi_saat_orang_bicara, adhd).
gejala(sering_kehilangan_barang, adhd).
gejala(mudah_terdistraksi, adhd).

gejala(kesulitan_membaca, disleksia).
gejala(membolak_balik_huruf, disleksia).
gejala(kesulitan_mengeja, disleksia).
gejala(lambat_memahami_bacaan, disleksia).

gejala(gerakan_tubuh_tidak_terkoordinasi, gangguan_motorik).
gejala(sering_menjatuhkan_benda, gangguan_motorik).
gejala(susah_mengikat_tali_sepatu_atau_menulis, gangguan_motorik).

gejala(sensitif_terhadap_suara_cahaya_atau_sentuhan, gangguan_sensorik).
gejala(tidak_nyaman_dengan_pakaian_tertentu, gangguan_sensorik).
gejala(menolak_disentuh, gangguan_sensorik).

% Fakta saran untuk masing-masing penyakit
saran(autisme, 'Anak mungkin membutuhkan intervensi terapi perilaku, terapi bicara, dan pengawasan medis.').
saran(adhd, 'Anak mungkin membutuhkan pengelolaan perilaku dan terapi pendidikan untuk membantu meningkatkan fokus dan pengendalian diri.').
saran(disleksia, 'Anak mungkin memerlukan pendidikan yang lebih terstruktur dan dukungan khusus dalam membaca dan menulis.').
saran(gangguan_bahasa, 'Anak sebaiknya mendapatkan terapi bicara dan dukungan untuk pengembangan kemampuan berbahasa.').
saran(gangguan_motorik, 'Anak bisa mendapatkan terapi fisik dan latihan untuk membantu koordinasi motorik.').
saran(gangguan_sensorik, 'Anak mungkin perlu penyesuaian lingkungan untuk mengurangi sensitivitas terhadap rangsangan sensorik.').

% Aturan diagnosa berdasarkan ≥ 50% kecocokan gejala
diagnosa(GejalaList, Penyakit) :-
    penyakit(Penyakit),
    findall(Gejala, gejala(Gejala, Penyakit), GejalaPenyakit),
    intersection(GejalaList, GejalaPenyakit, GejalaYangCocok),
    length(GejalaYangCocok, JumlahCocok),
    length(GejalaPenyakit, JumlahTotal),
    JumlahTotal > 0,
    Persentase is (JumlahCocok / JumlahTotal) * 100,
    Persentase >= 50.

% Aturan mendapatkan saran
dapatkan_saran(Penyakit, Saran) :-
    saran(Penyakit, Saran), !.
dapatkan_saran(_, 'Belum ada saran spesifik untuk diagnosis ini.').
