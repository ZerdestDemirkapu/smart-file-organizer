
from pathlib import Path
import shutil
import logging

klasor = Path(__file__).resolve().parent / "test_dosyalari"


logging.basicConfig(
    filename=Path(__file__).resolve().parent / "islem_kayitlari.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


dosya_turleri = {
    ".jpg": "Resimler",
    ".jpeg": "Resimler",
    ".png": "Resimler",
    ".pdf": "Belgeler",
    ".txt": "Belgeler",
    ".docx": "Belgeler",
    ".xlsx": "Tablolar",
    ".csv": "Tablolar"
}

def kategori_bul(dosya):
    uzanti = dosya.suffix.lower()
    kategori = dosya_turleri.get(uzanti, "Diger")
    return kategori


def dosya_tasi(dosya, kategori):
    hedef_klasor = klasor / kategori
    hedef_klasor.mkdir(exist_ok=True)

    hedef_dosya = hedef_klasor / dosya.name

    if hedef_dosya.exists():
        print(f"Dosya zaten var: {dosya.name}")
        return

    try:
        shutil.move(str(dosya), str(hedef_dosya))
        print(f"Taşındı: {dosya.name} -> {kategori}")
        logging.info(f"Taşındı: {dosya.name} -> {kategori}")

    except OSError as hata:
        print(f"HATA: {dosya.name} taşınamadı!")
        print(f"Sebep: {hata}")
        logging.error(f"{dosya.name} taşınamadı: {hata}")


for dosya in klasor.iterdir():
    if dosya.is_file():
        kategori = kategori_bul(dosya)
        dosya_tasi(dosya, kategori)

print("Dosya düzenleme tamamlandı!")


