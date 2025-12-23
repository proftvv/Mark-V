# Versiyon Geçmişi

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
