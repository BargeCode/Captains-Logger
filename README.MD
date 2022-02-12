<<<<<<< HEAD
# Captain's logger
=======
## update
probleem verholpen door de loop aan te passen.
Ik loopte door een list en wees aan geinitieerde hetzelfde item aan.
En het laatste item op de list blijft dan aangewezen. en alle buttons kregen dezelfde "laatste item" daardoor aangewezen.



### intro
>>>>>>> 9d6ab00a1fc845a37cb570231804c21c91521c71

### Intro
This application is being designed for inland barge vessels, in the beginning for the river rhine. 
I am solo on this and i have followed 0 coding courses or lessons. Act accordingly please :-) and correct me if im wrong. That is only going to help me. But be nice and have some patience.

This app is going to predict a arrival time more accuratly then the most experianced captains on the river. Since when the voyage starts, they have an accuracy of 4 hours. We will arrive 4 hours above or below that E.T.A.. After 40 years experiance they still get surprised by for example current or undepths on the riverbed. 

It probably will not hit production or be used. its a hobby project of a barge captain. At this moment there are probably teams of experts working on this idea or application as well.

### Targets
In the end, the app will grab a GPS device on a COM/USB port and use that flow of data to determine where the vessel is and how fast it is going. For now, i want it to start collecting data either trough the GPS or manual "timers".

in the future, i want it to work both ways. Not only will the programm feed us an E.T.A. but i want an feature where i can say : I have to be there at that time. Which RPMs do i have to set to the engines so we can get that with the least amount of fuel used and still be on time.

#### stuff that wil go automagically
So, the sectors of the river are fixed in the program. There are no fixed sectors on the river tho.
But i like to use the GPS grabber, to do a couple of run's and see which sectors we set in the first place. I think a sector has to be where keep a steady speed throughout. By setting "steady" sectors. we can have a more accurate prediction since it is going to be steady. So i have to learn how to implement Geofencing. I want it to predict a E.T.A. based on past results with roughly the same variables. 

<<<<<<< HEAD
#### stuff that have to be done by hand.
This isnt that bad. There are a couple of variables.
* River level, either high or low, you are gonna be slow.
* Draught, the more we reach maximum draught either by ships limit or keel clearance because of low river levels. We are gonna be slower.
* RPM's set on the machines. 
=======
ps. ik heb géén idee waarom ik een "__pycache__" folder in de repo heb. Maar ik heb het idee dat ik ergens geheugen niet vrij geef of iets dergelijks.
maar dat valt simpel te googlen. 

edit: gegoogled wat "__pycache__" is, kan voor errors zorgen. Voor de zekerheid een keer gedelete. maar mocht niet baten voor het probleem :( 


### componenten
De app bestaat op het moment uit:
Main.py ( = overigens gewoon werkend/opstartbaar)
sector_class.py
voyage_class.py
numpad_class.py

en voor debug en wat dingen testen:
test_button.py


### het probleem
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


### overig
de overige bestanden:
GPS_grabber: werkt maar nog niet met de app. in de toekomst wel de bedoeling. 
GPSlog.txt: resultaat van GPS_grabber
reisjournaal.py
>>>>>>> 9d6ab00a1fc845a37cb570231804c21c91521c71

# installing this app for you to test or try.
All you need is Python and pyserial. 
so install python with your favourit app manager.
and `pip install pyserial` . That should work.

Just know that at this point in time, pyserial isnt neccesary. it works seperatly from the main app. 
To get it working, hardcode your com or usb port into the code and set the `len()` method for the data you want to catch. The GPS we use on board is spitting out GPRMC and others. I only want the GPRMC since it got everything i need. 
