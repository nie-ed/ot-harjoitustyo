```mermaid
classDiagram
	Pelaaja "2..8" --> "1" Pelilauta
	Noppa "2" --> "1" Pelilauta
	Pelilauta --> "40" Ruutu : Contains
	Pelinappula "1" --> Ruutu : Located
	class Noppa{
	}
	class Pelaaja{
		Pelinappula
	}
	class Pelilauta{
	}	
	class Ruutu{
		Seuraava ruutu
	}

```
