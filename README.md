# Mark-V - Macro Tuş Basma Programı

![Version](https://img.shields.io/badge/version-1.0.1-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-blue)

## 📖 Açıklama

Mark-V, belirli bir tuşu ayarlanabilir aralıklarla otomatik olarak basan profesyonel bir macro programıdır. Windows için optimize edilmiş, kullanıcı dostu arayüze sahip ve güçlü özellikleriyle oyun ve otomasyon ihtiyaçlarınız için ideal bir çözüm sunar.

## ✨ Özellikler

### 🎯 Ana Özellikler
- ⌨️ **Tuş Kontrolü**: Herhangi bir tuşu otomatik basma
- 🎯 **Otomatik Yakalama**: Tuş yakalama butonu ile kolay ayarlama
- 🔥 **F9 Hotkey**: Hızlı başlat/durdur kısayolu
- ⏸️ **F10 Hotkey**: Hızlı duraklat/devam kısayolu
- ⏱️ **Zaman Ayarı**: Milisaniye veya saniye cinsinden hassas zamanlama
- 🎲 **Rastgele Aralık**: Min-Max değer aralığında doğal simülasyon
- 🔢 **Tekrar Kontrolü**: Sonsuz veya belirli sayıda tekrar
- ⏸️ **Duraklat/Devam**: Makroyu durdurmadan duraklatma

### 📊 İstatistikler ve Takip
- 📈 **Gelişmiş İstatistikler**: Geçen süre ve toplam basış sayısı
- 📊 **Canlı Sayaç**: Anlık basış ve kalan tekrar göstergesi
- 💾 **Otomatik Kaydetme**: Ayarlar anında kaydedilir

### 🎨 Kullanıcı Deneyimi
- 🎨 Temiz ve modern arayüz
- 🇹🇷 Türkçe dil desteği
- 💻 Windows 10/11 uyumlu
- 🔒 Çalışırken kapatma koruması
- 🔗 GitHub entegrasyonu

## 🚀 Kurulum

### Seçenek 1: EXE Dosyası (Önerilen)
1. [Releases](https://github.com/proftvv/Mark-V/releases) sayfasından `Mark-V-v1.0.1.exe` dosyasını indirin
2. İndirilen EXE'yi çalıştırın
3. Python kurulumuna gerek yok!

### Seçenek 2: Kaynak Koddan Çalıştırma

#### Gereksinimler
- Python 3.8 veya üzeri
- pip paket yöneticisi

#### Bağımlılıkları Yükleme
```bash
pip install -r requirements.txt
```

#### Programı Çalıştırma
```bash
python main.py
```

### Seçenek 3: Kendi EXE'nizi Oluşturma
```bash
pip install -r requirements.txt
pyinstaller --onefile --windowed --name=MarkV --clean main.py
```
Oluşturulan EXE: `dist/MarkV.exe`

Detaylı build bilgisi için [BUILD.md](BUILD.md) dosyasına bakınız.

## 🎮 Kullanım

1. Programı başlatın
2. Basmak istediğiniz tuşu girin
3. Basma aralığını milisaniye cinsinden ayarlayın
4. "Başlat" butonuna tıklayın veya **F9** tuşuna basın
5. Durdurmak için "Durdur" butonuna tıklayın veya **F9** tuşuna basın

### 🔥 Kısayollar
- **F9**: Macro'yu başlat/durdur (global hotkey)

### 📋 Desteklenen Tuşlar
- Tek karakterler: `a`, `b`, `1`, `2`, vb.
- Özel tuşlar: `space`, `enter`, `tab`, `esc`, `shift`, `ctrl`, `alt`

## 📋 Versiyon Geçmişi

Detaylı versiyon geçmişi için [VERSION.md](VERSION.md) dosyasına bakınız.

## 🛠️ Geliştirme

Bu proje aktif olarak geliştirilmektedir. Önerileriniz için issue açabilirsiniz.

## ⚠️ Uyarı

Bu program sadece eğitim amaçlıdır. Kullanımdan doğacak sorumluluk kullanıcıya aittir.

## 📝 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
