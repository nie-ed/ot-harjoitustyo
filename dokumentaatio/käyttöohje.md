# Käyttöohje

Voit ladata sovelluksen uusimman releasen [täältä](https://github.com/nie-ed/ot-harjoitustyo/releases).

## Sovelluksen käynnistäminen
Asenna aluksi sovelluksen riippuvuudet komennolla

```bash
poetry install
```

Suorita alustus komennolla:

```bash
poetry run invoke build
```

Sovelluksen voi käynnistää komennolla:

```bash
poetry run invoke start
```

## Sovelluksen käyttö
Peliä voi pelata painamalla nuolinäppäimiä: 
- Painamalla alas palikka liikkuu yhden alaspäin ruudulla.
- Painamalla oikealle palikka liikkuu yhden oikealla ruudulla.
- Painamalla vasemmalle, palikka liikkuu yhden vasemmalle
- Painamalla ylös, palikka rotatoi.

Palikkaa ei voi liikuttaa yli peliruudun reunojen eikä muiden jo ruudulla olevien palikoiden päälle.

Pisteitä voi kerätä, sovittamalla palikat ruudulle niin, että kokonainen rivi täyttyy palikan osista. Jos kokonainen rivi täyttyy, se katoaa ruudulta ja pelaaja saa 10 pistettä lisää.

Peli loppuu jos jokin palikka ylittää ruudun yläreunan. 

Jos pelin haluaa lopettaa ajoissa, voi painaa pelinäytön yläoikeassa olevaa ruksi näppäintä. Tällöin kuitenkaan pelaajan keräämät pisteet eivät tallennu repositorioon.

Loppuruudulla näkyy pelaajan keräämät pisteet, sekä top 10 pistemäärää, joita saatu aiemmilla pelauskerroilla.
