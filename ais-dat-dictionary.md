# AIS Data Dictionary

|Name| Description| Example| Units| Resolution| Type| Size|


1 ,MMSI Maritime Mobile Identity Service value,  477220100,,, Text, 9
2 ,BaseDateTime, Full UTC date and time, 2017-02-01T20:05:07,, YYYY-MM-DD:HH-MM-SS, DateTime,
3 ,LAT, Latitude, 42.35137, decimal degrees, XX.XXXXX, Double, 8
4 ,LON, Longitude, -71.04182, decimal degrees, XXX.XXXXX, Double, 8
5 ,SOG, Speed Over Ground, 5.9, knots, XXX.X, Float, 4
6 ,COG, Course Over Ground, 47.5, degrees, XXX.X, Float, 4
7 ,Heading True heading angle, 45.1, degrees, XXX.X, Float, 4
8 ,VesselName Name as shown on the station radio license OOCL Malaysia Text 32 International Maritime
9 ,IMO Organization Vessel number IMO9627980 Text 7
10,CallSign Call sign as assigned by FCC VRME7 Text 8
11,VesselType Vessel type as defined in NAIS specifications 70 Integer short
12,Status Navigation status as defined by the COLREGS 3 Integer short
13,Length Length of vessel specifications) (see NAIS 71.0 meters XXX.X Float 4
14,Width Width of vessel (see NAIS specifications) 12.0 meters XXX.X Float 4
15,Draft Draft depth of vessel (see NAIS specifications) 3.5 meters XXX.X Float 4
16,Cargo Cargo type (see NAIS specification and codes) 70 Text 4
17,TransceiverClass Class of AIS transceiver A Text 2 
