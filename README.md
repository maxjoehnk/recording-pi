# Recording Pi

A Software and Hardware Combination for 1-Click Multi Channel Recording and Exporting.

# Components
## Hardware
All Hardware Specifications can be found in src/schematics.

## Python Host
The Python Backend interacts with the Hardware.
It does the actual recording via GStreamer and displays the application state on the display.

### HTTP API
#### POST: /recording/start
Start a new Recording with the posted filenames and channel layout

Request Body:
```json
[{
    "filename": "timestamp-0.wav",
    "channels": [1, 2]
}]
```

#### POST: /recording/stop
Stop a running recording

#### POST: /session/load
Load the posted Session

Request Body:
```json
{
    "id": "6242BDCC-EB94-4C40-9AC1-DA35E26B9C8D",
    "name": "Empty Session",
    "date": "2017-07-13T21:22:01.551Z",
    "channels": [[1, 2]],
    "recordings": []
}
```

#### POST: /session/close
Close the open session

## NodeJS Backend
The NodeJS Backend holds the main application state.
It provides an Api for the React Frontend and communicates to the Python Host via HTTP Requests.

### HTTP API
#### POST: /store/dispatch
Dispatch an Action on the Store

Request Body:
```json
{
    "type": "[Recording] Start",
    "payload": 1499981054812
}
```

#### GET: /store
Returns the whole store

## React Frontend
Allows Control of the Hardware via another Client on the Network. This can be a mobile device or a desktop.
