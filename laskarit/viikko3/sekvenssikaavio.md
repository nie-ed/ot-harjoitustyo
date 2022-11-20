```mermaid
sequenceDiagram
  participant Main
  participant Kone
  participant Moottori
  participant Tankki
  Main->>Kone: Machine()
  Kone->>Tankki: FuelTank()
  Tankki-->>Kone: 0
  Kone->>Tankki: fill(40)
  Tankki-->>Kone: 40
  Kone->>Moottori
  Moottori-->>Kone: Tankki
  Main->>Kone: drive()
  Kone->>Moottori: start()
  Moottori->>Tankki: consume(5)
  Tankki-->>Moottori: fuel_contents(35)
```
