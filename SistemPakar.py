import numpy as np
MB = 1
E = 'Extrovert'
I = 'Introvert'
S = 'Sensing'
N = 'Intuition'
T = 'Thinking'
F = 'Feeling'
J = 'Judging'
P = 'Perceiving'

# Membuka file .txt untuk dimasukan ke list berbeda
nama_file = 'soalMBTI.txt'
with open(nama_file, 'r') as file:
    #Inisialisasi delapan list untuk menyimpan data dari file
    soalE, soalI, soalS, soalN, soalT, soalF, soalJ, soalP = [], [], [], [], [], [], [], []
    current_list = soalE
    
    #Membaca setiap baris dalam file
    for line in file:
        # Menghapus karakter newline ('\n') dari akhir setiap baris
        line = line.strip()
        
        # Jika baris kosong, beralih ke list berikutnya
        if not line:
            current_list = None
        else:
            # Jika belum ada list yang aktif, aktifkan list berikutnya
            if current_list is None:
                for i, current in enumerate([soalE, soalI, soalS, soalN, soalT, soalF, soalJ, soalP]):
                    if not current:
                        current_list = current
                        break
            
            # Tambahkan baris ke list yang aktif
            current_list.append(line)

# Fungsi untuk menghitung CF_Rule berdasarkan nilai MD dalam tiap pertanyaan dari file .txt
def calculate_CF_Rule(MD):
    # Menghitung CF_Rule
    return MB - float(MD)

nama_file = 'bobotMD.txt'
with open(nama_file, 'r') as file:
    # Inisialisasi delapan list untuk menyimpan data dari file
    CF_Rule_E, CF_Rule_I, CF_Rule_S, CF_Rule_N, CF_Rule_T, CF_Rule_F, CF_Rule_J, CF_Rule_P = [], [], [], [], [], [], [], []
    current_list = CF_Rule_E

    # Membaca setiap baris dalam file
    for line in file:
        # Menghapus karakter newline ('\n') dari akhir setiap baris
        line = line.strip()

        # Jika baris kosong, beralih ke list berikutnya
        if not line:
            current_list = None
        else:
            # Jika belum ada list yang aktif, aktifkan list berikutnya
            if current_list is None:
                for i, current in enumerate([CF_Rule_E, CF_Rule_I, CF_Rule_S, CF_Rule_N, CF_Rule_T, CF_Rule_F, CF_Rule_J, CF_Rule_P]):
                    if not current:
                        current_list = current
                        break

            # Menghitung CF_Rule dan menambahkannya ke list yang aktif
            CF_Rule = calculate_CF_Rule(line)
            current_list.append(CF_Rule)

# Deklarasi variabel CF [E] atau Nilai CF dari suatu evidence (user)
CF_E_E, CF_E_I, CF_E_S, CF_E_N, CF_E_T, CF_E_F, CF_E_J, CF_E_P = [], [], [], [], [], [], [], []

def UI(soal, jawaban):
    pilihan = ["Sangat Tidak Setuju (A)", "Tidak Setuju (B)", "Sedikit Setuju (C)", "Setuju (D)", "Sangat Setuju (E)"]
    print(pilihan)  # Mencetak daftar pilihan jawaban kepada pengguna
    for i, soal in enumerate(soal):
        print(f"Soal {i + 1}: {soal}")  # Menampilkan soal kepada pengguna
        opsi = input("Masukkan pilihan (A/B/C/D/E): ")  # Meminta pengguna memasukkan pilihan jawaban
        opsi = opsi.upper()  # Mengonversi pilihan ke huruf besar (uppercase)
        if opsi == 'A':
            opsi = 0.1  # Mengubah pilihan 'A' menjadi nilai 0.1
        elif opsi == 'B':
            opsi = 0.2  # Mengubah pilihan 'B' menjadi nilai 0.2
        elif opsi == 'C':
            opsi = 0.3  # Mengubah pilihan 'C' menjadi nilai 0.3
        elif opsi == 'D':
            opsi = 0.5  # Mengubah pilihan 'D' menjadi nilai 0.5
        elif opsi == 'E':
            opsi = 0.8  # Mengubah pilihan 'E' menjadi nilai 0.8
        else:
            print("Opsi tidak valid")  # Cetak pesan jika pilihan tidak valid
            return # Berhenti jika nilai tidak valid
        jawaban.append(opsi)  # Menambahkan jawaban (dalam bentuk nilai numerik) ke dalam list jawaban

# Memunculkan soal dari tiap tipe soal kepribadian
UI(soalE, CF_E_E)
UI(soalI, CF_E_I)
UI(soalS, CF_E_S)
UI(soalN, CF_E_N)
UI(soalT, CF_E_T)
UI(soalF, CF_E_F)
UI(soalJ, CF_E_J)
UI(soalP, CF_E_P)

# Mencari CH[H, E] atau Nilai CF dari hipotesis yang dipengaruhi evidence
def cariCF_H_E(CF_E_n, CF_Rule_n):
    # CF [H, E] = CF [E] * CF [Rule]
    CF_H_E_n = np.array(CF_E_n) * np.array(CF_Rule_n)
    CF_H_E_n = CF_H_E_n.round(3)
    return CF_H_E_n

# Mencari nilai CF[H, E] dari tiap kepribadian
CF_H_E_E = cariCF_H_E(CF_E_E, CF_Rule_E)
CF_H_E_I = cariCF_H_E(CF_E_I, CF_Rule_I)
CF_H_E_S = cariCF_H_E(CF_E_S, CF_Rule_S)
CF_H_E_N = cariCF_H_E(CF_E_N, CF_Rule_N)
CF_H_E_T = cariCF_H_E(CF_E_T, CF_Rule_T)
CF_H_E_F = cariCF_H_E(CF_E_F, CF_Rule_F)
CF_H_E_J = cariCF_H_E(CF_E_J, CF_Rule_J)
CF_H_E_P = cariCF_H_E(CF_E_P, CF_Rule_P)

# Mencari CF[Comb] atau nilai CF dari hipotesis yang dipengaruhi evidence
def cariCF_Comb(CF_H_E_n):
    CF_Comb = CF_H_E_n[0]
    # CF [Comb] = CF [lama] + CF [baru] (1 - CF [lama])
    # Melakukan iterasi dari CF paling bawah (-1, karena element ke 0 dipakai CF [Comb]) sampai terakhir
    for i in range(1, len(CF_H_E_n)):
        CF_Comb = CF_Comb + (CF_H_E_n[i] * (1 - CF_Comb))
    return CF_Comb

# Mencari CF[Comb] dari tiap kepribadian 
CF_Comb_E = cariCF_Comb(CF_H_E_E)
CF_Comb_I = cariCF_Comb(CF_H_E_I)
CF_Comb_S = cariCF_Comb(CF_H_E_S)
CF_Comb_N = cariCF_Comb(CF_H_E_N)
CF_Comb_T = cariCF_Comb(CF_H_E_T)
CF_Comb_F = cariCF_Comb(CF_H_E_F)
CF_Comb_J = cariCF_Comb(CF_H_E_J)
CF_Comb_P = cariCF_Comb(CF_H_E_P)

# Mencari nilai kepribadian yang lebih dominan dalam satu dimensi
def perbandinganDimensi(CF_Comb_A, CF_Comb_B, Nama_A, Nama_B):
    # Mencari persentase dominasi
    Sum = CF_Comb_A + CF_Comb_B
    PersenA = (CF_Comb_A / Sum) * 100
    PersenB = (CF_Comb_B / Sum) * 100

    # Melakukan perbandingan dominasi dari 2 kepribadian
    if CF_Comb_A >= CF_Comb_B:
        return Nama_A, PersenA
    else:
        return Nama_B, PersenB

# Menyimpan kepribadian mana yang lebih dominan serta persentasenya dari satu dimensi
Dimensi_Energi, Persen_Energi = perbandinganDimensi(CF_Comb_E, CF_Comb_I, E, I)
Dimensi_Informasi, Persen_Informasi = perbandinganDimensi(CF_Comb_S, CF_Comb_N, S, N)
Dimensi_Keputusan , Persen_Keputusan  = perbandinganDimensi(CF_Comb_T, CF_Comb_F, T, F)
Dimensi_Lifestyle, Persen_Lifestyle = perbandinganDimensi(CF_Comb_J, CF_Comb_P, J, P)

def Kepribadian(Dim_Energi, Dim_Informasi, Dim_Keputusan, Dim_Lifestyle, nama_file):
    # Dictionary untuk mencari deskripsi yang sesuai dari baris pada file menggunakan kode kepribadian
    Tipe_Kepribadian = {
        'ISTJ - The Duty Fulfiller' : 0,
        'ISTP - The Mechanic' : 1,
        'ISFJ - The Nurturer' : 2,
        'ISFP - The Artist' : 3,
        'INFJ - The Protector' : 4,
        'INFP - The Idealist' : 5,
        'INTJ - The Scientist' : 6,
        'INTP - The Thinker' : 7,
        'ESTP - The Doer' : 8,
        'ESTJ - The Guardian' : 9,
        'ESFP - The Performer' : 10,
        'ESFJ - The Caregiver' : 11,
        'ENFP - The Inspirer' : 12,
        'ENFJ - The Giver' : 13,
        'ENTP - The Visionary' : 14,
        'ENTJ - The Executive' : 15
    }
    
    # Mencari kombinasi tipe kepribadian yang cocok dari input
    Kode_Tipe_Kepribadian = None
    if (Dim_Energi == 'Extrovert'):
        if (Dim_Informasi == 'Sensing'):
            if (Dim_Keputusan == 'Thinking'):
                if (Dim_Lifestyle == 'Judging'):
                    Kode_Tipe_Kepribadian = 'ESTJ - The Guardian'
                elif (Dim_Lifestyle == 'Perceiving'):
                    Kode_Tipe_Kepribadian = 'ESTP - The Doer'
            elif (Dim_Keputusan == 'Feeling'):
                if (Dim_Lifestyle == 'Judging'):
                    Kode_Tipe_Kepribadian = 'ESFJ - The Caregiver'
                elif (Dim_Lifestyle == 'Perceiving'):
                    Kode_Tipe_Kepribadian = 'ESFP - The Performer'
        elif (Dim_Informasi == 'Intuition'):
            if (Dim_Keputusan == 'Thinking'):
                if (Dim_Lifestyle == 'Judging'):
                    Kode_Tipe_Kepribadian = 'ENTJ - The Executive'
                elif (Dim_Lifestyle == 'Perceiving'):
                    Kode_Tipe_Kepribadian = 'ENTP - The Visionary'
            elif (Dim_Keputusan == 'Feeling'):
                if (Dim_Lifestyle == 'Judging'):
                    Kode_Tipe_Kepribadian = 'ENFJ - The Giver'
                elif (Dim_Lifestyle == 'Perceiving'):
                    Kode_Tipe_Kepribadian = 'ENFP - The Inspirer'
    elif (Dim_Energi == 'Introvert'):
        if (Dim_Informasi == 'Sensing'):
            if (Dim_Keputusan == 'Thinking'):
                if (Dim_Lifestyle == 'Judging'):
                    Kode_Tipe_Kepribadian = 'ISTJ - The Duty Fulfiller'
                elif (Dim_Lifestyle == 'Perceiving'):
                    Kode_Tipe_Kepribadian = 'ISTP - The Mechanic'
            elif (Dim_Keputusan == 'Feeling'):
                if (Dim_Lifestyle == 'Judging'):
                    Kode_Tipe_Kepribadian = 'ISFJ - The Nurturer'
                elif (Dim_Lifestyle == 'Perceiving'):
                    Kode_Tipe_Kepribadian = 'ISFP - The Artist'
        elif (Dim_Informasi == 'Intuition'):
            if (Dim_Keputusan == 'Thinking'):
                if (Dim_Lifestyle == 'Judging'):
                    Kode_Tipe_Kepribadian = 'INTJ - The Scientist'
                elif (Dim_Lifestyle == 'Perceiving'):
                    Kode_Tipe_Kepribadian = 'INTP - The Thinker'
            elif (Dim_Keputusan == 'Feeling'):
                if (Dim_Lifestyle == 'Judging'):
                    Kode_Tipe_Kepribadian = 'INFJ - The Protector'
                elif (Dim_Lifestyle == 'Perceiving'):
                    Kode_Tipe_Kepribadian = 'INFP - The Idealist'

    # Cek jika kode tipe personality ada
    if Kode_Tipe_Kepribadian is not None:
        try:
            # Buka file dan membaca deskripsi dari file
            with open(nama_file, 'r') as file:
                descriptions = file.read().splitlines()
                description = descriptions[Tipe_Kepribadian[Kode_Tipe_Kepribadian]]
                print(f'{Kode_Tipe_Kepribadian}: {description}')
        except FileNotFoundError:
            print(f'File tidak ditemukan: {nama_file}')
        return Kode_Tipe_Kepribadian, description
    else:
        print('Kode kepribadian invalid')

# Example usage
hasilTes, Desc = Kepribadian(Dimensi_Energi, Dimensi_Informasi, Dimensi_Keputusan, Dimensi_Lifestyle, 'deskripsiKepribadian.txt')

def hasilMBTI(Dim_Energi, Dim_Informasi, Dim_Keputusan, Dim_Lifestyle, Per_Energi, Per_Informasi, Per_Keputusan, Per_Lifestyle, hasil, Deskripsi, nama_file):
    with open(nama_file, 'a') as file:
        file.write('Tipe kepribadian: ' + str(hasil) + '\n')
        file.write('Deskripsi Kepribadian: ' + str(Deskripsi) + '\n')
        file.write(str(Dim_Energi) + ' persentase: ' + str(Per_Energi) + '\n')
        file.write(str(Dim_Informasi) + ' persentase: ' + str(Per_Informasi) + '\n')
        file.write(str(Dim_Keputusan) + ' persentase: ' + str(Per_Keputusan) + '\n')
        file.write(str(Dim_Lifestyle) + ' persentase: ' + str(Per_Lifestyle) + '\n')
        file.write('\n')

hasilMBTI(Dimensi_Energi, Dimensi_Informasi, Dimensi_Keputusan, Dimensi_Lifestyle, Persen_Energi, Persen_Informasi, Persen_Keputusan, Persen_Lifestyle, hasilTes, Desc, 'hasilTes.txt')