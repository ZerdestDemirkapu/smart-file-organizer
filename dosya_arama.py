
from pathlib import Path

def dosya_ara(klasor, aranan_dosya):
    klasor = Path(klasor)

    for dosya in klasor.rglob("*"):
        if dosya.is_file() and dosya.name.lower() == aranan_dosya.lower():
            print(f"Dosya bulundu: {dosya}")
            return

    print("Aranan dosya bulunamadı.")


if __name__ == "__main__":
    test_klasoru = Path(__file__).resolve().parent / "test_dosyalari"

    aranan = input("Aramak istediğiniz dosyanın adını girin: ")
    dosya_ara(test_klasoru, aranan)
