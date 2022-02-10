### intro ###

Zoals al verteld,

ik ben aan het hobbyen, en heb ik 0 opleidingen gevolgd met programmeren
Alles heb ik mezelf geleerd a.d.v. google en "python-for-dummies" 

Dus ik gooi ongetwijfeld heel veel termen door elkaar zowel in het engels als
in het nederlands :)) vergeef me. 

ik ben bezig met een app, (screenshot in repo: "screenshot huidige app")
die op voorhand vast gezette trajecten op de rivier (sectoren) gestart en gestopt moeten worden
de tijd moet gaan bij houden, hoe lang we over een bepaald traject doen. zodat aan de hand van de vast gezette afstanden
een gemiddelde snelheid berekent kan worden. Op dit moment zijn de afstanden nog "verzonnen" omdat de werkelijke trajecten
uren kunnen duren voor een binnenvaart schip. heeft het testen met werkelijke gegevens nog geen zin. 

Er staat een py app "reisjournaal(eerdere versie).py tussen (in repo: screenshot eerste app)
Deze app heb ik ook zelf gemaakt toen ik net met python begon. 
Dat wat ik nu aan het bouwen ben, is min of meer voor mezelf een verplichting om meer "OOP" te gebruiken. 
Dat schijnt goed te zijn :)) 

beide maken gebruik van tkinter library/module/framework of iets dergelijks welke standaard met de officiele python3 zijn mee geleverd.

ps. ik heb géén idee waarom ik een "__pycache__" folder in de repo heb. Maar ik heb het idee dat ik ergens geheugen niet vrij geef of iets dergelijks.
maar dat valt simpel te googlen. 

edit: gegoogled wat "__pycache__" is, kan voor errors zorgen. Voor de zekerheid een keer gedelete. maar mocht niet baten voor het probleem :( 


### componenten ###
De app bestaat op het moment uit:
Main.py ( = overigens gewoon werkend/opstartbaar)
sector_class.py
voyage_class.py
numpad_class.py

en voor debug en wat dingen testen:
test_button.py


### het probleem ###
Het gaat fout bij het schermtoetsenboord.
Wanneer er op de toets "A" wordt gedrukt en een textbox is geselecteerd;
spuugt hij "test" neer terwijl dit "A" zou moeten zijn. "test" is de laatste knop in de list.
wanneer ik "test" weghaal, spuugt hij de tekst "Del" in de geselecteerde textbox. 

de knoppen worden d.m.v. een : " for each in list " - loop geinitieerd.
waarbij de "niet-enkele-letters" een andere method krijgen. 
Del = bijv. het tekstvak leegmaken. 

a.d.v. een if text == Del
wordt de button.configure(command=lambda: del_button()) toegewezen aan de button. 

hetzelfde geld voor "test", 
deze button (text) zou er voor moeten zorgen dat de inhoud van de textboxen op CLI word gedropt.

Alleen het lijkt erop, dat op 1 of andere manier, alle knoppen behalve "Del" de testbutton() method uit de test_button module toegewezen krijgen.


### overig ###
de overige bestanden:
GPS_grabber: werkt maar nog niet met de app. in de toekomst wel de bedoeling. 
GPSlog.txt: resultaat van GPS_grabber
reisjournaal.py


