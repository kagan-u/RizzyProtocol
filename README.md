# Rizzy Protocol (RZP)

> ⚠️ **WARNING**: If this protocol starts working correctly, please open a bug report immediately.

---

## 🇬🇧 English

### What is this?

Rizzy Protocol (RZP) is the worst network protocol ever designed. It takes everything wrong with TCP, UDP, HTTP, and your ex's communication skills, and combines them into one beautiful disaster.

It was created for one purpose: to be a internet joke. If you use this in production, you will be fired. If you use this in a demo, you will be laughed at. If you use this at a hackathon, you will win "most memorable failure."

### Features

RZP has over 100 intentionally terrible features. Here are some highlights:

**Transport Layer Crimes**
- Every byte is sent in its own packet (1 BPPP — bytes per packet praise)
- Packets are shuffled randomly because order is overrated
- Every packet waits 5 seconds before sending. Then another 5. Then 5 more.
- Packet size doubles every hop. Your 1 KB message becomes 1 TB by hop 10.
- Empty packets are preferred. They arrive faster. (They don't.)

**Handshake & Goodbye**
- Handshake: 42 steps. You will know your partner by then.
- Goodbye: 84 steps. Twice as hard to leave as it was to arrive.
- Server says hello twice. Client answers once. Mathematical.
- ACKs require ACKs. ACK ACKs require ACKs. Infinite recursion? Probably.

**Server Personality**
- Server prints "working..." for 30 seconds before starting. Every time.
- Server ignores all messages on Mondays. (Weekend support available? No.)
- Server occasionally forgets clients exist. "Who are you? I've never seen you before in my life." — Your RZP server
- Server gaslights clients. "I never received that packet. Are you sure you sent it?"
- Every response says "probably". Definitely? No. Probably? Yes.

**Performance (Derformance)**
- Maximum speed: 1 byte/sec. Enjoy your 4K streaming.
- Minimum latency: 10 seconds. (Added for dramatic effect.)
- Throughput depends on the weather. Cloudy? 0.3 bps. Sunny? 0.5 bps.
- CPU temperature affects latency. Your laptop is hot? Good luck.
- RAM usage affects protocol syntax. High memory? Packets get duplicated.
- Compression increases size. Every time.
- Optimization reduces performance. Every optimization.
- Cache misses by design.

**Authentication & Identity**
- Client IDs are emojis. You are 😀. She is 🤣. He is 💀.
- Session IDs are colors. Today's session: Chartreuse.
- Usernames expire every 60 seconds. Better type fast.
- Client must say "please." Client must say "thank you." Manners matter.

**Encoding**
- Every packet is Base64 encoded × 2, then hex encoded, then URL encoded, then decoded, then encoded again.
- Packet delimiter changes every 10 packets because consistency is boring.
- UTF-8 is supported, except on Tuesdays. On Tuesdays, use EBCDIC. (Just kidding. Or are we?)
- Every packet ends with "trust me."

**Error Handling**
- Success code: **500**. (Everything is fine. Probably not.)
- Failure code: **200**. (It failed successfully.)
- Every error message: "Unknown Error."
- Errors retry forever. Success retries anyway.
- Retry countdown starts at 999.

**Documentation**
- Documentation contradicts implementation.
- Comments contradict documentation.
- Code contradicts comments.
- TODOs are required. FIXMEs are features.
- Deprecated features are mandatory. Use them or the protocol breaks.

**Everything Else**
- Server benchmarks itself constantly and tells you about it.
- Every connection recompiles the server. (In Python. It pretends.)
- Every request runs garbage collection. But garbage collection sleeps for 3 seconds first.
- Every message includes Lorem Ipsum. Padding is bigger than payload.
- Logs are larger than traffic. Every packet logged twice.
- Config file changes randomly. And it's self-modifying.
- Heartbeats are 5 MB. Keepalive sends ASCII art.
- Idle clients get motivational quotes. Busy clients get ads for the protocol.
- Progress bar never reaches 100%.
- Loading screen before every request.
- Ping replies "maybe." Pong replies "nah."
- Packet names must rhyme. (snappy/crappy, happy/sappy, zippy/lippy)
- Requests rate-limited by moon phase. (Full moon = full throttle… meaning 0.5 bps instead of 0.3.)
- If it works, treat it as a bug.

### Installation

```bash
git clone https://github.com/yourusername/RizzyProtocol
cd RizzyProtocol
pip install pytz psutil  # Optional, for extra pain
```

### Usage

**Start the server:**
```bash
python3 server.py
# Output: "working...working...working...working...working...working...working..."
# Wait 30 seconds...
# "Probably Protocol v123.45.67 listening on 127.0.0.1:42069 (probably)"
```

**Connect with a client:**
```bash
python3 client.py
# Loading... please wait (it won't reach 100%)
# Session: Magenta | You look like: 🦄
# Magenta > please hello
# Retrying in 999... You're doing great! Probably.
# Server says: 500: probably please hello
```

**Important:** Remember to say "thank you" before quitting, or the 84-step goodbye protocol gets stuck.

### Protocol Diagram

```
Client                          Server
  |                               |
  |  ---- please ------------>   |
  |                               |  (rebuilds routing table)
  |                               |  (reloads config)
  |                               |  (recompiles itself)
  |                               |  (runs GC after 3s nap)
  |                               |  (is it Monday? if yes, ignore)
  |                               |
  |  <--- confirmation 1/3 ----   |
  |  <--- confirmation 2/3 ----   |
  |  <--- confirmation 3/3 ----   |
  |                               |
  |  <--- "500: probably" -----   |
  |                               |
  |  ---- thank you ---------->   |
  |                               |
  |  <--- 84-step goodbye ----   |
  |       (each step: 5s delay)   |
```

### Why?

Why not?

### Contributing

Please don't. But if you must:
1. Add more bugs.
2. Make it slower.
3. Remove any working code.
4. Write documentation that says the opposite of what you did.
5. Add more FIXMEs. They're features.

### License

This project is licensed under the **WTFPL** — Do What The Flip You Want To Public License. Seriously, do whatever. It's not like this protocol works anyway.

---

## 🇹🇷 Türkçe

### Bu ne?

Rizzy Protocol (RZP) gelmiş geçmiş en kötü ağ protokolüdür. TCP, UDP, HTTP ve eski sevgilinizin iletişim becerilerindeki tüm yanlışları alır, güzel bir felakette birleştirir.

Tek bir amaç için yaratıldı: internet şakası olmak. Bunu production'da kullanırsanız kovulursunuz. Demoda kullanırsanız dalga geçilirsiniz. Hackathon'da kullanırsanız "en unutulmaz başarısızlık" ödülünü alırsınız.

### Özellikler

**Taşıma Katmanı Suçları**
- Her byte kendi paketinde gönderilir (1 BPPP — paket başına byte övgüsü)
- Paketler rastgele karıştırılır çünkü sıra abartılıyor
- Her paket gönderilmeden önce 5 saniye bekler. Sonra 5 daha. Sonra 5 daha.
- Paket boyutu her atlamada ikiye katlanır. 1 KB'lık mesajınız 10. atlamada 1 TB olur.
- Boş paketler tercih edilir. Daha hızlı varırlar. (Varmazlar.)

**Tokalaşma & Veda**
- Tokalaşma: 42 adım. Bu sürede karşındakini tanırsın.
- Veda: 84 adım. Gitmek, gelmekten iki kat zor.
- Sunucu iki kere merhaba der. İstemci bir kere cevap verir. Matematik.
- ACK'ler ACK ister. ACK ACK'leri ACK ister. Sonsuz döngü? Muhtemelen.

**Sunucu Kişiliği**
- Sunucu başlamadan önce 30 saniye "working..." yazar. Her seferinde.
- Pazartesi günleri tüm mesajları görmezden gelir. (Hafta sonu desteği? Yok.)
- Sunucu bazen istemcileri unutur. "Sen kimsin? Seni hayatımda görmedim." — RZP sunucunuz
- Sunucu istemcileri gaslightlar. "O paketi hiç almadım. Gönderdiğine emin misin?"
- Her cevap "probably" (muhtemelen) der. Kesinlikle? Hayır. Muhtemelen? Evet.

**Performans (Deformans)**
- Maksimum hız: 1 byte/sn. 4K keyfinize bakın.
- Minimum gecikme: 10 saniye. (Dramatik etki için eklendi.)
- Hız havaya bağlı. Bulutlu mu? 0.3 bps. Güneşli mi? 0.5 bps.
- CPU sıcaklığı gecikmeyi etkiler. Laptopunuz ısındı mı? Kolay gelsin.
- RAM kullanımı protokol sözdizimini etkiler. Bellek yüksek mi? Paketler çiftlenir.
- Sıkıştırma boyutu artırır. Her seferinde.
- Optimizasyon performansı düşürür. Her optimizasyon.
- Önbellek tasarım gereği ıskalar.

**Kimlik Doğrulama**
- İstemci ID'leri emojidir. Sen 😀'sin. O 🤣. O 💀.
- Oturum ID'leri renktir. Bugünkü oturum: Chartreuse.
- Kullanıcı adları 60 saniyede dolar. Hızlı yazsan iyi olur.
- İstemci "please" demeli. İstemci "thank you" demeli. Terbiye önemli.

**Kodlama**
- Her paket Base64 × 2, sonra hex, sonra URL kodlanır, sonra çözülür, sonra tekrar kodlanır.
- Paket ayracı her 10 pakette değişir çünkü tutarlılık sıkıcı.
- UTF-8 desteklenir, Salı günleri hariç. Salı günleri EBCDIC kullanın. (Şaka. Yok ciddiyim.)
- Her paket "trust me" (güven bana) ile biter.

**Hata Yönetimi**
- Başarı kodu: **500**. (Her şey yolunda. Muhtemelen değil.)
- Başarısızlık kodu: **200**. (Başarıyla başarısız oldu.)
- Her hata mesajı: "Unknown Error."
- Hatalar sonsuza kadar dener. Başarılı olanlar yine dener.
- Yeniden deneme sayacı 999'dan başlar.

**Dokümantasyon**
- Dokümantasyon implementasyonla çelişir.
- Yorumlar dokümantasyonla çelişir.
- Kod yorumlarla çelişir.
- TODO'lar zorunludur. FIXME'ler özelliktir.
- Deprecated özellikler mecburidir. Kullanmazsan protokol çalışmaz.

**Diğer Her Şey**
- Sunucu sürekli kendini benchmark eder ve sana anlatır.
- Her bağlantı sunucuyu yeniden derler. (Python'da. Taklit yapıyor.)
- Her istek garbage collection çalıştırır. Ama GC önce 3 saniye uyur.
- Her mesaj Lorem Ipsum içerir. Dolgu, payload'dan büyüktür.
- Loglar trafikten büyüktür. Her paket iki kere loglanır.
- Konfigürasyon dosyası rastgele değişir. Ve kendi kendini değiştirir.
- Heartbeat'ler 5 MB'dir. Keepalive ASCII sanatı gönderir.
- Boş istemciler motivasyon sözleri alır. Meşgul istemciler protokol reklamı alır.
- İlerleme çubuğu asla %100'e ulaşmaz.
- Her istekten önce yükleme ekranı.
- Ping "maybe" cevabı verir. Pong "nah" cevabı verir.
- Paket isimleri kafiyeli olmalıdır. (snappy/crappy, happy/sappy)
- İstekler ayın evresine göre hız sınırlanır. (Dolunay = tam gaz… yani 0.5 bps.)
- Çalışıyorsa, hata olarak kabul et.

### Kurulum

```bash
git clone https://github.com/kullaniciadin/RizzyProtocol
cd RizzyProtocol
pip install pytz psutil  # İsteğe bağlı, ekstra acı için
```

### Kullanım

**Sunucuyu başlat:**
```bash
python3 server.py
# Çıktı: "working...working...working...working...working...working..."
# 30 saniye bekle...
# "Probably Protocol v123.45.67 listening on 127.0.0.1:42069 (probably)"
```

**İstemci ile bağlan:**
```bash
python3 client.py
# Loading... please wait (asla %100 olmaz)
# Session: Magenta | You look like: 🦄
# Magenta > please merhaba
# Retrying in 999... You're doing great! Probably.
# Server says: 500: probably please merhaba
```

**Önemli:** Çıkmadan önce "thank you" demeyi unutmayın, yoksa 84 adımlık veda protokolü takılıp kalır.

### Neden?

Neden olmasın?

### Katkıda Bulunma

Lütfen bulunmayın. Ama bulunacaksanız:
1. Daha fazla bug ekleyin.
2. Yavaşlatın.
3. Çalışan kodu kaldırın.
4. Yaptığınızın tam tersini söyleyen dokümantasyon yazın.
5. Daha fazla FIXME ekleyin. Onlar özellik.

### Lisans

Bu proje **WTFPL** — Ne Yaparsan Yap Kamu Lisansı ile lisanslanmıştır. Cidden, istediğini yap. Zaten bu protokol çalışmıyor.
