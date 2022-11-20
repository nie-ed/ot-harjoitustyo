
```mermaid
sequenceDiagram
	participant main
	participant lataajalaite
	participant lukijalaite
	participant matkakortti	

	create laitehallinto;
	main->>laitehallinto: HKLLaitehallinto()
	main ->> rautatietori: Lataajalaite()
	main ->>* ratikka6: Lukijalaite()
	main ->>* bussi244: Lukijalaite()
	main ->> laitehallinto: lisaa_lataaja(rautatietori)
	main ->> laitehallinto: lisaa_lukija(ratikka6)
	main ->> laitehallinto: lisaa_lukija(bussi244)
	main ->>* lippu_luukku: Kioski()
	main ->>* kallen_kortti: None
	kallen_kortti ->> lippu_luukku: osta_matkakortti("Kalle")
	lippu_luukku ->> matkakortti: Matkakortti("Kalle")
	lippu_luukku -->> kallen_kortti: uusi_kortti
	main ->> rautatietori: lataa_arvoa(kallen_kortti, 3)
	rautatietori ->> matkakortti: kasvata_arvoa(3)
	matkakortti -->> rautatietori: 3
	main ->> ratikka6: osta_lippu(kallen_kortti, 0)
	ratikka6 -->> matkakortti: vahenna_arvoa(1.5)
	matkakortti -->> ratikka6: 1.5
	ratikka6 -->> main: True
	main->>bussi244:osta_lippu(kallen_kortti, 2)
	bussi244 --> main: False
	

```

