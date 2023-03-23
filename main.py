# Kütüphaneler eklendi {
from tkinter import * # GUİ yani Grafiksel Kullanıcı Arayüzü 
from tkinter import messagebox # Grafiksel Kullanıcı Arayüzüne 'messagebox' kolu eklendi. 
# Messagebox: kullanıcıya hata göstermek, bilgi vermek, uyarı vermek, evet hayır sorusu vb. soruları soran bir Tkinter'da bulunan ek işlev
# }

# 18.5'in altındaki VKİ: Zayıf
# 18.5 - 24.9 arası VKİ: Normal
# 25 - 29.9 arası VKİ: Fazla kilolu
# 30 - 34.9 arası VKİ: Obez (Tip 1)
# 35 - 39.9 arası VKİ: Obez (Tip 2)
# 40 ve üzeri VKİ: Aşırı obez (Tip 3)

def hesapla(): # Düğme için fonksiyon oluşturuldu
    global kilogramEnt, boyEnt, VuKiIn # Local -> Global
    VuKiIn.configure(state='normal') # Çıktı 'normal' yaptı çünkü çıktı 'readonly' yani sadece okunabilir ama bunu 'normal' yaparak üzerine yazı yazılabilir hale getirdim
    VuKiIn.delete(0, END) # İçerik temizlendi
    kilogramEntInt = int(kilogramEnt.get()) # Kullanıcının girdiği kilo, KilogramEntInt değişkenine integer olarak geçirildi    
    boyEntFlt = float(boyEnt.get()) # Kullanıcının girdiği boy, boyEntFlt değişkenine float olarak geçirildi 
    
    indeks = kilogramEntInt / (boyEntFlt*boyEntFlt) # İşlem yapılıyor
    indeks = str(indeks) # indeks string değerine geçirildi
    
    VuKiIn.insert(END, indeks) # İndeks çıktıya basıldı
    VuKiIn.configure(state='readonly') # Kullanıcı çıktıyı dokunmasın diye 'readonly' olarak değiştirildi
    
    indeks = float(indeks) # İndeks yine float olarak değiştirildi
    
    if indeks < 18.5:
        messagebox.showwarning('UYARI!',f'''Çok zayıfsınız. Lütfen VKİ(Vücut Kitle İndeksi) 18.5-24.9 arasında yapabilmeniz için -{18 - indeks}- değer daha yükseltmeniz gerekmektedir. \n
VKİ değerinizi yükseltmek için doktorunuza başvurabilir veya spor yaparak ve sağlıklı beslenebilirsiniz.''')

    elif indeks >= 18.5 and indeks <= 24.9:
        messagebox.showinfo('SAĞLIKLI','VKİ değerleriniz normal.')
        
    elif indeks >= 25.0 and indeks <= 29.9:
        messagebox.showerror('UYARI!',f'''Kilolusunuz. Lütfen VKİ(Vücut Kitle İndeksi) 18.5-24.9 arasında yapabilmeniz için -{18 - indeks}- değer daha düşürmeniz gerekmektedir. \n
VKİ değerinizi düşürmek için doktorunuza başvurabilir veya spor yaparak ve sağlıklı beslenebilirsiniz.''')

    elif indeks >= 30.0 and indeks <= 34.9:
        messagebox.showwarning('DİKKAT!',f'''1.TİP obezsiniz. Lütfen VKİ(Vücut Kitle İndeksi) 18.5-24.9 arasında yapabilmeniz için -{18 - indeks}- değer daha düşürmeniz gerekmektedir. \n
VKİ değerinizi düşürmek için doktorunuza başvurabilir veya spor yaparak ve sağlıklı beslenebilirsiniz.''')
        
    elif indeks >= 35.0 and indeks <= 39.9:
        messagebox.showwarning('DİKKAT!',f'''2.TİP obezsiniz. Lütfen VKİ(Vücut Kitle İndeksi) 18.5-24.9 arasında yapabilmeniz için -{18 - indeks}- değer daha düşürmeniz gerekmektedir. \n
VKİ değerinizi düşürmek için doktorunuza başvurabilir veya spor yaparak ve sağlıklı beslenebilirsiniz.''')
    
    else:
        messagebox.showwarning('DİKKAT!',f'''3.TİP obezsiniz. Lütfen VKİ(Vücut Kitle İndeksi) 18.5-24.9 arasında yapabilmeniz için -{18 - indeks}- değer daha düşürmeniz gerekmektedir. \n
VKİ değerinizi düşürmek için doktorunuza başvurabilir veya spor yaparak ve sağlıklı beslenebilirsiniz.''')

  
# Pencere özelleştirme {
pencere = Tk() # pencere değişkeni oluşturuldu ve Pencere, pencere değişkenine atıldı. 
pencere.title('Vücut Kitle İndeksi') # Başlık
pencere.geometry('600x400') # Boyut
pencere.resizable(width=False,height=False) # Kullanıcının pencerenin boyutuna dokunmasını engelledim
# }

# Frame oluşturdum ve yerleştirdim {
# Oluşturuldu
baslikFrame = Frame(pencere)
kilogramFrame = Frame(pencere) 
boyFrame = Frame(pencere)
hesaplaFrame = Frame(pencere) 

# Yerleştirildi
baslikFrame.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.20)
kilogramFrame.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.10)
boyFrame.place(relx=0.05,rely=0.5,relwidth=0.9,relheight=0.10)
hesaplaFrame.place(relx=0.1,rely=0.7,relwidth=0.9,relheight=0.10)
# }

# Pencere içeriği (düğmeler, yazılar, input[girdi] alanı vs.) {
    
### Başlık ###
baslik = Label(baslikFrame, text='Vücut Kütle İndeksi', font=('arial 40 bold'))
baslik.pack(side=BOTTOM)
###

### Kilogram ###
kilogramYazi = Label(kilogramFrame, text='Kilonuz :', font=('arial 25 bold')).pack(side='left')
kilogramEnt = Entry(kilogramFrame, font=('arial 25 bold'), width=5)
kilogramEnt.pack(side='left')
###

### Boy ###
boyYazi = Label(boyFrame, text='Boyunuz (x.xx):', font=('arial 25 bold')).pack(side='left')
boyEnt = Entry(boyFrame, font=('arial 25 bold'), width=5)
boyEnt.pack(side='left')
### 

### Düğme ###
hesaplaButton = Button(hesaplaFrame, text='Hesapla', font=('arial 25 bold'), command=hesapla).pack(side='left')
###

### Sonuç ###
VuKiIn = Entry(hesaplaFrame, font=('arial 25 bold'), state='readonly')
VuKiIn.pack(padx=0.1)
###

# }

pencere.mainloop() # Pencere hemen kapanmasın diye döngüye soktum
