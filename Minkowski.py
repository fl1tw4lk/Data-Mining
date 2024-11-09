from prettytable import PrettyTable
import math

# Koordinat titik
points = {
    'p1': (1, 1),
    'p2': (4, 1),
    'p3': (1, 2),
    'p4': (3, 4),
    'p5': (5, 4)
}

def minkowski_distance(point1, point2, p):
    """Menghitung jarak Minkowski antara dua titik."""
    return sum(abs(a - b) ** p for a, b in zip(point1, point2)) ** (1 / p)

# Pilih nilai p
p = 2  # Anda bisa mengganti nilai p sesuai kebutuhan

# Membuat tabel untuk hasil
table = PrettyTable()

# Menambahkan header kolom
table.field_names = ["", "p1", "p2", "p3", "p4", "p5"]

# Menghitung jarak dan menambahkan ke tabel
for p1_name, p1_coords in points.items():
    row = [p1_name]  # Mulai baris dengan nama titik
    for p2_name, p2_coords in points.items():
        if p1_name != p2_name:
            distance = minkowski_distance(p1_coords, p2_coords, p)
            row.append(f"{distance:.2f}")

            # Menampilkan langkah perhitungan
            print(f"Jarak antara {p1_name} dan {p2_name}:")
            steps = [f"|{p2_coords[i]} - {p1_coords[i]}|^{p} = {abs(p2_coords[i] - p1_coords[i]) ** p}" for i in range(len(p1_coords))]
            print(f"= ({' + '.join(steps)})^{1}/{p}")
            print(f"= {sum(abs(p2_coords[i] - p1_coords[i]) ** p for i in range(len(p1_coords)))}^{1}/{p}")
            print(f"= {distance:.2f}\n")
        else:
            row.append("-")  # Menambahkan tanda '-' untuk jarak ke dirinya sendiri
    table.add_row(row)

# Menampilkan tabel
print(table)
