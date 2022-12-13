## Sovelluslogiikka

```mermaid
classDiagram
	GameLoop
	NewBlockAttributes *--> Level 
	Blocks * --> Level
	Shapes --> NewBlockAttributes
        CreateShapes --> Level

	class Level {
		__init__()
		_initialize_sprites()
		_create_new_block()
		move_block()
		rotate_block()
	}

	class Blocks{
		__init__()
	}

	class NewBlockAttributes {
		__init__()
	}

	class Shapes {
		list shapes_list
		list shape_colors
	}

	class CreateShapes {
		__init__()
	}

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
