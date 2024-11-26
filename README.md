directions.py
=============

A very simple script using the googlemaps python library to do a regular (in my case, every 
10 minutes) query to get the estimated (including traffic) drive time both to and from work. 
This info is then fed into a graphite/carbon/whisper store as is, slight mods (if even needed) 
would allow feeding into another desired system.  I've been running this since 2015 to track 
travel times to/from work and have some interesting data, especially around the time of the 
Covid breakout.

The directions vs newdirections was a change I made around Covid where I added the newdirections 
whisper files with a much longer retention time at much higher time resolution.. you only need to 
write each once

Requires the googlemaps python library:
https://github.com/googlemaps/google-maps-services-python

Their page includes how to sign up and get a google API key.  Make sure to read what the allowed
queries are before costs are incurred to avoid suddenly owing google a bunch of money.
