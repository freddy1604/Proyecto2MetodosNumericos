import os

def ensure_folder_exists(folder_path):
    """Verifica si la carpeta existe, de lo contrario la crea."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
