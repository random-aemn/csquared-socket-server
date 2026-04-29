# Conversion of data from PositionReportMap data structure to CargoTypeMap data structure

## Data Structures

### Position Report 
 
 This interface provides the structure for a Postion Report received via the websocket.
 
```
interface PositionReportStruct {
  "MMSI": number,
  "BaseDateTime": string,
  "LAT": number,
  "LON": number,
  "SOG": number,
  "COG": number,
  "Heading": number,
  "VesselName": string,
  "IMO": string,
  "CallSign": string,
  "VesselType": number,
  "Status": number | null,
  "Length": number,
  "Width": number | null,
  "Draft": number | null,
  "Cargo": number | null,
  "TransceiverClass": string,
  "VesselTypeTxt" : string | null,
  "CargoTxt" : string | null,
  "Hazardous": string,
  "Nav_Status": string 
}
```

This interface provides the ability to explicitly a MMSI with a set of Position Reports

```
interface mmsiPositionReportListStruct {
	mmsi : number,
	positionReportList : Array<PositionReportStruct>
}
```

This structure will be used to define a map with a key of *CargoType* and a value of an <Array>mmsiPositionReportListStruct
Thus, a given *CargoType* can be associated with many MMSIs and each MMSI with a set of PositionReports

```
interface CargoTypeMapStruct {
		cargoType : string,
		mmsiPositionReportList : Array<mmsiPositionReportListStruct>
}
  ```


