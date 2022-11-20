```mermaid
sequenceDiagram
	participant Main
	participant Kone
	participant Moottori
	participant Tankki

	Main ->> Kone: Machine()
	Kone -> Tankki: FuelTank()
	Tankki -->> Kone: 0
	Kone -> Tankki: fill(40)
	Kone -> Moottori

	Main --> Kone: drive()
```
