def konversi(j=0):
    def menit(m=0):
        def detik(d=0):
            return ((j * 60) + m) * 60 + d
        return detik
    return menit

# Minta input dari pengguna
input_data = input("Masukkan waktu dalam format 'minggu hari jam menit': ")

# Parsing input pengguna
parts = input_data.split()
weeks = int(parts[0])
days = int(parts[1])
hours = int(parts[2])
minutes = int(parts[3])

# Mengonversi waktu
konvert = konversi(weeks * 7 * 24 * 60)(days * 24 * 60)(hours * 60)(minutes)

# Mencetak hasil konversi
print(f"{weeks} minggu {days} hari {hours} jam {minutes} menit = {konvert} menit")
