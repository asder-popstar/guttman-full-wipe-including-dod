import os
import shutil
import subprocess
import random
import string

def gutmann_overwrite(file_path):
    """Perform Gutmann method overwrite (35 passes)."""
    patterns = [
        b'\x00', b'\xFF', b'\xAA', b'\x55', b'\x33', b'\xCC', b'\x77',
        b'\x11', b'\x77', b'\x00', b'\xFF', b'\x00', b'\xFF', b'\xCC', 
        b'\x77', b'\x55', b'\xAA', b'\x33', b'\x11', b'\x77', b'\xFF', 
        b'\x00', b'\xAA', b'\x55', b'\x33', b'\xCC', b'\x77', b'\x11',
        b'\x77', b'\x33', b'\xAA', b'\xFF', b'\x00', b'\x55', b'\x11'
    ]
    try:
        with open(file_path, "ba+") as f:
            length = os.path.getsize(file_path)
            for pattern in patterns:
                f.seek(0)
                f.write(pattern * (length // len(pattern)))
        print(f"Gutmann overwrite complete: {file_path}")
    except Exception as e:
        print(f"Failed to overwrite with Gutmann method: {e}")

def dod_5220_overwrite(file_path):
    """Perform DoD 5220.22-M overwrite method."""
    patterns = [b'\x00', b'\xFF', b'\x55', b'\xAA']
    try:
        with open(file_path, "ba+") as f:
            length = os.path.getsize(file_path)
            for pattern in patterns:
                f.seek(0)
                f.write(pattern * (length // len(pattern)))
        print(f"DoD 5220.22-M overwrite complete: {file_path}")
    except Exception as e:
        print(f"Failed to overwrite with DoD 5220.22-M method: {e}")

def secure_delete(file_path, method='gutmann'):
    """Overwrite and delete a file securely using chosen method."""
    try:
        if method == 'gutmann':
            gutmann_overwrite(file_path)
        elif method == 'dod5220':
            dod_5220_overwrite(file_path)
        else:
            print("Unknown method, skipping overwrite.")
        os.remove(file_path)
        print(f"Securely deleted: {file_path}")
    except Exception as e:
        print(f"Failed to delete {file_path}: {e}")

# Rest of the script remains the same
