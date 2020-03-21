# NowPark (HackTheNorth 2019)

## Inspiration

A study conducted by USA Today exposed the devastating epidemic that is parking: the average motorist spends more than **17 hours** and wastes 345 dollars a year just looking for parking. That’s over **12 billion dollars** of fuel wasted per year nationally. We wanted to put and end to this struggle, which is why we created NowPark.

## What it does
NowPark is a parking app which automatically takes care of the majority of parking problems. Through this app, users will be able to see exactly which parking spots (not locations/building/zones: exact spots) which are open for parking. The user will be able to find them with an application on their phone or through the web app. The user will then be able to navigate to the parking spot, and will be automatically charged based on the amount of time the user spent at the parking spot.

## How we built it
We built our app using HTML/CSS/JS for the frontend along with React + Google Maps API. On the backend, we have a Firebase Cloud Firestore Database through which the user app and the parking spot sensors would interact with one another. For the hardware aspect, we used a Raspberry Pi + Ultrasonic Sensor.

## Challenges we ran into
Trying to integrate Firebase into React. Global state management in React. Trying to integrate our hardware to Firebase. Hardware + Software integration.

## Accomplishments that we're proud of
One accomplishment we are proud of is we got a working beta version of our app and product. We are also proud that we were able to connect the hardware to the frontend and vice versa, specifically as most of us had limited experience with the technologies we were working with.

## What we learned
Importance of security in authentication. Adjusting our plan to what is realistic during a short time period. How to use Firebase in python. How to work under a time pressure.

## What's next for NowPark
To have a computer vision algorithm that detects how many parking spots there are with a birds eye view, to have a feature that lets you book parking spots, and finally to have smaller and sturdier hardware to make everything as low profile as possible.
