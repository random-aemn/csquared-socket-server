# AIS Data Dictionary

[AIS Data Dictionary PDF source](https://coast.noaa.gov/data/marinecadastre/ais/data-dictionary.pdf)


|Field Position|Name| Description| Example| Units| Resolution| Type| Size|
|---|---|----|---|---|---|---|---|
|1|MMSI Maritime Mobile Identity Service value|  477220100||| Text| 9
|2 |BaseDateTime| Full UTC date and time| 2017-02-01T20:05:07|| YYYY-MM-DD:HH-MM-SS|DateTime
|3 |LAT| Latitude| 42.35137| decimal degrees| XX.XXXXX| Double| 8
|4 |LON| Longitude| -71.04182| decimal degrees| XXX.XXXXX| Double| 8
|5 |SOG| Speed Over Ground| 5.9| knots| XXX.X| Float| 4
|6 |COG| Course Over Ground| 47.5| degrees| XXX.X| Float| 4
|7 |Heading| True heading angle| 45.1| degrees| XXX.X| Float| 4
|8 |VesselName Name|Name as shown on the station radio license| OOCL Malaysia||| Text| 32 
|9 |IMO| International Organization Vessel number| IMO9627980||| Text| 7
|10|CallSign| Call sign as assigned by FCC| VRME7||| Text| 8
|11|VesselType| [Vessel type](#expanded-ais-ship-types) as defined in NAIS specifications| 70||| Integer| short
|12|Status| Navigation status as defined by the [COLREGS](https://www.imo.org/en/About/Conventions/Pages/COLREG.aspx)| 3||| Integer |short
|13|Length| Length of vessel (see NAIS specifications)  | 71.0 |meters |XXX.X |Float| 4
|14|Width| Width of vessel (see NAIS specifications)| 12.0| meters| XXX.X| Float| 4
|15|Draft| Draft depth of vessel (see NAIS specifications)| 3.5| meters| XXX.X |Float| 4
|16|Cargo| Cargo type (see NAIS specification and codes)| 70||| Text| 4
|17|TransceiverClass| Class of AIS transceiver| A |||Text| 2 


## Expanded AIS Ship Types 
Sourced from [AIS Ship Types](https://api.vtexplorer.com/docs/ref-aistypes.html)
|Type Code|Description|
|---|---|
|0	|Not available (default)
|1	|Reserved for future use
|2	|Reserved for future use
|3	|Reserved for future use
|4	|Reserved for future use
|5	|Reserved for future use
|6	|Reserved for future use
|7	|Reserved for future use
|8	|Reserved for future use
|9	|Reserved for future use
|10	|Reserved for future use
|11	|Reserved for future use
|12	|Reserved for future use
|14	|Reserved for future use
|14	|Reserved for future use
|15	|Reserved for future use
|16	|Reserved for future use
|17	|Reserved for future use
|18	|Reserved for future use
|19	|Reserved for future use
|20	|Wing in ground (WIG), all ships of this type
|21	|Wing in ground (WIG), Hazardous category A
|22	|Wing in ground (WIG), Hazardous category B
|23	|Wing in ground (WIG), Hazardous category C
|24	|Wing in ground (WIG), Hazardous category D
|25	|Wing in ground (WIG), Reserved for future use
|26	|Wing in ground (WIG), Reserved for future use
|27	|Wing in ground (WIG), Reserved for future use
|28	|Wing in ground (WIG), Reserved for future use
|29	|Wing in ground (WIG), Reserved for future use
|30	|Fishing
|31	|Towing
|32	|Towing: length exceeds 200m or breadth exceeds 25m
|33	|Dredging or underwater ops
|34	|Diving ops
|35	|Military ops
|36	|Sailing
|37	|Pleasure Craft
|38	|Reserved
|39	|Reserved
|40	|High speed craft (HSC), all ships of this type
|41	|High speed craft (HSC), Hazardous category A
|42	|High speed craft (HSC), Hazardous category B
|43	|High speed craft (HSC), Hazardous category C
|44	|High speed craft (HSC), Hazardous category D
|45	|High speed craft (HSC), Reserved for future use
|46	|High speed craft (HSC), Reserved for future use
|47	|High speed craft (HSC), Reserved for future use
|48	|High speed craft (HSC), Reserved for future use
|49	|High speed craft (HSC), No additional information
|50	|Pilot Vessel
|51	|Search and Rescue vessel
|52	|Tug
|53	|Port Tender
|54	|Anti-pollution equipment
|55	|Law Enforcement
|56	|Spare - Local Vessel
|57	|Spare - Local Vessel
|58	|Medical Transport
|59	|Noncombatant ship according to RR Resolution No. 18
|60	|Passenger, all ships of this type
|61	|Passenger, Hazardous category A
|62	|Passenger, Hazardous category B
|63	|Passenger, Hazardous category C
|64	|Passenger, Hazardous category D
|65	|Passenger, Reserved for future use
|66	|Passenger, Reserved for future use
|67	|Passenger, Reserved for future use
|68	|Passenger, Reserved for future use
|69	|Passenger, No additional information
|70	|Cargo, all ships of this type
|71	|Cargo, Hazardous category A
|72	|Cargo, Hazardous category B
|73	|Cargo, Hazardous category C
|74	|Cargo, Hazardous category D
|75	|Cargo, Reserved for future use
|76	|Cargo, Reserved for future use
|77	|Cargo, Reserved for future use
|78	|Cargo, Reserved for future use
|79	|Cargo, No additional information
|80	|Tanker, all ships of this type
|81	|Tanker, Hazardous category A
|82	|Tanker, Hazardous category B
|83	|Tanker, Hazardous category C
|84	|Tanker, Hazardous category D
|85	|Tanker, Reserved for future use
|86	|Tanker, Reserved for future use
|87	|Tanker, Reserved for future use
|88	|Tanker, Reserved for future use
|89	|Tanker, No additional information
|90	|Other Type, all ships of this type
|91	|Other Type, Hazardous category A
|92	|Other Type, Hazardous category B
|93	|Other Type, Hazardous category C
|94	|Other Type, Hazardous category D
|95	|Other Type, Reserved for future use
|96	|Other Type, Reserved for future use
|97	|Other Type, Reserved for future use
|98	|Other Type, Reserved for future use
|99	|Other Type, no additional information

## AIS Navigation Status

Sourced from [AIS Navigation Status](https://api.vtexplorer.com/docs/ref-navstat.html)
|Navigation Status	|Description
|---|---
|0	|Under way using engine
|1	|At anchor
|2	|Not under command
|3	|Restricted manoeuverability
|4	|Constrained by her draught
|5	|Moored
|6	|Aground
|7	|Engaged in Fishing
|8	|Under way sailing
|9	|reserved for future amendment of navigational status for ships carrying dangerous goods (DG), harmful substances(HS), or IMO hazard or pollutant category C, high-speed craft (HSC)
|10	|reserved for future amendment of navigational status for ships carrying dangerous goods (DG), harmful substances (HS) or marine pollutants (MP), or IMO hazard or pollutant category A, wing in the ground (WIG).
|11	|power-driven vessel towing astern.
|12	|power-driven vessel pushing ahead or towing alongside
|13	|Reserved for future use
|14	|AIS-SART is active
|15	|Not defined (default)


