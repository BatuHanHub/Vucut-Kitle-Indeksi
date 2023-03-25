# .exe olarak nasıl paketledim?
CMD veya terminal'i açıyoruz ve şu komutu giriyoruz `pip install pyinstaller`

İndirdikten sonra şimdi .py dosyamızı .exe olarak paketlemeye;

Windows Terminal'iniz varsa yazdığımız kodun olduğu yere sağ tıklayıp `Terminalde aç` menüsünü seçiyoruz ve Windows Terminal'imiz açılıyor. CMD kullanıyorsanız 
yazdığınız kodun olduğu yere gitmeniz gerekir. 

# Komutlar
`pyinstaller dosya_adi.py --onefile --noconsole --icon=icon_adi.ico` veya kısaca `pyinstaller dosya_adi.py` yazınız.

--onefile : paketlerken tek dosya halinde paketler. Yani `dist` klasöründe sadece programımızın exe hali durur. </br>
--noconsole : arkada planda konsolu gösterme. Eğer program konsolda çalışıyorsa bu komut gereksiz ve programız çalışır ama ekranda göstermez. </br>
--icon : program çalıştığında icon gösterir. Örneğin programın simgesini değiştiriyor. Bu komut kullanılmazsa kaset şeklinde yılan simgesi ile beraber gelir. </br>

# simge
![kasetli yılan](https://avatars.githubusercontent.com/u/1215332?s=200&v=4)
