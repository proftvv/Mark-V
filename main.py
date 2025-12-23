"""
Mark-V - Macro Tuş Basma Programı
Version: 0.0.2
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from pynput.keyboard import Key, Controller

class MacroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mark-V - Macro Tuş Basma")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.is_running = False
        self.macro_thread = None
        self.keyboard_controller = Controller()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Kullanıcı arayüzünü oluştur"""
        # Başlık
        title_label = tk.Label(
            self.root, 
            text="Mark-V Macro", 
            font=("Arial", 18, "bold"),
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Tuş seçimi
        key_frame = tk.Frame(self.root)
        key_frame.pack(pady=10)
        
        tk.Label(key_frame, text="Tuş:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.key_entry = tk.Entry(key_frame, width=10, font=("Arial", 10))
        self.key_entry.insert(0, "a")
        self.key_entry.pack(side=tk.LEFT, padx=5)
        
        # Süre ayarı
        interval_frame = tk.Frame(self.root)
        interval_frame.pack(pady=10)
        
        tk.Label(interval_frame, text="Aralık (ms):", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.interval_entry = tk.Entry(interval_frame, width=10, font=("Arial", 10))
        self.interval_entry.insert(0, "1000")
        self.interval_entry.pack(side=tk.LEFT, padx=5)
        
        # Kontrol butonları
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.start_button = tk.Button(
            button_frame,
            text="▶ Başlat",
            command=self.start_macro,
            bg="#27ae60",
            fg="white",
            font=("Arial", 12, "bold"),
            width=10,
            cursor="hand2"
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(
            button_frame,
            text="⬛ Durdur",
            command=self.stop_macro,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 12, "bold"),
            width=10,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        # Durum göstergesi
        self.status_label = tk.Label(
            self.root,
            text="Durum: Hazır",
            font=("Arial", 10),
            fg="#7f8c8d"
        )
        self.status_label.pack(pady=10)
        
        # Versiyon
        version_label = tk.Label(
            self.root,
            text="v0.0.2",
            font=("Arial", 8),
            fg="#95a5a6"
        )
        version_label.pack(side=tk.BOTTOM, pady=5)
    
    def start_macro(self):
        """Macro'yu başlat"""
        try:
            # Tuş ve süre bilgilerini al
            key = self.key_entry.get().strip()
            interval = int(self.interval_entry.get())
            
            if not key:
                messagebox.showerror("Hata", "Lütfen bir tuş girin!")
                return
            
            if interval <= 0:
                messagebox.showerror("Hata", "Aralık 0'dan büyük olmalıdır!")
                return
            
            # Macro'yu başlat
            self.is_running = True
            self.macro_thread = threading.Thread(target=self.run_macro, args=(key, interval))
            self.macro_thread.daemon = True
            self.macro_thread.start()
            
            # UI güncellemeleri
            self.status_label.config(text=f"Durum: Çalışıyor... ('{key}' her {interval}ms)", fg="#27ae60")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.key_entry.config(state=tk.DISABLED)
            self.interval_entry.config(state=tk.DISABLED)
            
        except ValueError:
            messagebox.showerror("Hata", "Aralık sayısal bir değer olmalıdır!")
    
    def stop_macro(self):
        """Macro'yu durdur"""
        self.is_running = False
        
        # UI güncellemeleri
        self.status_label.config(text="Durum: Durduruldu", fg="#e74c3c")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.key_entry.config(state=tk.NORMAL)
        self.interval_entry.config(state=tk.NORMAL)
    
    def run_macro(self, key, interval):
        """Macro döngüsü - ayrı thread'de çalışır"""
        press_count = 0
        
        while self.is_running:
            try:
                # Tuşu bas
                if len(key) == 1:
                    # Tek karakter ise direkt bas
                    self.keyboard_controller.press(key)
                    self.keyboard_controller.release(key)
                else:
                    # Özel tuşlar için (space, enter, vb.)
                    special_keys = {
                        'space': Key.space,
                        'enter': Key.enter,
                        'tab': Key.tab,
                        'esc': Key.esc,
                        'shift': Key.shift,
                        'ctrl': Key.ctrl,
                        'alt': Key.alt
                    }
                    
                    if key.lower() in special_keys:
                        self.keyboard_controller.press(special_keys[key.lower()])
                        self.keyboard_controller.release(special_keys[key.lower()])
                    else:
                        # Bilinmeyen tuş, yine de string olarak dene
                        self.keyboard_controller.press(key)
                        self.keyboard_controller.release(key)
                
                press_count += 1
                
                # Durum güncelleme (her 10 basışta bir)
                if press_count % 10 == 0:
                    self.root.after(0, lambda: self.status_label.config(
                        text=f"Durum: Çalışıyor... ({press_count} basış)"
                    ))
                
                # Bekleme süresi (milisaniye cinsinden)
                time.sleep(interval / 1000.0)
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Hata", 
                    f"Tuş basma hatası: {str(e)}"
                ))
                self.root.after(0, self.stop_macro)
                break

def main():
    root = tk.Tk()
    app = MacroApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
