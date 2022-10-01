import shutil
toplam_alan,kullanılmış_alan,kalan_alan=shutil.disk_usage("/")
print("Toplam Alan: %d GB"%(toplam_alan//(2**30)))
print("Kullanılmış Alan: %d GB"%(kullanılmış_alan//(2**30)))
print("Kalan Alan: %d GB"%(kalan_alan//(2**30)))