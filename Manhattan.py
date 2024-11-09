from prettytable import PrettyTable

# Koordinat titik
points = {
    'p1': (1, 1),
    'p2': (4, 1),
    'p3': (1, 2),
    'p4': (3, 4),
    'p5': (5, 4)
}

def manhattan_distance(point1, point2):
    """Menghitung jarak Manhattan antara dua titik."""
    x1, y1 = point1
    x2, y2 = point2
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

# Membuat tabel untuk hasil
table = PrettyTable()

# Menambahkan header kolom
table.field_names = ["", "p1", "p2", "p3", "p4", "p5"]

# Menghitung jarak dan menambahkan ke tabel
for p1_name, p1_coords in points.items():
    row = [p1_name]  # Mulai baris dengan nama titik
    for p2_name, p2_coords in points.items():
        if p1_name != p2_name:
            distance = manhattan_distance(p1_coords, p2_coords)
            row.append(f"{distance}")

            # Menampilkan langkah perhitungan
            print(f"Jarak antara {p1_name} dan {p2_name}:")
            print(f"= |{p2_coords[0]} - {p1_coords[0]}| + |{p2_coords[1]} - {p1_coords[1]}|")
            print(f"= |{p2_coords[0] - p1_coords[0]}| + |{p2_coords[1] - p1_coords[1]}|")
            print(f"= {abs(p2_coords[0] - p1_coords[0])} + {abs(p2_coords[1] - p1_coords[1])}")
            print(f"= {distance}\n")
        else:
            row.append("-")  # Menambahkan tanda '-' untuk jarak ke dirinya sendiri
    table.add_row(row)

# Menampilkan tabel
print(table)
