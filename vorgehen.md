# Vorgehensweise

1. Eingabe & Vorverarbeitung
2. Lexikalische Analyse (Scanner)
3. Syntaktische Analyse (Parser)
4. Semantische Analyse
5. Tests & Validierung

## Phase 0 – Projektstruktur & Grundlagen

- Festlegen der Projektstruktur (Scanner, Parser, Tests, …)
- Definition der PL/0-Grammatik als Referenz

## Phase 1 – Lexikalische Analyse (Scanner)

- Zerlegung des Quelltextes in Token
- Erkennen von Schlüsselwörtern, Bezeichnern, Zahlen und Operatoren
- Implementierung eines deterministischen Scanners
- Verwendung einer Token-Klasse mit Typ, Wert und Position

## Phase 2 – Syntaktische Analyse (Parser)

- Überprüfung der Programmsyntax
- Abbildung der Grammatik durch rekursive Abstiegsmethoden

- Umsetzung der PL/0-Grammatik als Methoden
- Direkte Fehlerbehandlung bei Syntaxfehlern

## Phase 3 – Semantische Analyse


- Prüfung der semantischen Korrektheit
- Verwaltung von Gültigkeitsbereichen und Symbolen

- Aufbau einer Symboltabelle
- Überprüfung von:
  - mehrfachen Deklarationen
  - nicht deklarierten Bezeichnern
  - Typverträglichkeit
- Verknüpfung mit dem Parser

## 7. Phase 5 – Tests & Validierung

- Erstellung von Testprogrammen
- Getrennte Tests für Scanner, Parser und Semantik
- Manuelle und automatisierte Tests
