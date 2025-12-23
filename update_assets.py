"""
Asset güncelleme scripti - icon, background ve logo oluşturur
"""
from PIL import Image, ImageEnhance, ImageDraw

# 1. Icon oluştur (icon.ico)
print("Icon oluşturuluyor...")
img = Image.open('49988250.jpg')

# Kare yap (merkeze crop)
width, height = img.size
min_side = min(width, height)
left = (width - min_side) // 2
top = (height - min_side) // 2
img_square = img.crop((left, top, left + min_side, top + min_side))

# Boyutları ayarla
sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
icon_images = []
for size in sizes:
    icon_images.append(img_square.resize(size, Image.Resampling.LANCZOS))

# ICO olarak kaydet
icon_images[0].save('icon.ico', format='ICO', sizes=[(img.size[0], img.size[1]) for img in icon_images])
print("✓ icon.ico oluşturuldu")

# 2. Background oluştur (siluet/watermark)
print("\nBackground oluşturuluyor...")
bg_img = img_square.copy()

# 200x200 boyutuna getir
bg_img = bg_img.resize((200, 200), Image.Resampling.LANCZOS)

# Gri tonlama
bg_img = bg_img.convert('L').convert('RGB')

# %15 opaklık için parlaklığı düşür
enhancer = ImageEnhance.Brightness(bg_img)
bg_img = enhancer.enhance(0.15)

# Kaydet
bg_img.save('background.png')
print("✓ background.png oluşturuldu (200x200, %15 opaklık)")

# 3. Logo oluştur (daha büyük, renkli)
print("\nLogo oluşturuluyor...")
logo_img = img_square.resize((128, 128), Image.Resampling.LANCZOS)
logo_img.save('logo.png')
print("✓ logo.png oluşturuldu (128x128, renkli)")

# 4. icon.png oluştur (PNG versiyonu)
print("\nIcon PNG oluşturuluyor...")
icon_png = img_square.resize((256, 256), Image.Resampling.LANCZOS)
icon_png.save('icon.png')
print("✓ icon.png oluşturuldu (256x256)")

print("\n✅ Tüm asset'ler başarıyla oluşturuldu!")
print("📁 Oluşturulan dosyalar:")
print("   - icon.ico (çoklu boyut)")
print("   - icon.png (256x256)")
print("   - background.png (200x200, watermark)")
print("   - logo.png (128x128, renkli)")
