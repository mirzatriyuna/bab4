#deklarasi fungsi
def hasil(masukan):
    score = float(masukan)
    #logika fungsi grade
    try:
      score = float(masukan)
      if score >= 1.0:
        print 'Bad Score'
      elif score >= 0.9:
        print 'A'
      elif score >= 0.8:
        print 'B'
      elif score >= 0.7:
        print 'C'
      elif score >= 0.6:
        print 'D'
      elif score < 0.6:
        print 'E'

    except:
      print 'Bad Score'


#info bagi user
print 'Score	Grade'
print '>=0.9	A'
print '>=0.8	B'
print '>=0.7	C'
print '>=0.6	D'
print ' <0.6	F'

#meminta user memasukkan score
masukan = raw_input('Enter score : ')
#pemanggilan fungsi
hasil(masukan)

