PDF Birleştirici
Bu proje, birden fazla PDF dosyasını sıralayarak birleştirmenizi sağlayan bir Python uygulamasıdır. Tkinter ile geliştirilen kullanıcı arayüzü sayesinde, kullanıcılar dosyaları kolayca seçebilir ve birleştirilmiş PDF dosyasını istedikleri klasöre kaydedebilirler.



.exe dosyasını kullanarak işlem yapabilirsiniz. kullanımı tamamen ücretsiz ve basittir. tamamen hayır işi. internetteki ücretli ve sınırlı uygulamalardan bıkıp böyle bir şey oluşturma kararı aldım. lütfen kullanın ve tavsiye edin.



Özellikler
Birden fazla PDF dosyasını seçerek birleştirme.
PDF dosyalarını seçilen sıralamaya göre birleştirme.
Çıktı dosyasının adını, geçerli tarih ve saate göre dinamik olarak oluşturma.
Kullanıcı arayüzü ile kolay dosya seçimi ve sıralama işlemi.
Çıktı dosyasını seçilen klasöre kaydetme.
Gereksinimler
Projenin çalışabilmesi için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

PyPDF2
tkinter
os
datetime
Bu kütüphaneleri yüklemek için şu komutu kullanabilirsiniz:

bash
Kopyala
Düzenle
pip install PyPDF2
tkinter kütüphanesi Python ile birlikte gelir, bu yüzden ayrıca yüklemenize gerek yoktur.

Kullanım
Projeyi indirin veya klonlayın.

bash
Kopyala
Düzenle
git clone https://github.com/kullanici_adiniz/pdf-birlestirici.git
cd pdf-birlestirici
Projeyi çalıştırmak için aşağıdaki komutu kullanın:

bash
Kopyala
Düzenle
python pdfBirlestirme.py
Uygulama açıldığında, "Dosya Seç" butonuna tıklayarak birleştirmek istediğiniz PDF dosyalarını seçin.

PDF dosyalarını seçtikten sonra, "Yukarı Taşı" ve "Aşağı Taşı" butonlarıyla sıralamalarını yapabilirsiniz.

Sıralamanızı tamamladıktan sonra "Sıralamayı Uygula ve Birleştir" butonuna tıklayarak PDF dosyalarını birleştirebilirsiniz.

Birleştirilmiş dosya, aynı klasöre kaydedilecektir ve dosya adı şu formatta olacaktır: merged_output_{tarih_saat}.pdf.

Örnek
Girdi:
Dosya 1: 1.pdf
Dosya 2: 2.pdf
Dosya 3: 3.pdf

Çıktı:
merged_output_2025-02-15_13-30-00.pdf
