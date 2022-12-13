## Viikko 3

- Luotu tiedostoon index.py ohjelman main() metodi, jolla aloitetaan ohjelma ja luodaan ruudukko ja solut. 
- Luotu luokka Level, jossa hallitaan pelin tilaa.
- Level luokassa luodaan sprite olioita ja muodostetaan niistä kaksiulotteinen taulukko. 
- Luotu luokka GameLoop, jossa aloitetaan peli, käsitellään pelaajan näppäinsyötteitä, ja piirretään sprite oliot ruudulle.
- Luotu taks.py, johon lisätty aloitukseen, testaukseen ja coverage raportin luomiseen metoditaskit.
- Luotu luokka Blocks, jonka avulla piirretään palikoita ruudulle.
- Luotu alustava luokka NewPiece, jolla pyritään luomaan käytössä oleva palikka ruudulle.
- Luotu tiedosto level_test.py, ja sinne luokka TestLevel johon luotu testi palikan liikkumiselle. Palikan liikkuminen toimii.
- Luotu Luokka Shapes, johon kerätty palikan muotoja, osoitteesta: https://data-flair.training/blogs/python-tetris-game-pygame/. Tiedosto ja sen käyttö vielä työnalla.
- Käyttäjä näkee näytöllä ruudukon.
- Käyttäjä näkee staattisia palikoita näytöllä.
- Käyttäjä voi liikuttaa yhden ruudun kokoista palikkaa näytöllä. 

## Viikko 4
- Luokka CreateShapes selvittää käytössä olevan palikan osien x ja y koordinaatiston positiot.
- Luokka NewBlockAttributes valitsee satunnaisen palikkamuodon ja asettaa palikan rotaation, x ja y koordinaatit ja värin.
- Luokkan Level lisätty toiminnallisuus piirtää käytössä oleva palikka ruudulle.
- Luokkaan Shapes on listattu palikkamuodot, jotka on saatu osoitteesta: https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/

## Viikko 5
- Metodi move_block liikuttaa palikkaa ja pysäyttää palikan liikkeen jos se osuu seinään tai toiseen staattiseen palikkaan
- Metodi _block_can_move tarkastaa onko palikka liikkumassa seinään tai toiseen staattiseen palikkaan
- Lisätty testaus palikan liikkeelle ja palikan osumiseen seinään.

## Viikko 6
- Lisätty aikariippuvainen palikan liikkuminen. Palikka liikkuu ruudulla alaspäin jatkuvasti.
- Lisätty palikan rotaation alustus. Ei toimi vielä täysin.
- Uusi palikka ilmestyy ruudun ylä reunaan.
