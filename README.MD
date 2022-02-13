# Captain's logger


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


#### stuff that have to be done by hand.
This isnt that bad. There are a couple of variables.
* River level, either high or low, you are gonna be slow.
* Draught, the more we reach maximum draught either by ships limit or keel clearance because of low river levels. We are gonna be slower.
* RPM's set on the machines. 


# installing this app for you to test or try.
All you need is Python and pyserial. 
so install python with your favourit app manager.
and `pip install pyserial` or `pip3 install pyserial` . That should work.

Just know that at this point in time, pyserial isnt neccesary. it works seperatly from the main app. 
To get it working, hardcode your com or usb port into the code and set the `len()` method for the data you want to catch. The GPS we use on board is spitting out GPRMC and others. I only want the GPRMC since it got everything i need. 
