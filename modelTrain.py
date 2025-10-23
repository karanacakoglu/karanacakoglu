import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# =================================================================
# 1. YAPILANDIRMA VE VERİ JENERATÖRLERİNİN OLUŞTURULMASI
# =================================================================
NUM_RICE_CLASSES = 5 # Kaç tane pirinç türünüz varsa (Arborio, Basmati, vs.)
TARGET_SIZE = (224, 224)
BATCH_SIZE = 32
OUTPUT_DIR = 'rice_dataset' # Veri klasörünüzün adı

# ResNet50'ye özel ön işleme fonksiyonu
resnet_preprocess = tf.keras.applications.resnet50.preprocess_input

# --- Eğitim Verisi Akışı (Veri Artırma Dahil) ---
train_datagen = ImageDataGenerator(
    preprocessing_function=resnet_preprocess,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    rotation_range=20
)

train_generator = train_datagen.flow_from_directory(
    os.path.join(OUTPUT_DIR, 'train'),
    target_size=TARGET_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# --- Doğrulama Verisi Akışı (Sadece Ön İşleme) ---
val_test_datagen = ImageDataGenerator(
    preprocessing_function=resnet_preprocess
)

validation_generator = val_test_datagen.flow_from_directory(
    os.path.join(OUTPUT_DIR, 'validation'),
    target_size=TARGET_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Gerekirse sınıf sayısını jeneratörden al
# NUM_RICE_CLASSES = train_generator.num_classes

# =================================================================
# 2. MODEL MİMARİSİNİN OLUŞTURULMASI
# =================================================================

# Temel Modeli Yükleme (ImageNet ağırlıklarıyla ve üst katman hariç)
base_model = ResNet50(weights='imagenet',
                      include_top=False,
                      input_shape=(TARGET_SIZE[0], TARGET_SIZE[1], 3))

# Temel Modeli Dondurma
base_model.trainable = False

# Yeni Sınıflandırma Başlığını Ekleme (Sequential model)
model = Sequential([
    base_model,                               # Dondurulmuş ResNet50
    GlobalAveragePooling2D(),                 # Özellikleri düzleştir
    Dense(512, activation='relu'),            # Gizli katman
    Dense(NUM_RICE_CLASSES, activation='softmax') # Çıkış katmanı
])

model.summary()

# =================================================================
# 3. MODELİN DERLENMESİ VE EĞİTİMİN BAŞLATILMASI
# =================================================================

# Optimize Edici ve Derleme
optimizer = Adam(learning_rate=0.0001)
model.compile(optimizer=optimizer,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Geri Çağrılar
checkpoint_filepath = 'best_rice_classifier.h5'
model_checkpoint_callback = ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_weights_only=False,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True
)

early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

print("\nModel Eğitiliyor (Transfer Öğrenme)...")
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // BATCH_SIZE,
    epochs=20, # İlk aşama için başlangıç denemesi
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // BATCH_SIZE,
    callbacks=[model_checkpoint_callback, early_stopping]
)

print(f"\nEğitim tamamlandı. En iyi model '{checkpoint_filepath}' konumuna kaydedildi.")