# File : TB_2572020_2572021.py
# Penulis : Jason Manuel Simadibrata, Nicolas Elnathan
# Tujuan Program : Sistem Laundry

## Definisi Prosedur cetak_baris(no_str, nama_str, kat_str, in_str, out_str, tot_str)
# Kamus lokal  
# no_str, nama_str, kat_str, in_str, out_str, tot_str : parameter berisi data kolom tabel (string) 
# kolom : array penampung seluruh data kolom (array of string) 
# lebar : array penampung spesifikasi lebar masing-masing kolom (array of int) 
# i : var. counter untuk indeks kolom (int) 
def cetak_baris(no_str, nama_str, kat_str, in_str, out_str, tot_str):
    kolom = [no_str, nama_str, kat_str, in_str, out_str, tot_str]
    lebar = [6, 17, 12, 13, 13, 15]
    for i in range(0,6,1):
        cetak_rata_kiri(kolom[i], lebar[i])
    print()

## Definisi Fungsi adalah_angka(s)
# Kamus lokal  
# s : parameter input berupa teks yang diperiksa (string) 
# valid : var. penanda apakah seluruh karakter berupa angka (boolean) 
# c : var. penampung karakter saat iterasi (string) 
def adalah_angka(s):
    if(s==""):
        return False
    valid = True
    for c in s:
        if(c!="0" and c!="1" and c!="2" and c!="3" and c!="4" and c!="5" and c!="6" and c!="7" and c!="8" and c!="9"):
            valid = False
    return valid
    
## Definisi Fungsi hitung_panjang(kata)
# Kamus lokal  
# kata : parameter input berupa teks (string) 
# n : var. counter untuk menghitung jumlah karakter (int) 
# c : var. penampung karakter saat iterasi (string) 
def hitung_panjang(kata):
    n = 0
    for c in kata:
        n += 1
    return n

## Definisi Fungsi cetak_rata_kiri(kata, lebar)
# Kamus lokal  
# kata : parameter input berupa teks yang akan dicetak (string) 
# lebar : parameter input untuk batas lebar kolom (int) 
# p : var. panjang karakter dari teks kata (int) 
# i : var. counter untuk mencetak spasi sisa (int) 
def cetak_rata_kiri(kata, lebar):
    p = hitung_panjang(kata)
    print(kata, end="")
    for i in range(0,lebar-p,1):
        print(" ", end="")

## Definisi Fungsi adalah_desimal(s)
# Kamus lokal  
# s : parameter input berupa teks yang diperiksa (string) 
# valid : var. penanda apakah string merupakan desimal valid (boolean) 
# titik : var. counter jumlah karakter titik desimal (int) 
# angka : var. counter jumlah karakter angka (int) 
# c : var. penampung karakter saat iterasi (string) 
def adalah_desimal(s):
    if(s==""):
        return False
    valid = True
    titik = 0
    angka = 0
    for c in s:
        if(c=="."):
            titik += 1
        elif(c!="0" and c!="1" and c!="2" and c!="3" and c!="4" and c!="5" and c!="6" and c!="7" and c!="8" and c!="9"):
            valid = False
        else:
            angka += 1
    if(titik>1 or angka==0):
        valid = False
    return valid

## Definisi Fungsi pilih_menu()
# Kamus lokal  
# pil_in : var. penampung input pilihan menu utama dari user (string) 
def pilih_menu():
    print()
    print("=== Selamat Datang di Laundry ===")
    print("1. Nyuci Baru")
    print("2. Print Nota")
    print("3. Cek Pemasukan Harian")
    print("4. Cek Pemasukan Bulanan")
    print("5. Cari Pelanggan (Searching)")
    print("6. Cek Histori (Sorting)")
    print("7. Keluar / Tutup")
    pil_in = input("Silahkan pilih, pilihan di atas : ")
    if(pil_in=="1" or pil_in=="2" or pil_in=="3" or pil_in=="4" or pil_in=="5" or pil_in=="6" or pil_in=="7"):
        return int(pil_in)
    else:
        return -1

## Definisi Prosedur nyuci()
# Kamus lokal  
# kat_in, dur_in, thn_in, bln_in, hr_in : var. penampung input teks tgl/durasi/kategori (string) 
# berat_in, pcs_in : var. penampung input nominal berat atau pcs (string) 
# kat, dur, thn, bln, hr, pcs, hrg : var. data numerik bulat transaksi (int) 
# berat : var. nilai berat pakaian dalam kg (float) 
# tot : var. kalkulasi total biaya laundry (float) 
# hr_out, bln_out, thn_out : var. penampung estimasi waktu selesai (int) 
# hr_per_bln : array batas hari maksimum tiap bulan (array of int) 
def nyuci():
    global jmlh
    print()
    print("=== Input Cucian Baru ===")
    print("--------------------------------------------------")
    print("              RINCIAN TARIF LAUNDRY               ")
    print("--------------------------------------------------")
    print("1. Paket Kiloan (per kg):")
    print("\t- 1 Hari (Express)\t: Rp15000")
    print("\t- 2 Hari (Sedang)\t: Rp10000")
    print("\t- 3 Hari (Biasa)\t: Rp5000")
    print("2. Paket Satuan (per pcs):")
    print("\t- 1 Hari (Express)\t: Rp10000")
    print("\t- 2 Hari (Sedang)\t: Rp7500")
    print("\t- 3 Hari (Biasa)\t: Rp5000")
    print("--------------------------------------------------")
    nama[jmlh] = ""
    while(nama[jmlh]==""):
        nama[jmlh] = input("Masukan nama\t\t\t\t: ")
        if(nama[jmlh]==""):
            print("Nama tidak boleh kosong!")
    kat_in = ""
    while(kat_in!="1" and kat_in!="2"):
        kat_in = input("Masukan kategori (1=kiloan, 2=satuan)\t: ")
        if(kat_in!="1" and kat_in!="2"):
            print("Kategori tidak valid! Pilih 1 atau 2.")
    kat = int(kat_in)
    dur_in = ""
    while(dur_in!="1" and dur_in!="2" and dur_in!="3"):
        dur_in = input("Lama pengerjaan (1-3 hari)\t\t: ")
        if(dur_in!="1" and dur_in!="2" and dur_in!="3"):
            print("Durasi tidak valid! Masukkan angka antara 1 sampai 3.")
    dur = int(dur_in)
    thn = 0
    while(thn<1990 or thn>2026):
        thn_in = ""
        while(adalah_angka(thn_in)==False):
            thn_in = input("Tahun masuk (yyyy)\t\t\t: ")
            if(adalah_angka(thn_in)==False):
                print("Tahun harus berupa angka bulat!")
        thn = int(thn_in)
        if(thn<1990 or thn>2026):
            print("Tahun harus di antara 1990 dan 2026!")
    bln_in = ""
    while(True):
        bln_in = input("Bulan masuk (mm)\t\t\t: ")
        if(adalah_angka(bln_in)==True):
            bln = int(bln_in)
            if(bln>=1 and bln<=12):
                break
        print("Bulan tidak valid! Masukkan angka 1 sampai 12.")
    hr_per_bln = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(thn%4==0):
        hr_per_bln[2] = 29
    hr_in = ""
    while(True):
        hr_in = input("Tgl masuk (dd)\t\t\t\t: ")
        if(adalah_angka(hr_in)==True):
            hr = int(hr_in)
            if(hr>=1 and hr<=hr_per_bln[bln]):
                break
        print(f"Tanggal tidak valid untuk bulan {bln}! Masukkan angka 1 sampai {hr_per_bln[bln]}.")
    if(kat==1):
        berat = 0.0
        while(berat<=0.0):
            berat_in = ""
            while(adalah_desimal(berat_in)==False):
                berat_in = input("Berat (kg)\t\t\t\t: ")
                if(adalah_desimal(berat_in)==False):
                    print("Berat harus berupa angka desimal atau bulat (contoh: 2.5 atau 3)!")
            berat = float(berat_in)
            if(berat<=0.0):
                print("Berat harus lebih besar dari 0!")
        if(dur==1):
            hrg = 15000
        elif(dur==2):
            hrg = 10000
        else:
            hrg = 5000
        tot = berat * hrg
        kategori[jmlh] = "Kiloan"
    else:
        pcs = 0
        while(pcs<=0):
            pcs_in = ""
            while(adalah_angka(pcs_in)==False):
                pcs_in = input("Jumlah (pcs)\t\t\t\t: ")
                if(adalah_angka(pcs_in)==False):
                    print("Jumlah pcs harus berupa angka bulat!")
            pcs = int(pcs_in)
            if(pcs<=0):
                print("Jumlah pcs harus lebih besar dari 0!")
        if(dur==1):
            hrg = 10000
        elif(dur==2):
            hrg = 7500
        else:
            hrg = 5000
        tot = pcs * hrg
        kategori[jmlh] = "Satuan"
    hr_out, bln_out, thn_out = hitung_selesai(hr, bln, thn, dur)
    tot_harga[jmlh] = tot
    lama[jmlh] = dur
    tgl_in[jmlh] = [hr, bln, thn]
    tgl_out[jmlh] = [hr_out, bln_out, thn_out]
    print()
    print(f" Data disimpan. Total harga: Rp{tot}")
    print("=================================")
    jmlh += 1

## Definisi Fungsi hitung_selesai(hr_in, bln_in, thn_in, dur_hr)
# Kamus lokal  
# hr_in, bln_in, thn_in, dur_hr : parameter input waktu awal masuk (int) 
# hr_per_bln : array batas hari maksimum tiap bulan (array of int) 
# hr_out, bln_out, thn_out : var. penampung kalkulasi waktu selesai (int) 
def hitung_selesai(hr_in, bln_in, thn_in, dur_hr):
    hr_per_bln = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(thn_in%4==0):
        hr_per_bln[2] = 29
    hr_out = hr_in + dur_hr
    bln_out = bln_in
    thn_out = thn_in
    while(hr_out>hr_per_bln[bln_out]):
        hr_out -= hr_per_bln[bln_out]
        bln_out += 1
        if(bln_out>12):
            bln_out = 1
            thn_out += 1
            if(thn_out%4==0):
                hr_per_bln[2] = 29
            else:
                hr_per_bln[2] = 28
    return hr_out, bln_out, thn_out

## Definisi Prosedur nota()
# Kamus lokal  
# i : var. counter indeks perulangan pelanggan (int) 
# idx_in : var. penampung input indeks pelanggan dari user (string) 
# idx : var. indeks numerik pelanggan terpilih (int) 
def nota():
    if(jmlh==0):
        print()
        print("Belum ada transaksi terdaftar!")
        return
    print()
    print("=== Daftar Pelanggan ===")
    for i in range(0,jmlh,1):
        print(f"{i}. {nama[i]}")
    idx_in = ""
    while(adalah_angka(idx_in)==False):
        idx_in = input("Pilih nomor pelanggan untuk cetak nota: ")
        if(adalah_angka(idx_in)==False):
            print("Indeks pelanggan harus berupa angka bulat!")
    idx = int(idx_in)
    if(idx>=0 and idx<jmlh):
        print()
        print("================== NOTA LAUNDRY ==================")
        print(f"Nama Pelanggan\t: {nama[idx]}")
        print(f"Kategori Paket\t: {kategori[idx]}")
        print(f"Lama Pengerjaan\t: {lama[idx]} hari")
        print(f"Tanggal Masuk\t: {tgl_in[idx][0]}/{tgl_in[idx][1]}/{tgl_in[idx][2]}")
        print(f"Tanggal Selesai\t: {tgl_out[idx][0]}/{tgl_out[idx][1]}/{tgl_out[idx][2]}")
        print(f"Total Bayar\t: Rp{tot_harga[idx]}")
        print("==================================================")
    else:
        print("Pelanggan tidak ditemukan.")

## Definisi Prosedur harian()
# Kamus lokal  
# thn_in, bln_in, hr_in : var. penampung input teks tanggal/bulan/tahun (string) 
# thn, bln, hr, i : var. tanggal numerik dan counter indeks perulangan (int) 
# hr_per_bln : array batas hari maksimum tiap bulan (array of int) 
# tot_hr : var. akumulasi jumlah pendapatan harian (float) 
# found : var. penanda apakah data pada tanggal tersebut ada (boolean) 
def harian():
    if(jmlh==0):
        print()
        print("Belum ada transaksi terdaftar!")
        return
    print()
    print("=== Cek Pemasukan Harian ===")
    thn_in = ""
    while(adalah_angka(thn_in)==False):
        thn_in = input("Masukan tahun (yyyy)\t\t\t: ")
        if(adalah_angka(thn_in)==False):
            print("Tahun harus berupa angka bulat!")
    thn = int(thn_in)
    bln_in = ""
    while(True):
        bln_in = input("Masukan bulan (mm)\t\t\t: ")
        if(adalah_angka(bln_in)==True):
            bln = int(bln_in)
            if(bln>=1 and bln<=12):
                break
        print("Bulan tidak valid! Masukkan angka 1 sampai 12.")
    hr_per_bln = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(thn%4==0):
        hr_per_bln[2] = 29
    hr_in = ""
    while(True):
        hr_in = input("Masukan tanggal (dd)\t\t\t: ")
        if(adalah_angka(hr_in)==True):
            hr = int(hr_in)
            if(hr>=1 and hr<=hr_per_bln[bln]):
                break
        print(f"Tanggal tidak valid untuk bulan {bln}! Masukkan angka 1 sampai {hr_per_bln[bln]}.")
    tot_hr = 0
    found = False
    for i in range(0,jmlh,1):
        if(tgl_in[i][0]==hr and tgl_in[i][1]==bln and tgl_in[i][2]==thn):
            tot_hr += tot_harga[i]
            found = True
    if(found==True):
        print()
        print(f" Total pemasukan pada tanggal {hr}/{bln}/{thn} adalah: Rp{tot_hr}")
    else:
        print()
        print(" Tidak ada transaksi pada tanggal tersebut.")

## Definisi Prosedur bulanan()
# Kamus lokal  
# tar_thn_in, tar_in : var. penampung input teks target bulan/tahun (string) 
# tar_thn, tar, i : var. target waktu numerik dan counter indeks perulangan (int) 
# tot_bln : var. akumulasi jumlah pendapatan bulanan (float) 
# found : var. penanda apakah data pada bulan tersebut ada (boolean) 
def bulanan():
    if(jmlh==0):
        print()
        print("Belum ada transaksi terdaftar!")
        return
    print()
    print("=== Cek Pemasukan Bulanan ===")
    tar_thn_in = ""
    while(adalah_angka(tar_thn_in)==False):
        tar_thn_in = input("Masukan tahun (yyyy)\t\t\t: ")
        if(adalah_angka(tar_thn_in)==False):
            print("Tahun harus berupa angka bulat!")
    tar_thn = int(tar_thn_in)
    tar_in = ""
    while(True):
        tar_in = input("Masukan bulan (1-12)\t\t\t: ")
        if(adalah_angka(tar_in)==True):
            tar = int(tar_in)
            if(tar>=1 and tar<=12):
                break
        print("Bulan tidak valid! Masukkan angka 1 sampai 12.")
    tot_bln = 0
    found = False
    for i in range(0,jmlh,1):
        if(tgl_in[i][1]==tar and tgl_in[i][2]==tar_thn):
            tot_bln += tot_harga[i]
            found = True
    if(found==True):
        print()
        print(f" Total pemasukan bulan {tar}/{tar_thn}: Rp{tot_bln}")
    else:
        print()
        print(f" Tidak ada transaksi pada bulan {tar}/{tar_thn}.")

## Definisi Prosedur cari_pelanggan()
# Kamus lokal  
# cari : var. penampung nama pelanggan yang dicari dari user (string) 
# found : var. penanda apakah data pelanggan berhasil dicari (boolean) 
# i : var. counter indeks perulangan pelanggan (int)  
def cari_pelanggan():
    if(jmlh == 0):
        print()
        print("Belum ada data pelanggan untuk dicari!")
        return
    print()
    print("=== Cari Pelanggan (Exact Match) ===")
    cari = input("Masukkan nama pelanggan yang dicari: ")
    found = False
    for i in range(0, jmlh, 1):
        if(cari == nama[i]):
            print()
            print(f"[Data Ditemukan di Indeks ke-{i}]")
            print(f"Nama Pelanggan  : {nama[i]}")
            print(f"Kategori Paket  : {kategori[i]}")
            print(f"Lama Pengerjaan : {lama[i]} hari")
            print(f"Tanggal Masuk   : {tgl_in[i][0]}/{tgl_in[i][1]}/{tgl_in[i][2]}")
            print(f"Tanggal Selesai : {tgl_out[i][0]}/{tgl_out[i][1]}/{tgl_out[i][2]}")
            print(f"Total Bayar     : Rp{tot_harga[i]}")
            print("-" * 30)
            found = True
    if(found == False):
        print()
        print(f" Pelanggan dengan nama '{cari}' tidak ditemukan.")

## Definisi Prosedur histori()
# Kamus lokal  
# i, j : var. counter untuk indeks perulangan luar dan dalam sorting (int) 
# kond_thn, kond_bln, kond_hr : var. penanda perbandingan tanggal (boolean) 
# no_s, tgl_m_s, tgl_s_s, tot_s : var. teks terformat untuk cetak kolom tabel (string) 
# temp : var. penampung sementara untuk penukaran data (swap) 
def histori():
    if(jmlh==0):
        print()
        print("Belum ada transaksi dalam histori!")
        return
    for i in range(0,jmlh,1):
        for j in range(0,jmlh-i-1,1):
            kond_thn = (tgl_in[j][2]>tgl_in[j+1][2])
            kond_bln = (tgl_in[j][2]==tgl_in[j+1][2] and tgl_in[j][1]>tgl_in[j+1][1])
            kond_hr = (tgl_in[j][2]==tgl_in[j+1][2] and tgl_in[j][1]==tgl_in[j+1][1] and tgl_in[j][0]>tgl_in[j+1][0])
            if(kond_thn==True or kond_bln==True or kond_hr==True):
                temp = nama[j]
                nama[j] = nama[j+1]
                nama[j+1] = temp
                temp = kategori[j]
                kategori[j] = kategori[j+1]
                kategori[j+1] = temp
                temp = lama[j]
                lama[j] = lama[j+1]
                lama[j+1] = temp
                temp = tot_harga[j]
                tot_harga[j] = tot_harga[j+1]
                tot_harga[j+1] = temp
                temp = tgl_in[j]
                tgl_in[j] = tgl_in[j+1]
                tgl_in[j+1] = temp
                temp = tgl_out[j]
                tgl_out[j] = tgl_out[j+1]
                tgl_out[j+1] = temp
    print()
    print("================================== HISTORI TRANSAKSI ==================================")
    cetak_baris("No.", "Nama", "Kategori", "Tgl Masuk", "Tgl Selesai", "Total Bayar")
    print("---------------------------------------------------------------------------------------")
    for i in range(0,jmlh,1):
        no_s = str(i+1)+"."
        tgl_m_s = str(tgl_in[i][0])+"/"+str(tgl_in[i][1])+"/"+str(tgl_in[i][2])
        tgl_s_s = str(tgl_out[i][0])+"/"+str(tgl_out[i][1])+"/"+str(tgl_out[i][2])
        tot_s = "Rp"+str(tot_harga[i])
        cetak_baris(no_s, nama[i], kategori[i], tgl_m_s, tgl_s_s, tot_s)
    print("=======================================================================================")

## Definisi Prosedur reset_data()
def reset_data():
    global nama, kategori, lama, tot_harga, tgl_in, tgl_out, jmlh
    nama = [None] * max_data
    kategori = [None] * max_data
    lama = [None] * max_data
    tot_harga = [None] * max_data
    tgl_in = [None] * max_data
    tgl_out = [None] * max_data
    jmlh = 0
    print()
    print(" Semua data transaksi telah di-reset!")
    print("=================================")

## Definisi Prosedur beres()
def beres():
    print()
    print("Sistem ditutup, terima kasih!")

## Definisi Fungsi login()
# Kamus lokal  
# username, password : var. kredensial pembanding statis admin (string) 
# ask_u, ask_p : var. penampung teks masukan admin (string) 
# cb : var. penampung jawaban konfirmasi ulang masuk sistem (string) 
def login():
    username = "admin"
    password = "admin"
    while(True):
        print()
        print("=================================")
        print("          SISTEM LOGIN           ")
        print("=================================")
        ask_u = input("Masukan Username : ")
        ask_p = input("Masukan password : ")
        if(ask_u==username and ask_p==password):
            print()
            print("=================================")
            print("         Login Berhasil!         ")
            print("=================================")
            return True
        else:
            print()
            print("=================================")
            print("  Username atau Password salah!  ")
            print("=================================")
            cb = ""
            while(cb!="ya" and cb!="Ya" and cb!="yA" and cb!="YA" and cb!="tidak" and cb!="Tidak" and cb!="tiDak" and cb!="tidAk" and cb!="TIdak" and cb!="TIDAK"):
                cb = input("Ulang (ya/tidak)? ")
                if(cb!="ya" and cb!="Ya" and cb!="yA" and cb!="YA" and cb!="tidak" and cb!="Tidak" and cb!="tiDak" and cb!="tidAk" and cb!="TIdak" and cb!="TIDAK"):
                    print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
            if(cb=="tidak" or cb=="Tidak" or cb=="tiDak" or cb=="tidAk" or cb=="TIdak" or cb=="TIDAK"):
                return False

## Program Utama ##
# Kamus data
# sis_on : var. status keaktifan sistem login (boolean) 
# sdg_on : var. status keaktifan menu utama transaksi (boolean) 
# pil : var. penampung indeks menu terpilih (int) 
# sub_pil : var. penampung indeks menu keluar/tutup terpilih (string) 
def main():
    sis_on = True
    while(sis_on==True):
        if(login()==False):
            beres()
            sis_on = False
        else:
            sdg_on = True
            while(sdg_on==True):
                pil = pilih_menu()
                if(pil==1):
                    if(jmlh<max_data):
                        nyuci()
                    else:
                        print("Penyimpanan transaksi penuh!")
                elif(pil==2):
                    nota()
                elif(pil==3):
                    harian()
                elif(pil==4):
                    bulanan()
                elif(pil==5):
                    cari_pelanggan()
                elif(pil==6):
                    histori()
                elif(pil==7):
                    print()
                    print("=== Pilihan Keluar / Tutup ===")
                    print("1. Log Out (Kembali ke Login)")
                    print("2. Reset Semua Data")
                    print("3. Matikan Sistem + Reset Data")
                    sub_pil = input("Silahkan pilih tindakan : ")
                    if(sub_pil=="1"):
                        sdg_on = False
                        print()
                        print("Anda telah log out!")
                        print("=================================")
                    elif(sub_pil=="2"):
                        reset_data()
                    elif(sub_pil=="3"):
                        reset_data()
                        sdg_on = False
                        sis_on = False
                        beres()
                    else:
                        print("Pilihan tidak valid!")
                else:
                    print("Pilihan tidak valid, silahkan coba lagi.")

# Kamus Global
# max_data : batas maksimum kapasitas penyimpanan data transaksi (int)
# nama : array penyimpan nama pelanggan (array of string)
# kategori : array penyimpan kategori paket (array of string)
# lama : array penyimpan durasi pengerjaan transaksi (array of int)
# tot_harga : array penyimpan total harga bayar transaksi (array of float)
# tgl_in : array penyimpan tanggal masuk [dd, mm, yyyy] (array of array of int)
# tgl_out : array penyimpan tanggal keluar/selesai [dd, mm, yyyy] (array of array of int)
# jmlh : counter pencatat jumlah transaksi yang terdaftar (int)
if __name__ == '__main__':
    max_data = 100
    nama = [None] * max_data
    kategori = [None] * max_data
    lama = [None] * max_data
    tot_harga = [None] * max_data
    tgl_in = [None] * max_data
    tgl_out = [None] * max_data
    jmlh = 0
    main()
