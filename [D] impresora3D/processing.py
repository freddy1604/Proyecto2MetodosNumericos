import os
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import filedialog, messagebox

def load_svg_file(filepath):
    """Carga un archivo SVG y extrae el polígono principal."""
    tree = ET.parse(filepath)
    root = tree.getroot()
    namespace = {'svg': 'http://www.w3.org/2000/svg'}
    
    for polygon in root.findall('.//polygon', namespace):
        points = polygon.get('points')
        if points:
            return [tuple(map(float, p.split(','))) for p in points.split()]
    
    return None

def generate_filling_path(polygon, resolution):
    """Genera la trayectoria de relleno para la impresión basada en la resolución."""
    min_x = min(p[0] for p in polygon)
    max_x = max(p[0] for p in polygon)
    min_y = min(p[1] for p in polygon)
    max_y = max(p[1] for p in polygon)
    
    fill_lines = []
    y = min_y
    while y <= max_y:
        intersections = []
        for i in range(len(polygon)):
            p1, p2 = polygon[i], polygon[(i+1) % len(polygon)]
            if (p1[1] <= y <= p2[1]) or (p2[1] <= y <= p1[1]):
                if p1[1] != p2[1]:
                    x_intersect = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                    intersections.append(x_intersect)
        
        intersections.sort()
        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                fill_lines.append([(intersections[i], y), (intersections[i+1], y)])
        
        y += resolution
    
    return fill_lines

def animate_printing(frame, ax, polygon, fill_lines):
    """Animación de la impresión progresiva."""
    ax.clear()
    polygon_np = np.array(polygon)
    ax.plot(polygon_np[:, 0], polygon_np[:, 1], color='blue', linewidth=2)
    
    for line in fill_lines[:frame]:
        line_np = np.array(line)
        ax.plot(line_np[:, 0], line_np[:, 1], color='orange', linewidth=1)

def start_printing(resolution):
    """Ejecuta el proceso de carga y animación de la impresión."""
    filepath = filedialog.askopenfilename(filetypes=[("SVG files", "*.svg")])
    if not filepath:
        return
    
    polygon = load_svg_file(filepath)
    if polygon is None:
        messagebox.showerror("Error", "No se encontró un polígono en el archivo SVG.")
        return
    
    fill_lines = generate_filling_path(polygon, resolution)
    
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, animate_printing, frames=len(fill_lines), fargs=(ax, polygon, fill_lines), interval=100)
    plt.show()
