# BHBot 

Bot pertanian emas/XP untuk Brawlhalla 

Sangat terinspirasi oleh [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) 

### ------ --------------------------------------------------- ----------- 

### BOT KEMBALI TERJAGA SECARA AKTIF! 
###### Bergabunglah dengan [Discord](https://discord.gg/2HDmuqqq9p "Discord") untuk membantu memelihara bot atau menambahkan fitur baru! 

### -------------------------------- -------------------- 

**PERINGATAN:** ​​Perangkat lunak ini awalnya dikembangkan untuk penggunaan pribadi. 
Meskipun tidak dirancang untuk melakukan hal tersebut, hal ini berpotensi menyebabkan hasil yang tidak terduga, termasuk pelaksanaan transaksi di Mallhalla menggunakan mata uang dalam game. 

**Pengembang melepaskan semua tanggung jawab atas segala kerusakan yang mungkin timbul dari penggunaan perangkat lunak ini. Disarankan untuk melanjutkan dengan hati-hati dan menggunakan perangkat lunak sesuai kebijaksanaan Anda sendiri.** 

(Bot telah diuji oleh banyak orang selama lebih dari 3.000 jam tanpa masalah per 18/4/2024) 

# Instalasi 
Rilis terbaru selalu dapat diunduh [di sini ](https://github.com/Nick2bad4u/BHBot/releases) 

# Fitur 

- Bekerja sepenuhnya di latar belakang 
- Mengirim input langsung ke Brawlhalla agar tidak mengganggu Anda 
- Meluncurkan game secara otomatis 
- Secara otomatis membuat/mengatur lobi 
- Secara otomatis mengambil/mengubah karakter dan durasi permainan 
- Secara otomatis mendeteksi dan mengatur ulang batas xp 
- Mendukung mode khusus 
- Mendukung bahasa khusus 
- Bahkan mendukung font khusus 
- ~~Membuat kopi untuk Anda~~ (untuk saat ini hanya mendukung teh) 

# Penggunaan 
- Prosesnya dirancang agar intuitif. Cukup pilih pengaturan yang diperlukan dengan mengklik tombol "Pengaturan" 
- Setelah pengaturan disimpan, mulai program dengan mengklik tombol "Mulai" 

# Keterbatasan 
- Bot memerlukan "Tutup persilangan" untuk disetel ke Ya. Jika menurut Anda seharusnya otomatis diatur seperti itu, silakan [buka terbitan](https://github.com/nick2bad4u/bhbot/issues) 
- Bot memerlukan bahasa dalam game untuk disetel ke bahasa Inggris. Jika menurut Anda hal tersebut seharusnya diatur secara otomatis, silakan [buka masalah](https://github.com/nick2bad4u/bhbot/issues) 

# Ikhtisar Teknis 
- Kode yang mendasarinya selalu tersedia untuk ditinjau oleh siapa pun. 
- Pada dasarnya, bot menggunakan Windows SendMessage API untuk mengirimkan masukan langsung ke jendela Brawlhalla. Ini menggunakan deteksi piksel untuk membedakan keadaan dan menentukan tindakan yang tepat pada saat tertentu.

- Kelas BrawlhallaBot dapat digunakan secara langsung atau Anda dapat mengembangkan pembungkus khusus untuk kelas tersebut. Ini dirancang untuk beroperasi secara independen, dengan gui.py hanya berfungsi sebagai pembungkus grafis menggunakan PySimpleGUI.
