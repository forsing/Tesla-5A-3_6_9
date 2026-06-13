"""
Tesla 5A - 3-6-9 slojeviti motor.
"""


import numpy as np

from Tesla_5_common import (
    BAZA_HZ,
    MNOZIOCI,
    PIRAMIDA,
    ZLATNI_ODNOS_INV,
    fokusni_omotac,
    normalizuj_signal,
    izvod_polja,
    ispisi_i_snimi_model,
)

OSNOVA = "tesla_369_5A"


def simuliraj_5a(nx):
    x = np.linspace(0.0, 1.0, nx)

    # 3f0 je sirok stabilizacioni omotac, 6f0 nosi vezu, 9f0 ostro fokusira centar.
    slojevi = [
        (3, 1.00, 0.34, "3f0 stabilizacija"),
        (6, ZLATNI_ODNOS_INV, 0.22, "6f0 nosilac/modulator"),
        (9, ZLATNI_ODNOS_INV ** 2, 0.12, "9f0 fokus/scalar shell"),
    ]
    s = np.zeros(nx)
    for m, amp, sigma, _ in slojevi:
        s += amp * fokusni_omotac(x, sigma=sigma) * np.sin(2.0 * np.pi * m * PIRAMIDA * x)

    s = normalizuj_signal(s)
    e_x = izvod_polja(x, s)
    detalji = {
        "izvor": "main_controller + tesla_369_layering_logic",
        "baza_hz": BAZA_HZ,
        "mnozioci": MNOZIOCI,
        "piramida": PIRAMIDA,
        "slojevi": ", ".join(naziv for _, _, _, naziv in slojevi),
    }
    return x, s, e_x, detalji


def main():
    ispisi_i_snimi_model(
        OSNOVA,
        "Tesla Scalar - GRUPA 5A / 3-6-9 slojeviti motor",
        simuliraj_5a,
        "Model koristi razdvojene uloge 3f0, 6f0 i 9f0 sloja.",
    )


if __name__ == "__main__":
    main()



"""
Slika talasa: /Tesla/tesla_369_5A.png
Slika talasa: /Tesla/tesla_369_5A.jpg

Tesla Scalar - GRUPA 5A / 3-6-9 slojeviti motor
CSV: /data/loto7hh_4632_k47.csv | Izvlacenja: 4632 | tezine: talas=0.7 freq=0.3
max S: 1.0000000000 | max |E_x|: 833.1798664130

Brojevi po kombinovanom skoru (tezinski talas + frekvencija):
  26  skor=0.8905679844  freq=0.02680  (pojava=869)
  37  skor=0.7795802909  freq=0.02652  (pojava=860)
  30  skor=0.7434482759  freq=0.02427  (pojava=787)
  35  skor=0.7167527233  freq=0.02600  (pojava=843)
  08  skor=0.7045280839  freq=0.02810  (pojava=911)
  09  skor=0.6907922540  freq=0.02600  (pojava=843)
  14  skor=0.6873840795  freq=0.02495  (pojava=809)
  12  skor=0.6741448556  freq=0.02498  (pojava=810)
  39  skor=0.6499690947  freq=0.02618  (pojava=849)
  13  skor=0.6330816750  freq=0.02554  (pojava=828)
  21  skor=0.6147049284  freq=0.02551  (pojava=827)
  05  skor=0.5902007561  freq=0.02554  (pojava=828)
  31  skor=0.5868830135  freq=0.02560  (pojava=830)
  36  skor=0.5822771181  freq=0.02424  (pojava=786)
  38  skor=0.5822156666  freq=0.02597  (pojava=842)
  27  skor=0.5747693907  freq=0.02433  (pojava=789)
  11  skor=0.5630028165  freq=0.02655  (pojava=861)
  28  skor=0.5600765700  freq=0.02532  (pojava=821)
  23  skor=0.5563248502  freq=0.02791  (pojava=905)
  18  skor=0.5499748433  freq=0.02532  (pojava=821)
  22  skor=0.5209706360  freq=0.02625  (pojava=851)
  04  skor=0.5091736684  freq=0.02504  (pojava=812)
  10  skor=0.5029886217  freq=0.02606  (pojava=845)
  29  skor=0.4949891942  freq=0.02618  (pojava=849)
  02  skor=0.4936873528  freq=0.02544  (pojava=825)
  19  skor=0.4682203204  freq=0.02510  (pojava=814)
  03  skor=0.4637248499  freq=0.02547  (pojava=826)
  16  skor=0.4580159664  freq=0.02581  (pojava=837)
  32  skor=0.4284888856  freq=0.02643  (pojava=857)
  25  skor=0.4223286321  freq=0.02591  (pojava=840)
  33  skor=0.4190832409  freq=0.02634  (pojava=854)
  15  skor=0.4012360244  freq=0.02461  (pojava=798)
  01  skor=0.3804051493  freq=0.02430  (pojava=788)
  20  skor=0.3566476471  freq=0.02375  (pojava=770)
  06  skor=0.2925433366  freq=0.02517  (pojava=816)
  24  skor=0.2910014289  freq=0.02591  (pojava=840)
  34  skor=0.2360851208  freq=0.02692  (pojava=873)
  17  skor=0.2185544475  freq=0.02362  (pojava=766)
  07  skor=0.1613793103  freq=0.02603  (pojava=844)

Predlozene kombinacije (rangirane po skoru kombinacije):
  01. 04 05 11 23 27 30 37  skor_komb=4.3165000486
  02. 08 14 16 22 26 31 32  skor_komb=4.2768386493
  03. 08 13 15 26 27 31 33  skor_komb=4.2101494128
  04. 05 11 12 18 32 35 39  skor_komb=4.1725339750
  05. 09 10 19 22 27 31 38  skor_komb=3.9268399029
  06. 07 10 13 21 29 30 39  skor_komb=3.8005611002
  07. 16 18 20 24 28 37 39  skor_komb=3.6452658414
  08. 02 11 20 23 31 33 39  skor_komb=3.6255980157
  09. 01 05 09 13 20 34 39  skor_komb=3.5371816969
  10. 07 08 13 21 23 25 32  skor_komb=3.5208363655

Sacuvano: /Tesla/tesla_369_5A.txt
"""




"""
Analiza Tesla_369_5A.py
Tesla_369_5A.py je slojevita verzija 3-6-9 modela. 
Za razliku od osnovnog Tesla_369_5.py, ovde 3, 6 i 9 nisu samo sabrani ravnopravno, nego svaki sloj ima posebnu ulogu, jačinu i širinu fokusa.

Osnovna ideja je harmonijsko raslojavanje:
3f0 = stabilizacioni sloj
6f0 = nosilac/modulator
9f0 = fokus / scalar shell
3-6-9 ne tretira samo kao zbir frekvencija, nego kao tri funkcionalna nivoa.

sinusni talas za svaki sloj
Gaussov fokusni omotač za koncentraciju oko centra
zlatni odnos 0.618 za smanjenje jačine viših slojeva
gradijent polja E_x = -dS/dx
energiju polja kasnije kroz zajednički pipeline
ne-frekvencijski talasni raspored preko istorije izvlačenja 

Funkcija simuliraj_5a(nx) pravi prostor x dužine koliko ima izvlačenja u CSV-u.

Zatim definiše tri sloja:
3f0: amplituda 1.00, sigma 0.34
6f0: amplituda 0.618, sigma 0.22
9f0: amplituda 0.618², sigma 0.12

To znači:
3f0 je najširi i najjači, kao stabilizaciona osnova.
6f0 je srednji sloj, modulator.
9f0 je najuži i najslabiji po amplitudi, ali najviše fokusiran oko centra.

Za svaki sloj računa:
amp * fokusni_omotac(x, sigma) * sin(2π * m * 21 * x)
Zatim sabira sva tri sloja, normalizuje signal i računa E_x.

Posle toga ne radi sam skoriranje ručno, 
nego poziva zajednički ispisi_i_snimi_model() iz Tesla_5_common.py, koji radi ostatak: loto skor, frekvencije, kombinacije, txt i slike.

Slojevita 3-6-9 superpozicija
Nisu svi harmonici jednaki. Svaki ima drugačiju funkciju.

Fokusni Gaussov omotač po sloju
3f0 širok, 6f0 srednji, 9f0 uzak. To daje „koncentrično” talasno polje.

Zlatni odnos 0.618
Viši slojevi se skaliraju sa 0.618 i 0.618². To sprečava da 9f0 potpuno preuzme signal i daje uređen pad jačine.

21 ciklus/piramida
PIRAMIDA = 21 iz zajedničkog fajla. Svaki sloj koristi m * 21, pa se celim prostorom prostire 3/6/9 struktura u odnosu na 21 jedinicu.

Zajednički pipeline
5A samo proizvodi talas. Skoriranje, frekvencija, izbor kombinacija i slike dolaze iz Tesla_5_common.py.

5A je sada jedan od šest ulaza u grupu 5:
5 + 5A + 5B + 5C + 5D + 5E -> Tesla_5final.py
Njegova uloga je da predstavlja čistu slojevitu 3-6-9 logiku, dok drugi modeli grupe 5 pokrivaju drift, geometriju, senzore i closed-loop korekciju.

Top 10 za 5A:
26, x, 30, y, 08, z, 14, x, 39, 13

Predlozene Top kombinacije (rangirane po skoru kombinacije):
04 x 11 y 27 z 37  skor_komb=4.3165000486

U odnosu na osnovni 5, 5A više podiže 37, 35, 08, 09, 12, što znači da slojeviti model daje drugačiji talasni raspored. To je korisno jer donosi dodatni signal u 5final, a ne samo kopiju osnovnog 3-6-9 modela.
"""



"""
source ~/tesla_env/bin/activate

Bitne verzije za tesla_env:

Paket	Verzija
python  3.11.13
numpy   2.2.6
scipy   1.15.3
pandas  3.0.3
matplotlib    3.10.9
k-Wave-python 0.6.2
pycharge      2.0.1
jax        0.10.1
jaxlib     0.10.1
jaxtyping  0.3.7
equinox    0.13.8
lineax     0.1.1
optimistix 0.1.0
ml-dtypes
(uz jax)
opencv-python 4.13.0.92
h5py          3.16.0
"""

