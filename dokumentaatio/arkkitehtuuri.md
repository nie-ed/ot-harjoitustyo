## Sovelluslogiikka

```mermaid
classDiagram
	GameLoop
	ShapeIndexes *-- Level 
	Blocks * -- Level
	GetShape *-- Level
	Map -- Level
	DrawDisplay -- GameLoop
	Event *-- GameLoop
	Clock -- GameLoop
	Level --> GameLoop
	
	
	


```

Sovelluksen toiminnasta vastaa luokka Level. Level tarjoaa käyttöliittymän toiminnoille metodit kuten:

- initialize_sprites
- initialize_shape
- move_block
- rotate_block

Level luokka pääsee käsiksi palikoiden luomiseen käytettäviin GetShape, ShapeIndexes ja Shapes luokkiin.

![Pakkauskaavio](pakkauskaavio.png)


## Sekvenssikaavio

![Sekvenssikaavio](sekvenssikaavio.png)
