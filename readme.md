# WhatsApp Durum İzleyici

Bu Python betiği, Selenium ve BeautifulSoup kütüphanelerini kullanarak WhatsApp web istemcisindeki kişilerin çevrimiçi durumunu izler ve Telegram üzerinden bildirim gönderir.

## Gereksinimler

- Python 3.x
- Selenium
- BeautifulSoup
- requests

## Kurulum

1. Proje dosyalarını bir dizine indirin veya klonlayın.
2. İstenirse, bir sanal ortam oluşturun ve aktifleştirin.
3. Gerekli Python paketlerini yükleyin.
4. `main.py` dosyasını düzenleyin ve aşağıdaki satırlardaki Telegram bot tokenini (`TOKEN`) ve kullanıcı kimliğini (`USER_ID`) güncelleyin. Bot oluşturma ve kimlik almak için [Telegram Bot API Dokümantasyonu](https://core.telegram.org/bots/api)na başvurun.

   ```python
   # Telegram bot token ve kullanıcı kimliği
   TOKEN = "..."
   USER_ID = "..."

## Chrome web tarayıcısı için uygun sürümde WebDriver'ı indirin ve sisteminize kurun. WebDriver'ı PATH'e eklemeyi unutmayın.
Uygulamayı başlatın.
Kullanın
WhatsApp web istemcisinde oturum açın.
Uygulamayı çalıştırın.
Kişilerin çevrimiçi durumu takip edilecektir. Durum değişiklikleri Telegram üzerinden bildirim olarak gönderilecektir.
