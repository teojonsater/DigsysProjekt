# EITA15-Projekt

Slutprojekt till kursen EITA15 - Digitala System.

## Medverkande

- Richard Colteius
- Arvid Fischer
- Teo Jonsäter
- Anna Svensson

## Inledning

Till kursen EITA15 - Digitala System har vi fått i uppgift att skapa ett projekt som visar på de kunskaper vi har fått
under kursens gång. Här är instruktionerna vi fick till projektet:

> The company that you are working for has asked you to develop a new product concept that you are to present for the
> product management team. Due to component shortage and a short time to market, you can only use components that you
> already have in-house. The customers of the company, and hence your target group, are people who cares about the
> environment and sustainability. The goal for you is to take a project from concept and idea to having realized a
> working
> prototype that is to be presented to the product management team.
>
> Technical requirements from the product management, the product should, at minimum,
>
> 1. include inputs from at least two different sensors
> 2. include presentation: display, LED(s) and/or buzzer
> 3. include interaction: button, potentiometer and/or rotary encoder
> 4. be designed as a state machine (sv: tillståndsmaskin)

Utifrån dessa instruktioner så har vi skapat en prototyp på en luftkvalitétsmätare som mäter luftkvalitén i en rum
genom att läsa av temperatur, luftfuktighet och mängden co2. Till prototypen finns en knapp, som när den trycks ner,
visar upp de avlästa värdena på en 14-segments display.

Om de avlästa värdena avviker från våra bestämda gränsvärden så kommer en av tre lysdioder att lysa upp. En grön lysdiod
kommer att lysa om co2-värdet är avvikande, en gul lysdiod kommer att lysa om luftfuktigheten är avvikande och en
röd lysdiod kommer att lysa om temperaturen är avvikande. Beroende på hur många avvikelser som finns så kommer en
påkopplad fläkt att starta i varierande hastigheter.

## Installation

Koden är skriven i Python och köra på en Adafruit Feather RP2040 med CircuitPython installerat. För att köra koden
krävs det att följande bibliotek är installerade på Feather RP2040:

- adafruit-circuitpython-ahtx0
- adafruit-circuitpython-ht16k33
- adafruit-circuitpython-sgp30

För att sedan köra koden på Feather RP2040 så behöver koden kopieras över till enheten. Detta görs genom att ansluta
Feather RP2040 med CircuitPython installerat (instruktioner
finns [här](https://learn.adafruit.com/adafruit-feather-rp2040-pico/circuitpython)) till en dator via en USB-kabel och
sedan kopiera över koden till enheten. OBS: `main.py` måste döpas om till `code.py`.