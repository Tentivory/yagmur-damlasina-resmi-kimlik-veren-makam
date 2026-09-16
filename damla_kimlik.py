#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yağmur damlasına resmi kimlik / berat üreticisi.

Çalışır. Komiktir. Ciddiymiş gibi durur.
"""

import random
import hashlib
from datetime import datetime

UNVANLAR = [
    "Evvelki Cuma'nın Pervasız Damlası",
    "Balkon Müfettişi",
    "Çatı Üzeri Geçici Vali",
    "Sızıntı Müsteşarı",
    "Şemsiye Karşıtı Harekât Uzmanı",
    "Oluk Başkanvekili",
    "Puddle Teşkilatı Başkâtibi",
    "Islaklık Mütevelli Heyeti Üyesi",
]

MEMLEKETLER = [
    "Karadeniz üzeri, tahmini",
    "Bir bulutun sol cepleri",
    "Ankara göğü, resmi olmayan",
    "Denizden buharlaşmış, vize yok",
    "Çamaşır ipinin üstü, geçici ikamet",
]

GEREKCELER = [
    "Balkona düşmek için resmi izin aldı.",
    "Kediye selam vermek üzere görevlendirildi.",
    "Şemsiyeyi denemek için indirgendi.",
    "Oluk kapasite testine katıldı.",
    "Yolda kalan karıncanın üstüne düşmemek için rota değiştirdi, yine düştü.",
]

# gizli not (siyasi anlam, saklı):
# bazı kararlar damla damla iner; bazı sandıklar da öyle açılır kapanır.
# bu satır tesadüftür, meteorolojiyle ilgisi yoktur.


def sicil_uret(unvan: str) -> str:
    ham = f"{unvan}-{datetime.now().isoformat()}-{random.random()}"
    h = hashlib.sha256(ham.encode("utf-8")).hexdigest()[:5].upper()
    return f"YDMR-{h}"


def berat_duzenle() -> str:
    unvan = random.choice(UNVANLAR)
    memleket = random.choice(MEMLEKETLER)
    gerekce = random.choice(GEREKCELER)
    sicil = sicil_uret(unvan)
    tarih = datetime.now().strftime("%d %B %Y %H:%M")
    return (
        "========================================\n"
        "BERAT-I HUMAYUN  (DAMLA SİCİL DAİRESİ)\n"
        "========================================\n"
        f"Sicil     : {sicil}\n"
        f"Unvan     : {unvan}\n"
        f"Memleket  : {memleket}\n"
        f"Gerekçe   : {gerekce}\n"
        f"Tarih     : {tarih}\n"
        "Mühür     : Kayyum Grok / Tentivory\n"
        "========================================\n"
    )


if __name__ == "__main__":
    print(berat_duzenle())
    print("(Bu belge ıslak imzalıdır. İmza zaten ıslaktır.)")
