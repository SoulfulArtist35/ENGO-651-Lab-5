# ENGO 651 Advanced Geospatial Topics Lab 5

## Ryan Janssen

## Overview

## Launching the Website

a. Github Pages:
    Simply visit `https://soulfulartist35.github.io/ENGO-651-Lab-5/`

b. VS Code:

1. Click on file "index.html"
2. Press F5

## Using the Website

a. Connecting to MQTT Broker

1. Type in desire host, post and SSL or use provided defaults
2. Click on "Connect"
3. After connecting to the MQTT broker, the connect form will disappear
4. Connected options (Share Status, Subscribe, Publish) will appear on the screen

b. Disconnecting to MQTT Broker

1. Click on "End Connection"
2. The connect form asking for host, port and SSL will reappear

c. Connection Status

There is a status bar at the top of the webpage below the main heading. It primary function is to inform the user the status of the connection. The console also informs the user about the connection status

| Status | Meaning |
|----|----|
| Not Connected | MQTT has never connected in instance |
| Connected | Currently connect to MQTT broker |
| Disconnected | User has disconnected session |
| Connection Drop | Lost connection with broker |

d. Subscribing to MQTT Topic

1. Enter desired MQTT Topic into subscription form
2. Click on "Topic subscribe"

f. Publish a MQTT Message

1. Enter desired MQTT Topic into publish form
2. Enter desired MQTT message
3. Click on "Publish"

g. View Location on Map

1. Subscribe to `ENGO651/Ryan/my_temp` by following instructions in d.
2. Location will appear on the map

h. Share MQTT Location

1. Click on "Share my Status"
2. Allow location sharing

i.Map Markers

1. Marker color will indicate temperature
   | Color | Temperature |
   |---|---|
   | Blue | -40 to 10 |
   | Green | 10.1 to 29.9 |
   | Red | 30 to 60 |

2. Click on marker to view its exact temperature

## Using MQTTX (Default Settings)

a. Connect to MQTT Broker

1. Click on "Add New Connection
2. Host:

   `wss://`

   `test.mosquitto.org`

3. Port: `8081`

4. Path: `/mqtt`

5. SSL/TLS: `On`

6. SSL Secure:  `off`

7. Certificate: `CA signed server certificate`

8. Click on "Connect"

b. Subscribe to MQTT Topic

1. Click on "New Subscription"
2. Enter desired topic
3. Qos: `0`

c. Publish a MQTT Message

1. QoS `0`
2. Enter desired topic
3. Enter desired message

## Terms of Use

The user agrees to only use the created website for personal use only. This license prohibits altering the created website without explicit concent from the creater.
