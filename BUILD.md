# Build Kılavuzu

## 🔧 EXE Oluşturma

### Gereksinimler
- Python 3.8 veya üzeri
- pip ile yüklenmiş bağımlılıklar

### Adım 1: Bağımlılıkları Yükleme
```bash
pip install -r requirements.txt
```

### Adım 2: EXE Oluşturma
```bash
pyinstaller --onefile --windowed --name=MarkV --clean main.py
```

### Parametreler:
- `--onefile`: Tek bir EXE dosyası oluştur
- `--windowed`: Console penceresi gösterme (GUI modu)
- `--name=MarkV`: EXE dosya adı
- `--clean`: Önceki build dosyalarını temizle

### Adım 3: EXE Konumu
Oluşturulan EXE dosyası:
```
dist/MarkV.exe
```

## 📦 Dosya Yapısı (Build Sonrası)

```
Mark-V/
├── dist/
│   └── MarkV.exe          # ✅ Kullanılabilir EXE
├── build/                  # Geçici build dosyaları
├── main.py                 # Ana kaynak kod
├── MarkV.spec             # PyInstaller spec dosyası
└── requirements.txt        # Python bağımlılıkları
```

## 🚀 Dağıtım

EXE dosyası bağımsızdır ve şunları içerir:
- Python interpreter
- Tüm gerekli kütüphaneler (pynput, pystray, Pillow, tkinter)
- Uygulama kodu

Kullanıcıların Python yüklemesine gerek yoktur!

## 🔍 Sorun Giderme

### Hata: "Failed to execute script"
- Antivirüs programını kontrol edin
- `--clean` parametresi ile yeniden build edin

### Hata: "Missing module"
- requirements.txt'deki tüm paketlerin yüklü olduğundan emin olun
- Virtual environment kullanıyorsanız aktif olduğundan emin olun

### EXE boyutu çok büyük
- Normal! Tkinter ve PIL gibi kütüphaneler dahil olduğu için ~20-30 MB olabilir
- UPX ile sıkıştırma: `pyinstaller --onefile --windowed --name=MarkV --upx-dir=<upx_path> main.py`
