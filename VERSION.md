# Versiyon Geçmişi

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
