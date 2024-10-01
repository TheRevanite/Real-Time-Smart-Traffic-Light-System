# Real-Time-Smart-Traffic-Light-System

Herein lies the proposed implementation of a real-time smart traffic lights system.

Today, the duration of commute has become a pressing concern in metropolitan cities with large volumes of individuals traveling to their workplaces in peak hours of the day. The number of vehicles waiting at traffic signals is increasing day by day. While the standard duration of the green signal is efficient in most cases, during peak hours the unilateral flow of traffic from residential areas to commercial areas is largely biased. 

In this smart traffic light system, the duration of the green signal is altered in real time depending on the volume of vehicles present on the road. A real-time live feed of the road is captured and the extracted frames are compared with a reference image of an empty road. A canny edge detection algorithm is used for processing the images and a match percentage is computed between the processed images. The duration of the green signal is set in real time depending on the match percentage computed. Thus the volume of vehicles present on each side of the signal is analyzed to skew the duration of the green signal in proportion to the traffic.
