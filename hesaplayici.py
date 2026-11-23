# Sosyal Medya Etkileşim Oranı Hesaplayıcı

# Kullanıcıdan girdilerin alınması ve tür dönüşümleri (str, int, float)
hesap_adi: str = input("Sosyal medya hesap adını giriniz: ")
takipci_sayisi: int = int(input("Toplam takipçi sayısını giriniz: "))
begeni_sayisi: int = int(input("Gönderinin beğeni sayısını giriniz: "))
yorum_sayisi: int = int(input("Gönderinin yorum sayısını giriniz: "))
paylasim_sayisi: int = int(input("Gönderinin paylaşım sayısını giriniz: "))
hedef_oran: float = float(input("Hedef etkileşim oranını (%) giriniz (örn. 3.5): "))

# Aritmetik operatörler ile etkileşim oranının hesaplanması
etkilesim_orani: float = ((begeni_sayisi + yorum_sayisi + paylasim_sayisi) / takipci_sayisi) * 100

# Karşılaştırma operatörü ile hedefin tutturulup tutturulmadığının kontrolü (bool)
hedef_basarili_mi: bool = etkilesim_orani >= hedef_oran

# Biçimli çıktı (f-string) ile sonuçların raporlanması
print("\n--- Etkileşim Analiz Raporu ---")
print(f"Hesap Adı: @{hesap_adi}")
print(f"Takipçi Sayısı: {takipci_sayisi}")
print(f"Hesaplanan Etkileşim Oranı: %{etkilesim_orani:.2f}")
print(f"Hedef Oran (%{hedef_oran:.2f}) Aşıldı mı?: {hedef_basarili_mi}")
