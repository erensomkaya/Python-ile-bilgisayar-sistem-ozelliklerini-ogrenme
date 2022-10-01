print ('----------------------RAM Bilgi Özeti----------------------')
print ('                                                                   ')
vvm=psutil.virtual_memory()
x=dict(psutil.virtual_memory()._asdict())
def forloop(): 
    for i in x: 
         print (i,"--",x[i]/1024/1024/1024)
forloop()


print ('                                                                   ')
print ('----------------------RAM Kullanım Özeti----------------------')
print ('                                                                   ')
print('Kullanılan RAM Yüzdesi :',psutil.virtual_memory().percent,'%')
print('Kullanılabilir Ram Yüzdesi :',psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,'%')