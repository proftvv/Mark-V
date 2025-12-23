"""
Mark-V - Macro Tuş Basma Programı
Version: 0.0.9-R2
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import json
import os
import random
from datetime import datetime, timedelta
from pynput.keyboard import Key, Controller, Listener
from PIL import Image, ImageDraw, ImageTk
import pystray

class MacroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mark-V | Private For ZORBEY <3")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#ecf0f1')  # Açık gri arka plan
        
        # Icon ayarla (eğer varsa)
        try:
            self.root.iconbitmap('icon.ico')
        except:
            pass
        
        self.is_running = False
        self.is_paused = False
        self.macro_thread = None
        self.keyboard_controller = Controller()
        self.hotkey_listener = None
        self.tray_icon = None
        self.key_capture_mode = False
        self.key_capture_listener = None
        self.press_count = 0
        self.remaining_count = 0
        self.start_time = None
        self.total_session_presses = 0
        
        # Tema renkleri
        self.themes = {
            'light': {
                'bg': '#ecf0f1',
                'fg': '#2c3e50',
                'secondary': '#7f8c8d',
                'entry_bg': 'white',
                'entry_fg': 'black',
                'button_bg': '#3498db'
            },
            'dark': {
                'bg': '#2c3e50',
                'fg': '#ecf0f1',
                'secondary': '#95a5a6',
                'entry_bg': '#34495e',
                'entry_fg': '#ecf0f1',
                'button_bg': '#2980b9'
            }
        }
        self.current_theme = 'light'
        
        # Ayarlar dosyası
        self.config_file = "config.json"
        self.load_settings()
        
        self.setup_ui()
        self.start_hotkey_listener()
        self.setup_tray()
        
        # Temayı uygula
        if self.current_theme == 'dark':
            self.root.after(100, self.toggle_theme)
        
        # Pencere kapatma olayı
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Minimize olayı
        self.root.bind('<Unmap>', self.on_minimize)
    
    def setup_ui(self):
        """Kullanıcı arayüzünü oluştur"""
        # Arka plan resmi (siluet/watermark)
        try:
            bg_image = Image.open('background.png')
            bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(self.root, image=bg_photo)
            bg_label.image = bg_photo  # Referansı sakla
            bg_label.place(relx=0.5, rely=0.5, anchor='center')
        except:
            pass  # Resim yoksa devam et
        
        # Başlık
        title_label = tk.Label(
            self.root, 
            text="Mark-V Macro", 
            font=("Arial", 18, "bold"),
            fg="#2c3e50",
            bg='#ecf0f1'
        )
        title_label.pack(pady=20)
        
        # Hotkey bilgisi
        hotkey_info = tk.Label(
            self.root,
            text="⌨️ Kısayol: F9 (Başlat/Durdur)",
            font=("Arial", 9),
            fg="#7f8c8d",
            bg='#ecf0f1'
        )
        hotkey_info.pack(pady=5)
        
        # Tuş seçimi
        key_frame = tk.Frame(self.root, bg='#ecf0f1')
        key_frame.pack(pady=10)
        
        tk.Label(key_frame, text="Tuş:", font=("Arial", 10), bg='#ecf0f1').pack(side=tk.LEFT, padx=5)
        self.key_entry = tk.Entry(key_frame, width=15, font=("Arial", 10))
        self.key_entry.insert(0, self.last_key)
        self.key_entry.pack(side=tk.LEFT, padx=5)
        
        # Tuş yakalama butonu
        capture_btn = tk.Button(
            key_frame,
            text="🎯 Yakala",
            command=self.start_key_capture,
            font=("Arial", 9),
            bg="#3498db",
            fg="white",
            cursor="hand2",
            width=8
        )
        capture_btn.pack(side=tk.LEFT, padx=5)
        
        # Süre ayarı
        interval_frame = tk.Frame(self.root, bg='#ecf0f1')
        interval_frame.pack(pady=10)
        
        tk.Label(interval_frame, text="Aralık:", font=("Arial", 10), bg='#ecf0f1').pack(side=tk.LEFT, padx=5)
        self.interval_entry = tk.Entry(interval_frame, width=8, font=("Arial", 10))
        self.interval_entry.insert(0, self.last_interval)
        self.interval_entry.pack(side=tk.LEFT, padx=5)
        
        # Zaman birimi seçici
        self.time_unit = tk.StringVar(value=getattr(self, 'last_time_unit', 'ms'))
        self.time_unit_combo = ttk.Combobox(
            interval_frame,
            textvariable=self.time_unit,
            values=["ms", "saniye"],
            state="readonly",
            width=7,
            font=("Arial", 9)
        )
        self.time_unit_combo.pack(side=tk.LEFT, padx=5)
        
        # Rastgele aralık frame
        random_frame = tk.Frame(self.root, bg='#ecf0f1')
        random_frame.pack(pady=5)
        
        self.random_var = tk.BooleanVar(value=getattr(self, 'last_random', False))
        random_check = tk.Checkbutton(
            random_frame,
            text="🎲 Rastgele Aralık:",
            variable=self.random_var,
            font=("Arial", 9),
            bg='#ecf0f1',
            command=self.toggle_random
        )
        random_check.pack(side=tk.LEFT, padx=5)
        
        tk.Label(random_frame, text="Min:", font=("Arial", 9), bg='#ecf0f1').pack(side=tk.LEFT, padx=2)
        self.min_interval_entry = tk.Entry(random_frame, width=6, font=("Arial", 9), state=tk.DISABLED)
        self.min_interval_entry.insert(0, getattr(self, 'last_min_interval', '500'))
        self.min_interval_entry.pack(side=tk.LEFT, padx=2)
        
        tk.Label(random_frame, text="Max:", font=("Arial", 9), bg='#ecf0f1').pack(side=tk.LEFT, padx=2)
        self.max_interval_entry = tk.Entry(random_frame, width=6, font=("Arial", 9), state=tk.DISABLED)
        self.max_interval_entry.insert(0, getattr(self, 'last_max_interval', '1500'))
        self.max_interval_entry.pack(side=tk.LEFT, padx=2)
        
        # Tekrar sayısı frame
        repeat_frame = tk.Frame(self.root, bg='#ecf0f1')
        repeat_frame.pack(pady=5)
        
        self.infinite_var = tk.BooleanVar(value=getattr(self, 'last_infinite', True))
        infinite_check = tk.Checkbutton(
            repeat_frame,
            text="♾️ Sonsuz",
            variable=self.infinite_var,
            font=("Arial", 9),
            bg='#ecf0f1',
            command=self.toggle_infinite
        )
        infinite_check.pack(side=tk.LEFT, padx=5)
        
        tk.Label(repeat_frame, text="Tekrar Sayısı:", font=("Arial", 9), bg='#ecf0f1').pack(side=tk.LEFT, padx=5)
        self.repeat_entry = tk.Entry(repeat_frame, width=8, font=("Arial", 9), state=tk.DISABLED)
        self.repeat_entry.insert(0, getattr(self, 'last_repeat', '100'))
        self.repeat_entry.pack(side=tk.LEFT, padx=5)
        
        # Kontrol butonları
        button_frame = tk.Frame(self.root, bg='#ecf0f1')
        button_frame.pack(pady=15)
        
        self.start_button = tk.Button(
            button_frame,
            text="▶ Başlat",
            command=self.start_macro,
            bg="#27ae60",
            fg="white",
            font=("Arial", 11, "bold"),
            width=9,
            cursor="hand2"
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.pause_button = tk.Button(
            button_frame,
            text="⏸ Duraklat",
            command=self.pause_macro,
            bg="#f39c12",
            fg="white",
            font=("Arial", 11, "bold"),
            width=9,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(
            button_frame,
            text="⬛ Durdur",
            command=self.stop_macro,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 11, "bold"),
            width=9,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Sayaç göstergesi
        counter_frame = tk.Frame(self.root, bg='#ecf0f1')
        counter_frame.pack(pady=5)
        
        self.counter_label = tk.Label(
            counter_frame,
            text="📊 Basış: 0 | Kalan: ∞",
            font=("Arial", 10, "bold"),
            fg="#2c3e50",
            bg='#ecf0f1'
        )
        self.counter_label.pack()
        
        # Durum göstergesi
        self.status_label = tk.Label(
            self.root,
            text="Durum: Hazır",
            font=("Arial", 10),
            fg="#7f8c8d",
            bg='#ecf0f1'
        )
        self.status_label.pack(pady=10)
        
        # İstatistik paneli
        stats_frame = tk.LabelFrame(
            self.root,
            text="📈 İstatistikler",
            font=("Arial", 9, "bold"),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        stats_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.elapsed_time_label = tk.Label(
            stats_frame,
            text="⏱️ Geçen Süre: 00:00:00",
            font=("Arial", 9),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        self.elapsed_time_label.pack(pady=2)
        
        self.total_presses_label = tk.Label(
            stats_frame,
            text="🎯 Toplam Basış (Oturum): 0",
            font=("Arial", 9),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        self.total_presses_label.pack(pady=2)
        
        # Tema toggle butonu
        theme_btn = tk.Button(
            self.root,
            text="🌓 Tema Değiştir",
            command=self.toggle_theme,
            font=("Arial", 9),
            bg="#9b59b6",
            fg="white",
            cursor="hand2",
            width=15
        )
        theme_btn.pack(pady=5)
        
        # Alt bilgi frame
        footer_frame = tk.Frame(self.root, bg='#ecf0f1')
        footer_frame.pack(side=tk.BOTTOM, pady=10)
        
        # GitHub linki
        github_frame = tk.Frame(footer_frame, bg='#ecf0f1')
        github_frame.pack(pady=2)
        
        github_label = tk.Label(
            github_frame,
            text="⚙️",
            font=("Arial", 10),
            fg="#333333",
            bg='#ecf0f1',
            cursor="hand2"
        )
        github_label.pack(side=tk.LEFT, padx=2)
        github_label.bind("<Button-1>", lambda e: self.open_github())
        
        dev_label = tk.Label(
            github_frame,
            text="Developed by Proftvv",
            font=("Arial", 9),
            fg="#7f8c8d",
            bg='#ecf0f1',
            cursor="hand2"
        )
        dev_label.pack(side=tk.LEFT)
        dev_label.bind("<Button-1>", lambda e: self.open_github())
        
        # Versiyon
        version_label = tk.Label(
            footer_frame,
            text="v0.0.9-R2",
            font=("Arial", 8),
            fg="#95a5a6",
            bg='#ecf0f1'
        )
        version_label.pack(pady=2)
        
        # Widget referanslarını sakla (tema için)
        self.all_buttons = [self.start_button, self.pause_button, self.stop_button, theme_btn]
        self.all_entries = [self.key_entry, self.interval_entry, self.min_interval_entry, self.max_interval_entry, self.repeat_entry]
        self.all_labels = [title_label, hotkey_info, self.counter_label, self.status_label, version_label, dev_label, github_label]
        self.all_frames = [key_frame, interval_frame, random_frame, repeat_frame, button_frame, counter_frame, stats_frame, footer_frame, github_frame]
    
    def toggle_random(self):
        """Rastgele aralık toggle"""
        if self.random_var.get():
            self.min_interval_entry.config(state=tk.NORMAL)
            self.max_interval_entry.config(state=tk.NORMAL)
            self.interval_entry.config(state=tk.DISABLED)
        else:
            self.min_interval_entry.config(state=tk.DISABLED)
            self.max_interval_entry.config(state=tk.DISABLED)
            self.interval_entry.config(state=tk.NORMAL)
        self.save_settings()  # Otomatik kaydet
    
    def toggle_infinite(self):
        """Sonsuz mod toggle"""
        if self.infinite_var.get():
            self.repeat_entry.config(state=tk.DISABLED)
        else:
            self.repeat_entry.config(state=tk.NORMAL)
        self.save_settings()  # Otomatik kaydet
    
    def start_macro(self):
        """Macro'yu başlat"""
        try:
            # Tuş ve süre bilgilerini al
            key = self.key_entry.get().strip()
            
            if not key:
                messagebox.showerror("Hata", "Lütfen bir tuş girin!")
                return
            
            # Rastgele aralık kontrolü
            if self.random_var.get():
                try:
                    min_val = int(self.min_interval_entry.get())
                    max_val = int(self.max_interval_entry.get())
                    if min_val <= 0 or max_val <= 0 or min_val > max_val:
                        messagebox.showerror("Hata", "Min değer Max'tan küçük ve her ikisi de 0'dan büyük olmalı!")
                        return
                except ValueError:
                    messagebox.showerror("Hata", "Min ve Max değerleri sayısal olmalıdır!")
                    return
            else:
                try:
                    interval_value = int(self.interval_entry.get())
                    if interval_value <= 0:
                        messagebox.showerror("Hata", "Aralık 0'dan büyük olmalıdır!")
                        return
                except ValueError:
                    messagebox.showerror("Hata", "Aralık sayısal bir değer olmalıdır!")
                    return
            
            # Tekrar sayısı kontrolü
            if not self.infinite_var.get():
                try:
                    repeat_count = int(self.repeat_entry.get())
                    if repeat_count <= 0:
                        messagebox.showerror("Hata", "Tekrar sayısı 0'dan büyük olmalıdır!")
                        return
                    self.remaining_count = repeat_count
                except ValueError:
                    messagebox.showerror("Hata", "Tekrar sayısı sayısal bir değer olmalıdır!")
                    return
            else:
                self.remaining_count = -1  # Sonsuz
            
            # Macro'yu başlat
            self.is_running = True
            self.is_paused = False
            self.press_count = 0
            self.start_time = datetime.now()
            self.macro_thread = threading.Thread(target=self.run_macro, args=(key,))
            self.macro_thread.daemon = True
            self.macro_thread.start()
            
            # Süre güncelleyici başlat
            self.update_elapsed_time()
            
            # Ayarları kaydet
            self.save_settings()
            
            # UI güncellemeleri
            self.status_label.config(text=f"Durum: Çalışıyor... ('{key}')", fg="#27ae60")
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.key_entry.config(state=tk.DISABLED)
            self.interval_entry.config(state=tk.DISABLED)
            self.min_interval_entry.config(state=tk.DISABLED)
            self.max_interval_entry.config(state=tk.DISABLED)
            self.repeat_entry.config(state=tk.DISABLED)
            self.time_unit_combo.config(state=tk.DISABLED)
            
        except ValueError:
            messagebox.showerror("Hata", "Aralık sayısal bir değer olmalıdır!")
    
    def pause_macro(self):
        """Macro'yu duraklat/devam ettir"""
        if self.is_paused:
            # Devam ettir
            self.is_paused = False
            self.pause_button.config(text="⏸ Duraklat", bg="#f39c12")
            self.status_label.config(text="Durum: Çalışıyor...", fg="#27ae60")
        else:
            # Duraklat
            self.is_paused = True
            self.pause_button.config(text="▶ Devam", bg="#3498db")
            self.status_label.config(text="Durum: Duraklatıldı", fg="#f39c12")
    
    def stop_macro(self):
        """Macro'yu durdur"""
        self.is_running = False
        self.is_paused = False
        self.start_time = None
        
        # UI güncellemeleri
        self.status_label.config(text="Durum: Durduruldu", fg="#e74c3c")
        self.counter_label.config(text="📊 Basış: 0 | Kalan: ∞")
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text="⏸ Duraklat", bg="#f39c12")
        self.stop_button.config(state=tk.DISABLED)
        self.key_entry.config(state=tk.NORMAL)
        
        # Rastgele aralık durumuna göre
        if self.random_var.get():
            self.min_interval_entry.config(state=tk.NORMAL)
            self.max_interval_entry.config(state=tk.NORMAL)
            self.interval_entry.config(state=tk.DISABLED)
        else:
            self.interval_entry.config(state=tk.NORMAL)
            self.min_interval_entry.config(state=tk.DISABLED)
            self.max_interval_entry.config(state=tk.DISABLED)
        
        # Tekrar sayısı durumuna göre
        if not self.infinite_var.get():
            self.repeat_entry.config(state=tk.NORMAL)
        
        self.time_unit_combo.config(state="readonly")
    
    def run_macro(self, key):
        """Macro döngüsü - ayrı thread'de çalışır"""
        
        while self.is_running:
            # Duraklat kontrolü
            while self.is_paused and self.is_running:
                time.sleep(0.1)
                continue
            
            if not self.is_running:
                break
            
            # Tekrar sayısı kontrolü
            if self.remaining_count == 0:
                self.root.after(0, self.stop_macro)
                self.root.after(0, lambda: messagebox.showinfo("Tamamlandı", "Belirlenen tekrar sayısına ulaşıldı!"))
                break
            
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
                
                self.press_count += 1
                self.total_session_presses += 1
                
                # Kalan sayıyı azalt (sonsuz değilse)
                if self.remaining_count > 0:
                    self.remaining_count -= 1
                
                # Sayaç güncelleme
                remaining_text = "∞" if self.remaining_count == -1 else str(self.remaining_count)
                self.root.after(0, lambda: self.counter_label.config(
                    text=f"📊 Basış: {self.press_count} | Kalan: {remaining_text}"
                ))
                self.root.after(0, lambda: self.total_presses_label.config(
                    text=f"🎯 Toplam Basış (Oturum): {self.total_session_presses}"
                ))
                
                # Aralık hesaplama (rastgele veya sabit)
                if self.random_var.get():
                    min_val = int(self.min_interval_entry.get())
                    max_val = int(self.max_interval_entry.get())
                    time_unit = self.time_unit.get()
                    
                    interval_ms = random.randint(min_val, max_val)
                    if time_unit == "saniye":
                        interval_ms *= 1000
                else:
                    interval_value = int(self.interval_entry.get())
                    time_unit = self.time_unit.get()
                    
                    interval_ms = interval_value
                    if time_unit == "saniye":
                        interval_ms *= 1000
                
                # Bekleme süresi (milisaniye cinsinden)
                time.sleep(interval_ms / 1000.0)
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Hata", 
                    f"Tuş basma hatası: {str(e)}"
                ))
                self.root.after(0, self.stop_macro)
                break
    
    def load_settings(self):
        """Ayarları yükle"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.last_key = config.get('key', 'a')
                    self.last_interval = config.get('interval', '1000')
                    self.last_time_unit = config.get('time_unit', 'ms')
                    self.last_random = config.get('random', False)
                    self.last_min_interval = config.get('min_interval', '500')
                    self.last_max_interval = config.get('max_interval', '1500')
                    self.last_infinite = config.get('infinite', True)
                    self.last_repeat = config.get('repeat', '100')
                    self.current_theme = config.get('theme', 'light')
            else:
                self.last_key = 'a'
                self.last_interval = '1000'
                self.last_time_unit = 'ms'
                self.last_random = False
                self.last_min_interval = '500'
                self.last_max_interval = '1500'
                self.last_infinite = True
                self.last_repeat = '100'
        except Exception:
            self.last_key = 'a'
            self.last_interval = '1000'
            self.last_time_unit = 'ms'
            self.last_random = False
            self.last_min_interval = '500'
            self.last_max_interval = '1500'
            self.last_infinite = True
            self.last_repeat = '100'
    
    def save_settings(self):
        """Ayarları kaydet"""
        try:
            config = {
                'key': self.key_entry.get(),
                'interval': self.interval_entry.get(),
                'time_unit': self.time_unit.get(),
                'random': self.random_var.get(),
                'min_interval': self.min_interval_entry.get(),
                'max_interval': self.max_interval_entry.get(),
                'infinite': self.infinite_var.get(),
                'repeat': self.repeat_entry.get(),
                'theme': self.current_theme
            }
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
        except Exception:
            pass
    
    def start_hotkey_listener(self):
        """Hotkey listener'ı başlat"""
        def on_press(key):
            try:
                # F9 tuşu kontrolü
                if key == Key.f9:
                    self.root.after(0, self.toggle_macro)
            except Exception:
                pass
        
        self.hotkey_listener = Listener(on_press=on_press)
        self.hotkey_listener.daemon = True
        self.hotkey_listener.start()
    
    def toggle_macro(self):
        """Macro'yu başlat/durdur (F9 ile)"""
        if self.is_running:
            self.stop_macro()
        else:
            self.start_macro()
    
    def on_closing(self):
        """Pencere kapatma olayı"""
        if self.is_running:
            result = messagebox.askyesno(
                "Uyarı",
                "Macro çalışıyor! Yine de kapatmak istiyor musunuz?"
            )
            if not result:
                return
        
        # Tray'i kapat
        if self.tray_icon:
            self.tray_icon.stop()
        
        # Listener'ı durdur
        if self.hotkey_listener:
            self.hotkey_listener.stop()
        
        # Tuş yakalama listener'ı durdur
        if self.key_capture_listener:
            self.key_capture_listener.stop()
        
        self.root.destroy()
    
    def start_key_capture(self):
        """Tuş yakalama modunu başlat"""
        if self.is_running:
            messagebox.showwarning("Uyarı", "Önce macro'yu durdurun!")
            return
        
        self.key_capture_mode = True
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, "Bir tuşa basın...")
        self.key_entry.config(bg="#fff3cd")
        
        # Tuş yakalama listener'ı başlat
        def on_key_press(key):
            if self.key_capture_mode:
                captured_key = self.format_key(key)
                self.root.after(0, lambda: self.finish_key_capture(captured_key))
                return False  # Listener'ı durdur
        
        self.key_capture_listener = Listener(on_press=on_key_press)
        self.key_capture_listener.start()
    
    def finish_key_capture(self, captured_key):
        """Tuş yakalamayı tamamla"""
        self.key_capture_mode = False
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, captured_key)
        theme = self.themes[self.current_theme]
        self.key_entry.config(bg=theme['entry_bg'], fg=theme['entry_fg'])
        
        if self.key_capture_listener:
            self.key_capture_listener.stop()
            self.key_capture_listener = None
    
    def format_key(self, key):
        """Tuşu formatla"""
        try:
            # Özel tuşlar
            if hasattr(key, 'name'):
                return key.name
            # Normal karakterler
            elif hasattr(key, 'char') and key.char:
                return key.char
            else:
                return str(key).replace("'", "")
        except:
            return str(key).replace("'", "")
    
    def toggle_theme(self):
        """Tema değiştir (açık/koyu)"""
        # Tema değiştir
        self.current_theme = 'dark' if self.current_theme == 'light' else 'light'
        theme = self.themes[self.current_theme]
        
        # Ana pencere
        self.root.config(bg=theme['bg'])
        
        # Tüm frame'ler ve label'lar
        for widget in self.all_frames + self.all_labels:
            try:
                widget.config(bg=theme['bg'], fg=theme['fg'])
            except:
                pass
        
        # Entry'ler
        for entry in self.all_entries:
            try:
                entry.config(bg=theme['entry_bg'], fg=theme['entry_fg'], insertbackground=theme['entry_fg'])
            except:
                pass
        
        # Checkbutton'lar
        try:
            for widget in self.root.winfo_children():
                self.update_widget_theme_recursive(widget, theme)
        except:
            pass
        
        # İstatistikler
        try:
            self.elapsed_time_label.config(bg=theme['bg'], fg=theme['fg'])
            self.total_presses_label.config(bg=theme['bg'], fg=theme['fg'])
        except:
            pass
        
        # Durum label
        try:
            self.status_label.config(bg=theme['bg'])
        except:
            pass
        
        self.save_settings()
    
    def update_widget_theme_recursive(self, widget, theme):
        """Widget temasını recursive güncelle"""
        try:
            widget_type = widget.winfo_class()
            
            if widget_type in ['Label', 'Checkbutton']:
                widget.config(bg=theme['bg'], fg=theme['fg'])
            elif widget_type == 'Frame':
                widget.config(bg=theme['bg'])
            elif widget_type == 'LabelFrame':
                widget.config(bg=theme['bg'], fg=theme['fg'])
            
            # Alt widget'ları da güncelle
            for child in widget.winfo_children():
                self.update_widget_theme_recursive(child, theme)
        except:
            pass
    
    def open_github(self):
        """GitHub profilini aç"""
        import webbrowser
        webbrowser.open("https://github.com/proftvv/")
    
    def setup_tray(self):
        """Sistem tepsisi ikonu oluştur"""
        try:
            # İkon oluştur - PNG'den yükle ve dönüştür
            try:
                icon_image = Image.open('icon.ico')
            except:
                # icon.ico yoksa icon.png'den oluştur
                icon_image = Image.open('icon.png')
            
            # Tray için uygun boyuta getir
            icon_image = icon_image.resize((64, 64), Image.Resampling.LANCZOS)
            
            # Tray menüsü
            menu = pystray.Menu(
                pystray.MenuItem("Göster", self.show_window),
                pystray.MenuItem("Gizle", self.hide_window),
                pystray.MenuItem("Çıkış", self.quit_app)
            )
            
            # Tray ikonu
            self.tray_icon = pystray.Icon("Mark-V", icon_image, "Mark-V Macro", menu)
            
            # Tray'i arka planda çalıştır
            threading.Thread(target=self.tray_icon.run, daemon=True).start()
        except Exception as e:
            print(f"Tray ikon hatası: {e}")
    
    def show_window(self, icon=None, item=None):
        """Pencereyi göster"""
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
    
    def hide_window(self, icon=None, item=None):
        """Pencereyi gizle"""
        self.root.withdraw()
    
    def on_minimize(self, event):
        """Minimize olayında tray'e gönder"""
        if str(event.widget) == '.':
            # Ana pencere minimize edildiğinde gizle
            self.root.after(100, self.hide_window)
    
    def quit_app(self, icon=None, item=None):
        """Uygulamayı kapat"""
        if self.tray_icon:
            self.tray_icon.stop()
        
        if self.hotkey_listener:
            self.hotkey_listener.stop()
        
        if self.key_capture_listener:
            self.key_capture_listener.stop()
        
        self.root.quit()
    
    def update_elapsed_time(self):
        """Geçen süreyi güncelle"""
        if self.is_running and self.start_time:
            elapsed = datetime.now() - self.start_time
            # Formatla: HH:MM:SS
            hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            self.elapsed_time_label.config(text=f"⏱️ Geçen Süre: {time_str}")
            
            # 1 saniye sonra tekrar güncelle
            self.root.after(1000, self.update_elapsed_time)
        else:
            self.elapsed_time_label.config(text="⏱️ Geçen Süre: 00:00:00")

def main():
    root = tk.Tk()
    app = MacroApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
