import os
import shutil
import random

# --- Yapılandırma ---
# Lütfen 'Rice_Image_Dataset' klasörünün, bu Python betiğiyle aynı dizinde olduğundan emin olun.
DATA_DIR = 'C:\\Users\\user\\Desktop\\dataset\\Rice_Image_Dataset'
OUTPUT_DIR = 'rice_dataset'
SPLIT_RATIOS = {'train': 0.7, 'validation': 0.15, 'test': 0.15}
CLASS_NAMES = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']
BATCH_SIZE = 32  # (Eğitim için kalsın, zorunlu değil)

# --- Adım 1 & 2: Klasörleri Oluşturma ---

print(f"Hedef klasör '{OUTPUT_DIR}' kontrol ediliyor...")
# 1. Ana Çıkış Klasörünü Oluşturma
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR)

# 2. Sınıflandırma Klasörlerini Oluşturma
for subset in SPLIT_RATIOS.keys():
    for class_name in CLASS_NAMES:
        path = os.path.join(OUTPUT_DIR, subset, class_name)
        os.makedirs(path)

# --- Adım 3: Dosyaları Dağıtma ve Kopyalama ---

for class_name in CLASS_NAMES:
    # O sınıfa ait görüntülerin bulunduğu KAYNAK alt klasörün yolu
    class_folder_path = os.path.join(DATA_DIR, class_name)

    # Hata Kontrolü: Eğer sınıf klasörü yoksa atla
    if not os.path.exists(class_folder_path):
        print(f"UYARI: Kaynak klasör {class_folder_path} bulunamadı. Bu sınıf atlanıyor.")
        continue

    # O alt klasördeki TÜM görüntü dosyalarını listele
    all_files = [f for f in os.listdir(class_folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    # Dosyaları karıştır
    random.shuffle(all_files)

    # Dağıtım noktalarını hesaplama
    total_count = len(all_files)
    if total_count == 0:
        print(f"UYARI: {class_name} klasöründe hiç görüntü bulunamadı.")
        continue

    train_end = int(total_count * SPLIT_RATIOS['train'])
    validation_end = train_end + int(total_count * SPLIT_RATIOS['validation'])

    # Dosya gruplarını ayırma
    train_files = all_files[:train_end]
    validation_files = all_files[train_end:validation_end]
    test_files = all_files[validation_end:]

    # Dosyaları hedef klasörlere kopyalamak için haritayı oluşturma
    file_map = {
        'train': train_files,
        'validation': validation_files,
        'test': test_files
    }

    # *** KOPYALAMA DÖNGÜSÜ *** (Artık doğru yerde, sınıf döngüsü içinde)
    kopyalanan_sayi = 0
    for subset, files_list in file_map.items():
        dest_path = os.path.join(OUTPUT_DIR, subset, class_name)

        for file_name in files_list:
            src_path = os.path.join(class_folder_path, file_name)

            # shutil.copy(src_path, dest_path)
            shutil.copy(src_path, dest_path)
            kopyalanan_sayi += 1

    print(f"-> {class_name} için {total_count} dosyadan {kopyalanan_sayi} tanesi başarıyla kopyalandı ve ayrıldı.")

print("\nVERİ KÜMESİ HAZIRLAMA İŞLEMİ TAMAMLANDI!")
print(f"Hedef klasör: {os.path.abspath(OUTPUT_DIR)}")