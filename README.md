Ödevin Konusu:
Bu ödevde amaç, Bézier eğrileri ile çalışmayı öğrenmek ve bu eğrileri animasyon ve fiziksel etkileşimlerle geliştirebilmektir. Öğrenciler, kontrol noktalarını sürükleyerek eğriyi değiştirebilecek, eğri boyunca hareket eden bir animasyon oluşturabilecek ve dış kuvvetler (rüzgar ve yerçekimi gibi) uygulayarak etkileşimli bir grafik programı geliştireceklerdir.
Teorik Giriş:
Bézier eğrileri, bilgisayar grafiklerinde sıkça kullanılan parametrik eğrilerdir. Bu eğriler, genellikle animasyon, şekil modelleme, vektör grafikler ve yol planlama gibi alanlarda kullanılır. Bézier eğrileri, kullanıcı tarafından tanımlanan kontrol noktaları ile oluşturulur. Bu kontrol noktaları, eğrinin şeklini ve yönünü belirler ve her t değeri için bir (x, y) koordinatı hesaplanarak çizilebilir.
Bir kübik Bézier eğrisi (4 kontrol noktasıyla tanımlanan eğri), şu matematiksel denklemle ifade edilir: 𝐟𝐟(𝑡𝑡)= (1−𝑡𝑡)3𝐏𝐏𝟎𝟎+ 3(1−𝑡𝑡)2𝑡𝑡𝐏𝐏𝟏𝟏+ 3(1−𝑡𝑡)𝑡𝑡2𝐏𝐏𝟐𝟐+ 𝑡𝑡3𝐏𝐏𝟑𝟑
Görevler (ve puanlama):
1. Bézier Eğrisi Uygulaması (%20):
o Dört kontrol noktası kullanarak bir kübik Bézier eğrisi oluşturun.
o Kullanıcıların fareyle kontrol noktalarını sürükleyip yeniden konumlandırmasını sağlayın.
o Kontrol noktaları her değiştiğinde eğriyi gerçek zamanlı olarak yeniden çizdirin.
o Oluşturulan eğriyi dinamik olarak ekrana çizdirin.
2. Animasyon Modu (%25):
o Eğri üzerinde bir daireyi 0 ile 1 arasında değer alan bir parametre (t) yardımı ile hareket ettirecek bir animasyon oluşturun.
o Daire eğri boyunca hareket ederken:
• Toplam kat edilen mesafeyi hesaplayın ve ekranda gösterin.
o Kullanıcı için aşağıdaki kontrol düğmelerini ekleyin:
• Oynat: Animasyonu başlatır.
• Durdur: Animasyonu durdurur.
• Sıfırla: Animasyonu ve kontrol noktalarını başlangıç durumuna döndürür.
3. Kuvvetler Modu (%30):
o Kontrol noktalarına dış kuvvetler uygulayın (örneğin rüzgar ve yerçekimi):
• Rüzgar Hızı: Kaydırma çubuğu ile kontrol edin.
• Rüzgar Yönü: Açılır menü ile ayarlayın.
• Yerçekimi Kuvveti: Kaydırma çubuğu ile ayarlayın.
o Kullanıcının tüm kuvvetleri sıfırlayabilmesi için bir "Kuvvetleri Sıfırla" düğmesi ekleyin. Bu düğme:
• Kontrol noktalarını başlangıç konumlarına döndürmelidir.
• Rüzgar ve yerçekimi kuvvetlerini sıfırlamalıdır.
o Kullanıcıdan alınan kuvvet değerlerine göre eğriyi dinamik olarak yeniden çizdirin.
4. Ekstra Zorluklar (Bonus Puan – Kişisel Yaratıcılık Bölümü) (%15):
o Sürtünme kuvveti ekleyerek hareketin direncini simüle edin.
o Rüzgar yönü ve yerçekimi için görsel göstergeler oluşturun.
o Kendiniz farklı etki dağılımına sahip farklı dış kuvvet(ler) tanımlayabilir ve/veya t değerinin değişimini manipüle edebilirsiniz, böylece ilginç/etkileyici animasyonlar oluşturabilirsiniz.
5. Raporlama ve Kodun Açıklaması (%10):
o Kodun ve elde edilen sonuçların açıklanması, her bir adımda yapılan işlemlerin teorik ve pratik yönleriyle anlatılması.
Ödev Teslimi:
• Ödev, Bezier eğrisi oluşturma sürecini ve sonuçları açıklayan kısa bir rapor, JavaScript/MATLAB/Python veya başka bir uygun dilde yazılmış kodlar şeklinde teslim edilmelidir.
• Raporda, her bir adımın nasıl gerçekleştirildiği ve elde edilen sonuçların açıklaması detaylı bir şekilde verilmelidir.
Son teslim tarihi: 10/12/2024 saat 23:59
Önemli Not: Ödevler bireysel yapılmalı ve bireysel teslim edilmelidir. Geciken ödevlerde her gün başına %10 kesinti yapılır ve 13/12/2024 saat 23:59dan sonra yükleme yapılamaz. Benzer ödevler değerlendirme dışı bırakılır.
