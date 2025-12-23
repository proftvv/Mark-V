# Versiyon Geçmişi

## v1.0.1 (23 Aralık 2025)

### Değişiklikler:
- 🎮 **F10 Hotkey eklendi**
  - F10 tuşu ile duraklat/devam
  - Çalışırken hızlı duraklat için kısayol
  - F9: Başlat/Durdur
  - F10: Duraklat/Devam
- 📝 **UI güncelleme**
  - Kısayol bilgisi genişletildi
  - Her iki hotkey de gösteriliyor

### Teknik Detaylar:
- `toggle_pause()` fonksiyonu eklendi
- F10 Key.f10 kontrolü
- Hotkey listener'da iki tuş desteği

## v1.0.0 - Stable Release 🎉 (23 Aralık 2025)

### İlk Stabil Sürüm
Mark-V'nin ilk resmi stable sürümü! Tüm core özellikler tamamlandı ve test edildi.

### Özellikler:
- ⌨️ **Tuş Basma Sistemi**
  - Herhangi bir tuşu otomatik basma
  - F9 hotkey ile başlat/durdur
  - Otomatik tuş yakalama (Yakala butonu)
- ⏱️ **Zaman Kontrolü**
  - Milisaniye veya saniye seçimi
  - Rastgele aralık desteği (Min-Max)
  - Hassas zamanlama
- 🔢 **Tekrar Sistemi**
  - Sonsuz mod
  - Belirli tekrar sayısı
  - Canlı sayaç göstergesi
- ⏸️ **Kontrol Özellikleri**
  - Başlat/Duraklat/Durdur butonları
  - Duraklat sırasında state korunması
  - Güvenli kapatma kontrolü
- 📊 **İstatistikler**
  - Geçen süre göstergesi (HH:MM:SS)
  - Toplam basış sayısı (oturum)
  - Kalan tekrar sayısı
- 💾 **Ayarlar**
  - Otomatik kaydetme
  - JSON formatında config
  - Uygulama yeniden açıldığında ayarları hatırlama
- 🎨 **Kullanıcı Arayüzü**
  - Temiz ve basit tasarım
  - Türkçe arayüz
  - Emoji ikonlar
  - Özel pencere ikonu
- 🔗 **Diğer**
  - GitHub profil linki
  - Developer bilgisi
  - MIT Lisans

### Teknik Detaylar:
- Python 3.14.0
- Tkinter GUI
- pynput keyboard control
- PyInstaller ile EXE paketleme
- ~10MB EXE boyutu
- Windows 10/11 uyumlu

### Gelecek Sürümler için Planlar:
- Profil sistemi (birden fazla konfigürasyon)
- İleri seviye istatistikler
- Import/Export ayarları
- Kullanıcı rehberi

---

## v0.0.9-R5 (23 Aralık 2025)

### Değişiklikler:
- ❌ **Background tamamen kaldırıldı**
  - Arka plan watermark/siluet görseli kaldırıldı
  - PIL/Pillow bağımlılığı kaldırıldı
  - Daha hızlı yüklenme
  - Daha küçük EXE dosyası
- ❌ **Tray sistemi kaldırıldı**
  - pystray bağımlılığı kaldırıldı
  - Sistem tepsisi ikonu kaldırıldı
  - Normal Windows minimize davranışı
  - Daha basit kullanım
- 🖼️ **Icon iyileştirmesi**
  - Sadece icon.ico kullanılıyor
  - Windows taskbar'da düzgün görünüyor
  - Daha küçük paket boyutu
- 🧹 **Kod temizliği**
  - setup_tray() fonksiyonu kaldırıldı
  - show_window(), hide_window(), on_minimize(), quit_app() fonksiyonları kaldırıldı
  - PIL/Pillow import'u kaldırıldı
  - pystray import'u kaldırıldı
  - 70+ satır gereksiz kod kaldırıldı

### Teknik Detaylar:
- Sadece tkinter ve pynput bağımlılıkları
- EXE boyutu ~8MB azaldı
- Daha hızlı başlangıç süresi
- Daha az RAM kullanımı

## v0.0.9-R4 (23 Aralık 2025)

### Değişiklikler:
- ❌ **Dark tema kaldırıldı**
  - Tema değiştir butonu kaldırıldı
  - Tema renk sistemi tamamen kaldırıldı
  - Sadece light tema kullanılıyor
  - Daha basit ve temiz kod yapısı
- 🖼️ **Icon ve background düzeltmeleri**
  - Background için sys._MEIPASS kontrolü eklendi
  - PyInstaller ile paketlenmiş EXE'de background düzgün yükleniyor
  - Icon.ico Windows taskbar'da görünüyor
  - Tray icon düzgün görünüyor
- 🧹 **Kod temizliği**
  - toggle_theme() fonksiyonu kaldırıldı
  - update_widget_theme_recursive() fonksiyonu kaldırıldı
  - Config'den theme alanı kaldırıldı
  - Gereksiz widget referansları kaldırıldı

### Teknik Detaylar:
- `sys._MEIPASS` ile PyInstaller resource path çözümü
- `os.path.join()` ile platform-bağımsız path
- Background için exception handling iyileştirildi
- Daha az kod, daha stabil çalışma

## v0.0.9-R3 (23 Aralık 2025)

### Değişiklikler:
- 🎨 **Dark tema iyileştirmesi**
  - Daha iyi renk paleti (#1e272e arka plan)
  - Gelişmiş kontrast oranları
  - Entry'ler için #2f3640 koyu gri
  - LabelFrame için #2f3640 (ana arka plandan daha açık)
  - Metin rengi #f5f6fa (daha okunaklı)
  - İkincil metin #a4b0be
  - Parlak mavi butonlar (#0984e3)
- 🖼️ **Asset güncellemesi**
  - 49988250.jpg'den tüm asset'ler otomatik oluşturuldu
  - icon.ico (çoklu boyut desteği)
  - icon.png (256x256)
  - background.png (200x200, %15 opaklık watermark)
  - logo.png (128x128, renkli)
  - update_assets.py scripti eklendi

### Teknik Detaylar:
- `label_frame_bg` tema rengi eklendi
- LabelFrame içindeki label'lar için özel arka plan
- LANCZOS resampling ile yüksek kaliteli görsel ölçekleme
- Otomatik asset generation scripti

## v0.0.9-R2 (23 Aralık 2025)

### Düzeltmeler:
- 🎨 **Dark tema düzeltmesi**
  - Entry'ler artık dark temada siyah arka plan alıyor
  - Tüm widget'lar (button, label, frame, entry, checkbutton) tema ile güncelleniyor
  - Recursive tema güncelleme ile tüm alt widget'lar da güncelleniyor
  - Entry insert cursor rengi tema ile uyumlu
- 📌 **Versiyon numarası düzeltmesi**
  - Alt tarafta v0.0.9-R2 görünüyor
  - Footer frame eklendi
- 🖼️ **Tray icon düzeltmesi**
  - Icon 64x64 boyutuna ölçekleniyor
  - LANCZOS resampling ile daha kaliteli görüntü
  - PNG fallback desteği
- 👨‍💻 **Developer bilgisi eklendi**
  - "Developed by Proftvv" yazısı alt tarafta
  - Tıklanabilir link
- 🔗 **GitHub linki eklendi**
  - ⚙️ ikonu ile GitHub profil linki
  - https://github.com/proftvv/ adresine yönlendirme
  - webbrowser modülü ile otomatik açılma

### Teknik Detaylar:
- `update_widget_theme_recursive()` ile recursive widget güncelleme
- `entry_bg`, `entry_fg`, `button_bg` tema renkleri eklendi
- `insertbackground` ile cursor rengi güncelleme
- `Image.Resampling.LANCZOS` ile kaliteli ölçekleme
- `webbrowser.open()` ile GitHub linki
- Pencere boyutu 450x600'e genişletildi

## v0.0.9 (23 Aralık 2025)

### Değişiklikler:
- 🖥️ **Sistem tepsisi (System Tray) desteği**
  - Minimize edildiğinde tray'e gönderme
  - Tray menüsü: Göster, Gizle, Çıkış
  - pystray kütüphanesi ile entegrasyon
  - Arka planda çalışma desteği
- 🌓 **Açık/Koyu tema seçici**
  - Light ve Dark tema desteği
  - Tek tuşla tema değiştirme
  - Tüm UI elementlerini otomatik güncelleme
  - Tema tercihi config'e kaydediliyor
- 💾 **Otomatik kaydetme**
  - Checkbox değişikliklerinde otomatik kayıt
  - Entry değişikliklerinde otomatik kayıt
  - Kullanıcı deneyimi iyileştirmesi
- 📈 **Gelişmiş istatistikler**
  - ⏱️ Geçen süre göstergesi (HH:MM:SS)
  - 🎯 Toplam basış sayısı (oturum boyunca)
  - Gerçek zamanlı güncelleme
  - İstatistik paneli eklendi

### Teknik Detaylar:
- `pystray` ile sistem tepsisi ikonu
- `datetime` ve `timedelta` ile süre takibi
- `total_session_presses` değişkeni ile toplam sayaç
- Tema sistemi: light/dark renk paletleri
- `update_widget_theme()` ile recursive widget güncelleme
- `update_elapsed_time()` ile 1 saniyelik süre güncelleyici
- Config dosyasına `theme` alanı eklendi
- `on_minimize` event handler ile tray entegrasyonu

## v0.0.8 (23 Aralık 2025)

### Değişiklikler:
- 🔢 **Tekrar sayısı özelliği**
  - Sonsuz mod veya belirli sayıda tekrar
  - "X kere bas ve dur" özelliği
  - Checkbox ile kolay geçiş
- 🎲 **Rastgele aralık özelliği**
  - Min-Max değer aralığında rastgele bekleme
  - Daha doğal makro simulas yonu
  - Checkbox ile aktif/pasif
- 📊 **Canlı sayaç göstergesi**
  - Toplam basış sayısı
  - Kalan tekrar sayısı
  - Gerçek zamanlı güncelleme
- ⏸️ **Duraklat/Devam butonu**
  - Makroyu durdurmadan duraklatma
  - Tek tuşla devam ettirme
  - Dinamik buton metni
- 🎨 **UI iyileştirmeleri**
  - Pencere boyutu büyütüldü (450x500)
  - 3 buton sistemi (Başlat, Duraklat, Durdur)
  - Daha organize layout
  - Emoji ikonlar

### Teknik Detaylar:
- `random.randint()` ile rastgele aralık
- `is_paused` state ile pause/resume
- `remaining_count` ile tekrar takibi
- Dinamik UI state yönetimi
- Config dosyasına 4 yeni alan eklendi

## v0.0.7 (23 Aralık 2025)

### Değişiklikler:
- 🎨 **Arka plan siluet görseli eklendi**
  - Profil resmi siluet/watermark olarak arka planda
  - PIL ile görsel işleme (gri tonlama, şeffaflık)
  - %15 opaklık ile ince watermark efekti
  - 200x200 boyutunda merkeze yerleştirildi
- 🎨 **UI renk şeması güncellendi**
  - Açık gri (#ecf0f1) arka plan
  - Tüm elementlerin arka plan renkleri uyumlu hale getirildi
  - Daha modern ve temiz görünüm
- 📦 **EXE paketleme iyileştirildi**
  - background.png dosyası EXE'ye gömüldü
  - --add-data parametresi ile otomatik ekleme

### Teknik Detaylar:
- `ImageTk.PhotoImage` ile Tkinter'da resim gösterme
- `place()` geometri yöneticisi ile merkeze yerleştirme
- `ImageEnhance.Brightness` ile şeffaflık ayarlaması
- PyInstaller --add-data ile runtime data ekleme

## v0.0.6 (23 Aralık 2025)

### Değişiklikler:
- ⏱️ **Zaman birimi seçici eklendi**
  - Milisaniye (ms) veya Saniye seçeneği
  - Combobox ile kolay seçim
  - Otomatik dönüştürme (saniye -> ms)
  - Ayarlarda zaman birimi kaydetme
- 🎯 **Otomatik tuş yakalama**
  - "🎯 Yakala" butonu eklendi
  - Butona tıklayıp bir tuşa basınca otomatik algılama
  - pynput.Listener ile gerçek zamanlı tuş yakalama
  - Tüm tuşlar desteklenir (a-z, 0-9, space, enter, shift, vb.)
  - Visual feedback (sarı arka plan)
- 🎨 **UI iyileştirmeleri**
  - Genişletilmiş tuş input alanı
  - Zaman birimi combobox'u
  - Daha düzgün layout
  - Responsive buton durumları

### Teknik Detaylar:
- `ttk.Combobox` ile zaman birimi seçici
- `pynput.Listener` ile ayrı tuş yakalama listener'ı
- `format_key()` metodu ile tuş formatlaması
- Config dosyasına time_unit eklendi

## v0.0.5 (23 Aralık 2025)

### Değişiklikler:
- 🏷️ **Başlık formatı güncellendi**
  - "Mark-V | Private For ZORBEY <3" formatına geçildi
  - Pipe (|) karakteri ile daha temiz görünüm
  - Hem pencere başlığı hem taskbar'da yeni format

### Teknik Detaylar:
- root.title() güncellendi
- EXE yeniden build edildi

## v0.0.4 (23 Aralık 2025)

### Değişiklikler:
- 🎨 **Özel ikon eklendi**
  - Uygulama ikonu olarak profil resmi kullanıldı
  - icon.ico dosyası oluşturuldu
  - PyInstaller --icon parametresi ile EXE'ye gömüldü
- 📝 **Pencere başlığı kişiselleştirildi**
  - "Mark-V Private For ZORBEY <3" başlığı
  - tkinter iconbitmap() ile pencere ikonu
- 🛠️ **Build süreci iyileştirildi**
  - create_icon.py scripti eklendi
  - PNG'den ICO'ya otomatik dönüştürme
  - Çoklu boyut desteği (16x16 - 256x256)

### Teknik Detaylar:
- PIL/Pillow ile çoklu boyut icon oluşturma
- Windows standart ikon boyutları desteği
- root.iconbitmap() ile runtime icon

## v0.0.3 (23 Aralık 2025)

### Değişiklikler:
- ⌨️ **Hotkey desteği eklendi**
  - F9 tuşu ile başlat/durdur
  - pynput.keyboard.Listener ile global hotkey dinleme
  - UI'da hotkey bilgi etiketi
- 💾 **Ayar kaydetme/yükleme sistemi**
  - config.json dosyasına otomatik kaydetme
  - Son kullanılan tuş ve aralık değerlerini hatırlama
  - UTF-8 encoding desteği
- 🔒 **Gelişmiş güvenlik**
  - Çalışırken kapatma uyarısı
  - WM_DELETE_WINDOW event handling
  - Listener cleanup on exit
- 🎨 **UI iyileştirmeleri**
  - Pencere boyutu güncellendi (350px)
  - Hotkey kısayol bilgisi göstergesi
  - Daha temiz arayüz
- 🧹 **Kod optimizasyonu**
  - Daemon thread kullanımı
  - Exception handling iyileştirmeleri
  - Config dosya yönetimi

### Teknik Detaylar:
- `pynput.keyboard.Listener` ile F9 tuş dinleme
- `json.dump/load` ile ayar kaydetme
- `root.protocol` ile pencere kapatma kontrolü
- Saved settings: key, interval

## v0.0.2 (23 Aralık 2025)

### Değişiklikler:
- ✅ **Tuş basma mekanizması eklendi**
  - pynput.keyboard kullanılarak tuş kontrol sistemi
  - Tek karakter ve özel tuşlar (space, enter, tab, vb.) desteği
  - Threading ile arka planda çalışma
- ⏱️ **Zamanlayıcı sistem implement edildi**
  - Milisaniye cinsinden ayarlanabilir aralık
  - Thread-safe basış sayacı
  - Her 10 basışta durum güncelleme
- 🎨 **UI iyileştirmeleri**
  - Basış sayısı göstergesi
  - Çalışırken input alanları kilitleme
  - Hata mesajları (messagebox)
  - Detaylı durum bilgisi
- 📄 **MIT Lisansı eklendi**
  - README'de lisans badge'i
  - LICENSE dosyası güncellendi
- 🔧 **Kod iyileştirmeleri**
  - Try-catch blokları ile hata yönetimi
  - Input validasyonu
  - Thread daemon mode

### Teknik Detaylar:
- `Controller()` ile klavye kontrolü
- `threading.Thread` ile async tuş basma
- `time.sleep()` ile milisaniye hassasiyetli bekleme

## v0.0.1 (23 Aralık 2025)

### Değişiklikler:
- ✨ Proje başlatıldı
- 📁 Temel klasör yapısı oluşturuldu
- 📝 Git repository kurulumu
- 📄 Proje dokümantasyonu hazırlandı
- 🔧 .gitignore ve temel dosyalar eklendi

### Planlanan Özellikler:
- Tuş basma mekanizması
- Zamanlayıcı sistem
- Tkinter GUI arayüzü
- EXE dönüşümü

### Değişiklikler:
- ✅ **Tuş basma mekanizması eklendi**
  - pynput.keyboard kullanılarak tuş kontrol sistemi
  - Tek karakter ve özel tuşlar (space, enter, tab, vb.) desteği
  - Threading ile arka planda çalışma
- ⏱️ **Zamanlayıcı sistem implement edildi**
  - Milisaniye cinsinden ayarlanabilir aralık
  - Thread-safe basış sayacı
  - Her 10 basışta durum güncelleme
- 🎨 **UI iyileştirmeleri**
  - Basış sayısı göstergesi
  - Çalışırken input alanları kilitleme
  - Hata mesajları (messagebox)
  - Detaylı durum bilgisi
- 📄 **MIT Lisansı eklendi**
  - README'de lisans badge'i
  - LICENSE dosyası güncellendi
- 🔧 **Kod iyileştirmeleri**
  - Try-catch blokları ile hata yönetimi
  - Input validasyonu
  - Thread daemon mode

### Teknik Detaylar:
- `Controller()` ile klavye kontrolü
- `threading.Thread` ile async tuş basma
- `time.sleep()` ile milisaniye hassasiyetli bekleme

## v0.0.1 (23 Aralık 2025)

### Değişiklikler:
- ✨ Proje başlatıldı
- 📁 Temel klasör yapısı oluşturuldu
- 📝 Git repository kurulumu
- 📄 Proje dokümantasyonu hazırlandı
- 🔧 .gitignore ve temel dosyalar eklendi

### Planlanan Özellikler:
- Tuş basma mekanizması
- Zamanlayıcı sistem
- Tkinter GUI arayüzü
- EXE dönüşümü
