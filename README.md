## 🤖 Makine Öğrenimi Projelerim

Burada Google Colab üzerinde geliştirdiğim Makine Öğrenimi ve Derin Öğrenme projelerime ait bağlantıları ve kısa açıklamaları bulabilirsiniz.

### 1. Proje ING HUB Datathon: Müşteri Churn Tahmini (ANN + CatBoost)

**Açıklama:** Bu proje, **customers, customer_history, referance_date, referance_date_test, sample_submission** veri setlerini  kullanarak bir müşterinin verilen tarihte churn durumunu tahmin eden model geliştirilmiştir.Modle geliştirilmesinde ilk önce ANN daha sonrasında ise CatBoost algoritmaları kullanılmıştır.

* **💻 Koda Erişim (Google Colab):** [ING HUB Datathon Colab Defteri]((https://colab.research.google.com/drive/1iE571WS9NBXVlIJStHZQlcWKFlD5SDaB?usp=sharing))
* **📊 Dataset Notu;**
* **customer_history.csv**: Müşterilerin aylık olarak toplulaştırılmış işlem geçmişini **(EFT, kredi kartı harcamaları vb.)** içeren dosya.
**customers.csv**: Müşterilerin demografik bilgilerini **(yaş, cinsiyet vb.)** içeren dosya.
**reference_data.csv:** Modeli eğitmek için kullanılacak müşterilerin, hangi referans tarihinde **"kayıp" (churn)** olarak etiketlendiğini gösteren dosya.
**reference_data_test.csv**: Kayıp (churn) tahmini yapılması istenen test müşterilerinin referans bilgilerini içeren dosya.
**sample_submission.csv**: Yapılan tahminlerin yarışmaya **hangi formatta** gönderilmesi gerektiğini gösteren örnek dosya.

---

### 2. Proje Adı: Telekom Customer Churn Tahmini ANN(Artifical Neural Network)

**Açıklama:** Bu projede, **telekom_customer_churn.csv** veri setinde bulunan müşteri verileri ile churn durumu tahmin edilir.Tahmin yapılacak model ANN(Artifical Neural Network) seçilmiştir.

* **💻 Koda Erişim (Google Colab):** [Telekom Customer Churn Tahmini Colab Defteri](https://colab.research.google.com/drive/1UZly1_jvmYP_55tix05RCSW0eaCs5Z2z?usp=sharing)
* **📊 Dataset Notu:** **telekom_customer_churn.csv** veri setinde yer alan veriler kullanılarak müşterinin **churn** durumu tahmin edilmelidir.

---

### 3. Proje Adı: Kredi Durumu Tahmini

**Açıklama:** Veri setinde bulunan veriler ile kişiye kredi kartı verilip-verilmeyeceği tahmin edilecektir.Model Performans seçimi için Logistic Regression, K-Neearest Neighbors(K-NN), Support Vecotr Machine(SVM), Kernel SVM, Naive Bayes, Decision Tree Classifier, Random Forest Classifier, XGBoost, LGBM modelleri denenmiştir.

* **💻 Koda Erişim (Logistic Regression Google Colab):**([COLAB_PROJENIZIN_LINKI1](https://colab.research.google.com/drive/1yWg3rQzQfUi3Fr4L0x5hG_ZISOhZ8Q-P?usp=sharing))
* * **💻 Koda Erişim (K-Neearest Neighbors(K-NN) Google Colab):**([COLAB_PROJENIZIN_LINKI2](https://colab.research.google.com/drive/1REq7rIvTSSTlJx3JUN9YF0bCwVdOH4lU?usp=sharing))
* **💻 Koda Erişim (Support Vecotr Machine(SVM) Google Colab):** ([COLAB_PROJENIZIN_LINKI3](https://colab.research.google.com/drive/1FkwArdpGPeuVYJwj3UdG3n9p2tlI-zvg?usp=sharing))
* **💻 Koda Erişim (Kernel SVM Google Colab):** ([COLAB_PROJENIZIN_LINKI4](https://colab.research.google.com/drive/1sQufmh4dGfh0AdvSBsqfBAbTI7cicRv2?usp=sharing))
* **💻 Koda Erişim (Naive Bayes Google Colab):**([COLAB_PROJENIZIN_LINKI5](https://colab.research.google.com/drive/1CJKIIM6CAhG6mcJfSqWLPun2Kg97Am0s?usp=sharing))
* **💻 Koda Erişim (Decision Tree Classifier Google Colab):** [COLAB_PROJENIZIN_LINKI6](https://colab.research.google.com/drive/16YfTJXUkLLwAh1j5vuZF4p9y6fOSyK0e?usp=sharing)
* **💻 Koda Erişim (Random Forest Classifier Google Colab):** ([COLAB_PROJENIZIN_LINKI7](https://colab.research.google.com/drive/1ZXf7snIDopWzd0h72rTAvJOTzICENU6W?usp=sharing))
* **💻 Koda Erişim (XGBoost Google Colab):** ([COLAB_PROJENIZIN_LINKI8](https://colab.research.google.com/drive/1kH3UZFRbJqVD_Dl7ZSlWTQRlkBaOvzMV?usp=sharing))
* **💻 Koda Erişim (LGBM Google Colab):** ([COLAB_PROJENIZIN_LINKI9](https://colab.research.google.com/drive/1d8MbDPS3xfPlxHXGJzu1p_OkoZmu6Rjw?usp=sharing))

* **📊 Dataset Kaynağı:** [Loan Prediction Problem Dataset - Kaggle](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)
* **Dataset Notu:** Bu veri seti, bir finansal kuruluşun müşteri detaylarına (Gelir, Medeni Durum, Eğitim, Kredi Geçmişi vb.) dayanarak müşterinin kredi onay durumunu tahmin etmek için kullanılmıştır. Colab defterinde veriye doğrudan Kaggle API veya manuel yükleme ile erişim sağlanmıştır.
