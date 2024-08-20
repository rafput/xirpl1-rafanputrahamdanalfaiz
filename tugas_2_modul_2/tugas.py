class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
      
    def tambah(self):
        return self.angka1 + self.angka2
    
    def kurang(self): 
        return self.angka1 - self.angka2
    
    def kali(self): 
        return self.angka1 * self.angka2
    
    def bagi(self): 
        if self.angka2 != 0:
            return self.angka1 / self.angka2
        else:
            return "tidak bisa dibagi"
        
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

kalkulator = Kalkulator(angka1, angka2)

pilihan = input("Masukkan pilihan (tambah/kurang/kali/bagi): ")

if pilihan == "tambah":
    print ("hasil pilihan pertama", kalkulator.tambah())
elif pilihan == "kurang":
    print ("hasil pilihan kedua", kalkulator.kurang())
elif pilihan == "kali":
    print ("hasil pilihan ketiga", kalkulator.kali())  
elif pilihan == "bagi":
    print ("hasil pilihan keempat", kalkulator.bagi())
else:
    print ("error")
        
