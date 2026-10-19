
# Smart File Organizer

Python ile geliştirilmiş otomatik dosya düzenleme uygulaması.

## Özellikler

- Dosyaları uzantılarına göre sınıflandırır.
- Resimler, Belgeler ve Tablolar klasörlerini oluşturur.
- Bilinmeyen uzantıları Diger klasörüne taşır.
- Aynı isimli dosyaların üzerine yazılmasını önler.
- Dosya taşıma hatalarını yakalar.
- İşlem kayıtlarını log dosyasına kaydeder.

## Kullanılan Teknolojiler

- Python
- pathlib
- shutil
- logging

## Nasıl Çalıştırılır?

1. Python 3 kurulu olmalıdır.
2. Proje klasörünün içinde `test_dosyalari` adlı bir klasör oluşturun.
3. Düzenlemek istediğiniz dosyaları bu klasöre ekleyin.
4. Terminalde aşağıdaki komutu çalıştırın:

```bash
python main.py
```

Dosyalar uzantılarına göre alt klasörlere taşınacaktır.

## Proje Yapısı

```text
smart-file-organizer/
├── main.py
├── README.md
└── .gitignore
```

## Not

Program dosyaları taşır, kopyalamaz.
İlk denemelerde yalnızca test dosyaları kullanılması önerilir.
