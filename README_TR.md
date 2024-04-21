
# BHBot 

[Этот файл доступен на Русском языке](README_RU.md) 

Brawlhalla için altın/XP tarım botu 

Büyük ölçüde [BrawlhallaEZ'den](https://github.com/jamunano/BrawlhallaEZ) ilham aldı 

### ------ -------------------------------------------------- ----------- 

### BOT AKTİF BİR ŞEKİLDE BAKILMAYA GERİ DÖNDÜ! 
###### Botun bakımına yardımcı olmak veya yeni özellikler eklemek için [Discord'a](https://discord.gg/2HDmuqqq9p "Discord") katılın! 

### ------------------------------------ --------------------- 

**UYARI:** Yazılım başlangıçta özel kullanım için geliştirilmiştir. 
Bu amaçla tasarlanmasa da, Mallhalla'da oyun içi para birimleri kullanılarak işlemlerin yürütülmesi de dahil olmak üzere öngörülemeyen sonuçlara yol açma potansiyeli vardır. 

**Geliştiriciler, bu yazılımın kullanımından doğabilecek her türlü zarara ilişkin hiçbir sorumluluk kabul etmez. Dikkatli bir şekilde ilerlemeniz ve yazılımı kendi takdirinize bağlı olarak kullanmanız tavsiye edilir.** 

(Bot, 18.04.2024 itibarıyla birden fazla kişi tarafından 3.000 saatten fazla sorun olmadan test edilmiştir) 

# Kurulum 
En son sürüm her zaman indirilebilir [buradan](https://github.com/Nick2bad4u/BHBot/releases) 

# Özellikler 

- Tamamen arka planda çalışır 
- Sizi rahatsız etmemek için girdileri doğrudan Brawlhalla'ya gönderir 
- Oyunu otomatik olarak başlatır 
- Lobiyi otomatik olarak oluşturur/ayarlar 
- Otomatik olarak seçer/değiştirir karakter ve oyun süresi 
- XP sınırını otomatik olarak algılar ve sıfırlar 
- Özel modları destekler 
- Özel dilleri destekler 
- Özel yazı tiplerini bile destekler 
- ~~Size kahve hazırlar~~ (şimdilik yalnızca çay desteklenmektedir) 

# Kullanım 
- Süreç sezgisel olacak şekilde tasarlanmıştır. "Ayarlar" düğmesini tıklayarak gerekli ayarları seçmeniz yeterlidir 
- Ayarlar kaydedildikten sonra, "Başlat" düğmesine tıklayarak programı başlatın. 

# Sınırlamalar 
- Bot, "Geçişleri daralt" seçeneğinin Evet olarak ayarlanmasını gerektirir. Otomatik olarak bu şekilde ayarlanması gerektiğini düşünüyorsanız lütfen [bir sorun açın](https://github.com/nick2bad4u/bhbot/issues) 
- Bot, oyun içi dilin İngilizce olarak ayarlanmasını gerektirir. Otomatik olarak bu şekilde ayarlanması gerektiğini düşünüyorsanız lütfen [bir sorun açın](https://github.com/nick2bad4u/bhbot/issues) 

# Teknik Genel Bakış 
- Temel kod her zaman herkes tarafından incelenebilir. 
- Temel olarak bot, girdileri doğrudan Brawlhalla penceresine iletmek için Windows SendMessage API'sini kullanıyor. Herhangi bir anda durumları ayırt etmek ve uygun eylemi belirlemek için piksel algılamayı kullanır.

- BrawlhallaBot sınıfı doğrudan kullanılabilir veya bunun için özel bir paketleyici geliştirebilirsiniz. Bağımsız olarak çalışacak şekilde tasarlanmıştır; gui.py, PySimpleGUI'yi kullanarak yalnızca grafiksel bir sarmalayıcı görevi görür.
