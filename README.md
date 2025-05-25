# Nokia Hackathon (early 2025)

**Általános információk:**

Minden feladatnak megvan a saját „munkaterülete” (workspace), saját feladatmappája. Kérjük, maradjatok ezekben a mappákban, amikor a megoldásokon dolgoztok. Ha valamilyen dependency-re szükségetek van, írjátok a _requirements.txt_ fájlba, és az automatikusan telepítve lesz, ha nem üres.
A pontokat először az alapján adjuk, hogy a feladatok helyesen és teljesen vannak-e megoldva. Ezután a megvalósítást, a funkcionalitást, a kód szépségét és olvashatóságát is figyelembe vesszük. Több fájlban is dolgozhattok, és használhattok absztrakciót is. A pontozásnál a ötödik feladat nehezebb, ezért ez dupla pontot ér.

Mappastruktúra:

- _input.txt_
- _main.py_, amely az automatizált tesztfuttató fő belépési pontja. Kérjük, ne távolítsátok el ezt a fájlt, és ne legyenek benne kötelező paraméterek. Kérjük, minden feladat megoldását printeljétek ki a console-ra.

**Figyelem:**

- A megoldások futási ideje nem haladhatja meg az 5 másodpercet. Ha egy kód ennél tovább fut, automatikusan leállítjuk.
- Figyeljetek arra, hogy ne módosítsátok a .github mappát.
- Ne nevezzétek át és ne töröljétek a main.py fájlt.
- A leaderboard nem a végleges állást mutatja, csak a szórakoztatás céljából van ott, a százalékos egyezés sem feltétlenül tükrözi a végső eredményt. Minden megoldást egyénileg végig nézünk és pontozunk a fentiekben meghatározottak alapján. 

---

## 1. Dobókocka intervallum

**Feladatmappa:**

`dice_range_expression`

### Leírás:

Képzeld el, hogy egy fantasy játékot tervezel, ahol minden véletlenszerű eseményt dobókockával kell eldönteni – pont úgy, mint a Dungeons & Dragons játékokban! A feladatod, hogy két egész számmal jelölt számintervallumot (pl. `2` és `5` között) kifejezz szabványos dobókockák kombinációjával és szükség esetén egy eltolással (pl.: `-2`, `+1`).

Elérhető dobókockák: `d20`, `d10`, `d8`, `d6`, `d4`, `d3`, `d2` - A számértékek a kockák oldalszámát mutatják: pl. d10 egy tízoldalú dobókockát jelöl. A d2 egy pénzérmének felel meg.

Minden „dX” dobás 1 és X közötti értéket ad vissza. Például 1d6 azt jelenti, hogy egy darab hatoldalú kockával dobsz egyszer, a kidobható érték pedig 1 és 6 között lesz, inkluzívan.

### Bemenet:

* `min_val`: legkisebb dobási eredmény (egész szám)
* `max_val`: legnagyobb dobási eredmény (egész szám)

### Kimenet:

* Egy string, amely dobókockák kombinációjával írja le az adott tartományt.
* A cél: a lehető legkevesebb kocka használata, eltolás csak ha szükséges.

### Példa:

***input.txt***

```
2 5
1 23
```

***console printout:***

```
1d4+1
1d4+1d20-1
```

---

## 2. Fibonacci

**Feladatmappa:**

`fibonacci`

### Leírás:

A feladat egy olyan program elkészítése, amely kiírja az összes **3-mal osztható Fibonacci-számot** 0-tól N-ig.

### Bemenet:

* Egy egész szám (`N`)
* Ha a bemenet nem értelmezhető (pl. nem szám), vagy nincs egyetlen megoldás sem: `N/A`

### Kimenet:

* Az összes `X` Fibonacci-szám, amelyre `0 <= X <= N` és `X % 3 == 0`
* A számok **vesszővel és szóközzel** elválasztva jelenjenek meg

### Példa:

***input.txt***

```
10
100
1000
```

***console printout:***

```
0, 3
0, 3, 21
0, 3, 21, 144, 987
```

---

## 3. Jelek

**Feladatmappa:**

`signals`

### Leírás:

Feladatod hogy dekódold két ellenséges bázis közötti rádió kommunikációt. Belehallgatva a rádióadásukba, rövid csipogásokat hallasz és egy rövid szünetet egy-egy adag csipogás között. Úgy tűnik ez egy kód, gyorsan fel is jegyezted a hallottakat amelyek a következők: 3.4 (3 csipogás, majd egy rövid szünet, majd 4 csipogás) 2.1.2.4 (2 csipogás, 1 csipogás, 2 csipogás, 4 csipogás)

A kódokat minden nap reggelén közvetítik. A nap folyamán történteket is feljegyezted: jelek = [“3.4”, “2.1.2.4”] esemenyek = [“A”, “B”] (Tudjuk, hogy "3.4" és "2.1.2.4" biztosan az "A" és "B" eseményhez köthetőek, de nem tudjuk melyik kód melyik eseméynt jelenti.)

Több napnyi kód összehasonlításával meg tudod fejteni a kódokat; a megoldás pedig így néz ki. decoded = {“3.4”: “B”, “2.1.2.4”: “A”}

Továbbá: - Több napnyi jeleket és eseményeket fogsz kapni, melyeket fel kell majd dolgoznod. - Minden kód csak egy eseményt jelenthet, viszont egy eseménynek lehet több különböző kódja is. - Mindig lesz elegendő információ a feladat megoldásához.

### Bemenet:

A bemenet egy lista lesz, amelyben minden egyes napot egy-egy tuple fog reprezentálni. Egy adott naphoz tartozó tuple-ben lesz két lista: 
* Az első lista tartalmazza az adott nap reggelén hallott kódokat mint string-ek (pl.: ["5", "3.4", "2.1.2.4"])
* A második listában pedig az adott nap eseményei lesznek mint betűk (pl.: ["A", "B", "O", "I"])

### Kimenet:

A programnak az adott lista bemenetre ki kell írnia a megfejtést egy dictionary-be rendezve a következő péda szerint. Fontos, hogy a ditonary kulcsaiként szerepeljenek stringként a kódok, az értékeik pedig a történések betűjelei legyenek szintén mint string.

### Példa:

***input.txt***

```
[
    (["4.1", "5"], ["A", "O"]),
    (["4.1", "5", "1.2.3"], ["T", "O", "A"]),
    (["5"], ["O"])
]
```

***console printout:***

```
{
    "5": "O",
    "4.1": "A",
    "1.2.3": "T"
}
```

---

## 4. Fogaskerekek

**Feladatmappa:**

`gear_system`

### Leírás:

Ez a feladat egy egyszerű mechanikai rendszert szimulál, amely három fogaskereket és két kart tartalmaz. A fogaskerekek nem érintkeznek egymással. Minden fogaskeréknek hat foga van, rajtuk számok, 1-től 3-ig sorrendben: 1, 2, 3, 1, 2, 3.

Egy fogaskeréken csak egy érték látható egy adott pillanatban. Ha más értéket szeretnénk látni, forgatni kell azt. A karok meghúzása meghatározott módon forgatja a fogaskerekeket.

**Kezdeti beállítás:**

* Három fogaskerék van.
* Kezdetben mindhárom fogaskeréken a `3` érték látható.

**Karok:**

Egy-egy kar helyezkedik el balra és jobbra a fogaskerekektől:
* `left_lever` = `[1, 1, 0]` – az első (0.) és második (1.) fogaskereket forgatja előre 1-gyel.
* `right_lever` = `[0, 1, 1]` – a második (1.) és harmadik (2.) fogaskereket forgatja előre 1-gyel.
* A karok listaként vannak megadva, ahol minden szám azt jelzi, hogy az adott fogaskerékre milyen hatással van a kar. A nulla azt jelenti, hogy az adott fogaskerékre nincs hatással.

**Fogaskerekek mozgása:**

Minden alkalommal, amikor meghúzunk egy kart:
* A megfelelő értékek hozzáadódnak a fogaskerekek aktuális értékeihez.
* Ha az új érték meghaladja a 3-at, akkor visszaugrik 1-re.
* Ha az érték 1 alá csökkenne (hátrafelé forgatás esetén), akkor 3-ra ugrik vissza.

### Bemenet:

* Egy lista, amely a kívánt végállapotot tartalmazza (pl. `[2, 1, 2]`)
* Egy opcionális egész szám, a maximális karhúzások száma (alapértelmezés szerint 8)

### Kimenet:

* Ha elérhető a kívánt végállapot, akkor írja ki szóközökkel elválasztva a szükséges karhúzásokat: pl. `left`, `right`, stb.
* Ha nem, akkor írja ki: `Megoldhatatlan`

### Példa:

***input.txt***

```
[2, 1, 2]
```

***console printout:***

```
left left right right
```

---

## 5. Matematika kvíz

**Feladatmappa:**

`math_quiz`

**Leírás:**

7 alfeladat van, amelyet meg kell oldanotok, ezek az alfeladatok egymástól függetlenek.
Található egy _thinking.txt_ a feladat mappájában, kérünk titeket hogy amennyire tudjátok vezessétek le a megoldásotokat ott vagy a `main.py`-ban kommentek formájában.

1. Mekkora lehet a kör sugara, amit a képen látsz?

![image](https://github.com/user-attachments/assets/8cfee45e-3047-4d59-9ff3-e64d10cae002)


2. Oldd meg ezt az egyenletet! Kíváncsiak vagyunk, mit kapsz eredménynek!

![image](https://github.com/user-attachments/assets/793269c3-895e-4802-9d23-152063a1ba94)


3. Számold ki, mennyi az értéke ennek a kifejezésnek!

![image](https://github.com/user-attachments/assets/98dae480-7485-4277-9bbc-f15bd7d84f30)


4. Van itt még egy egyenlet – meg tudod oldani?

![image](https://github.com/user-attachments/assets/17d3c677-d6b3-4794-bfd5-94ccef05f6d7)


5. Nézd meg jól az ábrát! Milyen magas az ott látható asztal (cm-ben)?

![image](https://github.com/user-attachments/assets/1337df46-b12e-4b9f-9985-f56c517c7481)


6. Itt van három állat – összesen hány kilót nyomnak?

![image](https://github.com/user-attachments/assets/2ff93b58-e5f4-4b51-b1fc-d460e7a9ff75)


7. Anna és Balázs felváltva dobnak egy szabályos dobókockával. Anna kezd, és az nyer, aki először hatost dob. A játék véget ér, amint valaki hatost dob. Mekkora az esélye annak, hogy Anna nyeri a játékot?

**Bemenet:**

Nincs külön bemeneti fájl. Minden szükséges információ a feladatleírásból vagy az ábrákból szerezhető meg.

**Kimenet:**

A programnak sorban ki kell írnia a 7 feladat megoldását, minden megoldást külön sorba.

**Példa:**

*console printout:*

```
1.: 450
2.: 1943
...
6.: 123
7.: 1.5
```
