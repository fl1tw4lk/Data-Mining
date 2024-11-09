import math
from prettytable import PrettyTable

# Koordinat titik
points = {
    'p1': (1, 1),
    'p2': (4, 1),
    'p3': (1, 2),
    'p4': (3, 4),
    'p5': (5, 4)
}

def euclidean_distance(point1, point2):
    """Menghitung jarak Euclidean antara dua titik."""
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Menghitung jarak antara semua pasangan titik
distances = {}
for p1_name, p1_coords in points.items():
    for p2_name, p2_coords in points.items():
        if p1_name != p2_name:
            distance = euclidean_distance(p1_coords, p2_coords)
            distances[(p1_name, p2_name)] = distance
            
            # Menampilkan langkah-langkah perhitungan
            print(f"Jarak antara {p1_name} dan {p2_name}:")
            print(f"√(({p2_coords[0]} - {p1_coords[0]})² + ({p2_coords[1]} - {p1_coords[1]})²)")
            print(f"= √(({p2_coords[0] - p1_coords[0]})² + ({p2_coords[1] - p1_coords[1]})²)")
            print(f"= √({(p2_coords[0] - p1_coords[0])**2} + {(p2_coords[1] - p1_coords[1])**2})")
            print(f"= √({(p2_coords[0] - p1_coords[0])**2} + {(p2_coords[1] - p1_coords[1])**2})")
            print(f"= {distance:.2f}\n")

# # Menampilkan semua jarak yang dihitung
# print("Semua jarak Euclidean yang dihitung:")
# for (p1, p2), dist in distances.items():
#     print(f"Jarak antara {p1} dan {p2} adalah {dist:.2f}")

def euclidean_distance(point1, point2):
    """Menghitung jarak Euclidean antara dua titik."""
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Membuat tabel untuk hasil
table = PrettyTable()

# Menambahkan header kolom
table.field_names = ["", "p1", "p2", "p3", "p4", "p5"]

# Menghitung jarak dan menambahkan ke tabel
for p1_name in points:
    row = [p1_name]  # Mulai baris dengan nama titik
    for p2_name in points:
        if p1_name != p2_name:
            distance = euclidean_distance(points[p1_name], points[p2_name])
            row.append(f"{distance:.2f}")
        else:
            row.append("-")  # Menambahkan tanda '-' untuk jarak ke dirinya sendiri
    table.add_row(row)

# Menampilkan tabel
print(table)
