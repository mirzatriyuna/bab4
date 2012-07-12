#deklarasi fungsi
def hasil(hours,rate):
    waktu = float(hours)
    bayar = float(rate)

    if waktu < 40:
       print float(waktu * bayar)
    else :
       normal = 40 * bayar	  #menampung perkalian rate sebanyak 40 hours
       lebih = waktu - 40	  #menampung banyaknya hours yang lebih dari 40
       bayarLebih = (bayar*3/2) * lebih
       akhir = normal + bayarLebih		#hasil akhir
       print ('pay :'), float(akhir)

#input pertama
hours = raw_input('Enter Hours : ')
#pengecekan inputan pertama
try:
   waktu = int(hours)
except:
   print ('Error, please enter numeric input')
#input kedua
rate = raw_input('Enter Rate : ')
#pengecekan inputan kedua
try:
   bayar = int(rate)
except:
   print ('Error, please enter numeric input')

#pemanggilan fungsi
hasil(hours,rate)
