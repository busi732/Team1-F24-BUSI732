## Entity-Relationship Diagram (ERD)

1. **Key Entities**
    Based on the merged data, the primary entities are:
   - **Wind Turbin(WEC)**: Represents various operational metrics, such as wind speed, power, and rotation.
   - **Temperature**: Includes different temperature readings for varioous turbin components.
   - **Status**: Captures turbine status messages, errors, and fault information.
   - **Timestamp**: Represents the time-related data for each measurement.


2. **Attributes for Each Entity**
   - **Wind Turbin(WEC)**: `ava.windspeed`, `max. windspeed`,`min. windspeed`,`ava. Rotation`,`max. Rotation`,`Production kWh`, etc.
   - **Temperature**: `Spinner temp`, `Front bearing temp`,`Blade A temp`,`Nacelle temp`, etc.
   - **Status**: `Main Status`, `Sub Status`,`Full Status`,`Error`,`FaultMsg`,`Fault`.
   - **Timestamp**: `DateTime`, `Timesamp`,`Time`.


3. **Relationship Between Entities**
   - Each Wind Each Wind Turbine has multiple Temperature and Inverter readings recorded at different Timestamps.
   - Timestamp acts as a common reference across entities to synchronize data.

### Diagram
This visual structure highlights the relationships between `WEC`, `Temperature`, `Inverter` ,`Status`, and `Timestamp` centered on their common datetime fields. 

![Local image](./output_erd.png)