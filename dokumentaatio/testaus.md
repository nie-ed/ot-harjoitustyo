# Testausdokumentti

## Yksikkö ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaa Level-luokka. Level-luokalle on tehty level_test.py tiedosto testaamiseen.

### Repositorio-luokka



### Testikattavuus

Sovelluksen tastauskattavuus on 63%. 

![Coverage Report](./pictures/coverage_report.png)

Testaamatta jäi osa build.py, config.py, initialized_database.py, event.py, game_loop.py ja level.py tiedostoista. Testikattavuuden ulkopuolelle olisi voinut jättää tiedostot, build.py, initialize_database.py ja event.py. Suurin ja tärkein osuus joku jäi testikattavuuden ulkopuolelle oli level.py tiedoston rotate_block metodi, joka on vastuussa palikan rotaatiosta.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on tehty manuaalisesti. Sovellusta on testattu käyttöohjeen kuvaamalla tavalla. 

Toiminnallisuuksia on testattu manuaalisesti käymällä läpi mahdollisia nuolinäppäinsyötteitä. Mahdollisia virhetilanteita on testattu käyttämällä virheellisiä syötteitä, eli muita näppäimiä kuin nuolinäppäimiä. 

## Sovellukseen jääneet laatuongelmat

- Kaikkien eri palikkavaihtoehtojen rotaatio ei toimi täysin oikein.
