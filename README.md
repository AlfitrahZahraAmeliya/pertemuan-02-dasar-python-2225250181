# Pertemuan 02 - Dasar Python

## Identitas

Nama: Alfitrah Zahra Ameliya  
NIM: 2225250181  
Kelas: 3B  

## Tujuan

Project ini dibuat untuk memenuhi tugas Pertemuan ke-2 mata kuliah Algoritma dan Pemrograman. Project ini bertujuan untuk menerapkan dasar-dasar Python menggunakan VS Code, meliputi variabel, tipe data, input dan output, operator aritmatika, serta pengujian program.

## Struktur Project

Project ini terdiri dari beberapa file latihan dan satu tugas utama:

- `latihan/01_biodata.py`  
  Program untuk membuat kartu biodata dan menghitung perkiraan usia.

- `latihan/02_persegi_panjang.py`  
  Program untuk menghitung luas dan keliling persegi panjang.

- `latihan/03_konversi_suhu.py`  
  Program untuk mengonversi suhu Celsius menjadi Fahrenheit dan Kelvin.

- `latihan/04_nilai_akhir.py`  
  Program untuk menghitung nilai akhir berdasarkan nilai tugas, UTS, dan UAS.

- `tugas/kalkulator_koordinat.py`  
  Program untuk menghitung perubahan koordinat, jarak antara dua titik, dan titik tengah dua titik.

## Cara Menjalankan Program

Pastikan Python 3 sudah terpasang dan folder project sudah dibuka melalui VS Code.

Program dapat dijalankan melalui terminal dengan perintah:

```bash
python latihan/01_biodata.py
```

```bash
python latihan/02_persegi_panjang.py
```

```bash
python latihan/03_konversi_suhu.py
```

```bash
python latihan/04_nilai_akhir.py
```

Untuk menjalankan tugas utama:

```bash
python tugas/kalkulator_koordinat.py
```

## Pengujian Tugas Utama

### Test Case 1

Input:
- x titik A = 0
- y titik A = 0
- x titik B = 3
- y titik B = 4

Output:

```text
KALKULATOR KOORDINAT DUA TITIK
Titik A : (0.00, 0.00)
Titik B : (3.00, 4.00)
Perubahan : dx = 3.00, dy = 4.00
Jarak A ke B : 5.00
Titik tengah : (1.50, 2.00)
```

### Test Case 2

Input:
- x titik A = -2
- y titik A = 1
- x titik B = 4
- y titik B = 1

Output:

```text
KALKULATOR KOORDINAT DUA TITIK
Titik A : (-2.00, 1.00)
Titik B : (4.00, 1.00)
Perubahan : dx = 6.00, dy = 0.00
Jarak A ke B : 6.00
Titik tengah : (1.00, 1.00)
```

### Test Case 3

Input:
- x titik A = 2.5
- y titik A = -1
- x titik B = 2.5
- y titik B = 3

Output:

```text
KALKULATOR KOORDINAT DUA TITIK
Titik A : (2.50, -1.00)
Titik B : (2.50, 3.00)
Perubahan : dx = 0.00, dy = 4.00
Jarak A ke B : 4.00
Titik tengah : (2.50, 1.00)
```

## Refleksi

Melalui tugas ini, saya belajar menggunakan Python dasar melalui VS Code, terutama dalam penggunaan variabel, tipe data, input dan output, operator aritmatika, serta format output menggunakan f-string. Saya juga belajar melakukan pengujian program dengan beberapa data input untuk memastikan hasil perhitungan sesuai dengan yang diharapkan. Selain itu, saya belajar menggunakan Git dan GitHub untuk mengelola serta mengumpulkan project. Pengujian dilakukan dengan beberapa variasi input dan seluruh hasil perhitungan pada tugas utama sesuai dengan perhitungan yang diharapkan.

## Sumber

Bahan Ajar Dasar Python di VS Code dan Pengumpulan melalui GitHub - Pertemuan ke-2, Dr. Aan Hendrayana, S.Si., M.Pd., Algoritma dan Pemrograman, S1 Pendidikan Matematika FKIP UNTIRTA, 2026/2027 Ganjil.