# Mark-V - Macro Tuş Basma Programı

![Version](https://img.shields.io/badge/version-0.0.8-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Açıklama

Mark-V, belirli bir tuşu ayarlanabilir aralıklarla otomatik olarak basan bir macro programıdır. 

## ✨ Özellikler

- 🔢 Tekrar sayısı ayarlama (sonsuz veya sınırlı)
- 🎲 Rastgele aralık (Min-Max değer aralığı)
- 📊 Canlı sayaç (basış & kalan)
- ⏸️ Duraklat/Devam özelliği
- ⏱️ Basma aralığını ms veya saniye olarak ayarlama
- 🎯 Otomatik tuş yakalama (Yakala butonu ile)
- ⌨️ İstediğiniz tuşu seçebilme
- ⏰ Basma aralığını milisaniye veya saniye cinsinden ayarlama
- ▶️ Başlat/Durdur kontrolleri
- 🎯 Basit ve kullanıcı dostu arayüz
- 💻 Windows EXE formatında çalışır
- 🔥 F9 tuşu ile hızlı başlat/durdur (Hotkey)
- 💾 Ayarları otomatik kaydetme ve yükleme
- 🔒 Çalışırken kapatma koruması

## 🚀 Kurulum

### Seçenek 1: EXE Dosyası (Önerilen)
1. [Releases](https://github.com/proftvv/Mark-V/releases) sayfasından en son `MarkV.exe` dosyasını indirin
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
