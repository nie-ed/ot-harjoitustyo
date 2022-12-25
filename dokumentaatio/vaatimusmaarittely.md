# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella käyttäjän voi pelata Tetris peliä, eli peliä, jossa yritetään sovittaa ruudulle ilmestyvät erimuotoiset palikat jo ruudulla olevien paikoiden joukkoon.

## Käyttäjät

Sovelluksella on vain yksi käyttäjäryhmä, joka on **normaali käyttäjät**. 

## Suunnitellut toiminnallisuudet

### Perusversio
**Peliruudulla:**
  - Sovellus muodostaa eri muotoisia ja väriä palikoita.
  - Palikat liikkuvat ruudulle ruudun yläreunasta.
  - Palikat eivät liiku yli ruudun oikean ja vasemman reuna.
  - Palikat eivät liiku staattisten palikoiden päälle.
  - Palikoita voi liikuttaa nuolinäppäimillä vasemmalle ja oikealle.
  - Palikoiden rotaation mahdollisuus.
  - Palikat voi sovittaa jo ruudulla näkyvien staattisten palikoiden joukkoon.
  - Rivi katoaa pelaajan pistemäärä kasvaa 10 pistettä, jos rivi on täysi.
  - Pelaajan pistenäärä näkyy pelatessa ruudulla.
  - Seuraavaksi tuleva palikka näkyy pelatessa ruudulla.
  - Peli loppuu, jos palikan osa menee yli ruudun ylärajan.

**Loppunäkymässä:**
- Pelin loputtua pelaajan pisteet tallennetaan tietokantaan.
- Pelin loppuruudulla näkyy top 5 tietokantaan tallennettua pistemäärää.

### Jatkokehitysideat
- Eri vaikeustasoja
- Mahdollisuus luoda oma käyttäjätunnus ja tallentaa omia tuloksia käyttäjätunnukselle.
 
