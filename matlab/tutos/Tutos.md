# Tutuos matlab ros

## 1) Base
### creation noeud et rostopic list, rosmsg etc
https://fr.mathworks.com/help/ros/ug/get-started-with-ros.html

[functions utiles](https://fr.mathworks.com/help/ros/referencelist.html?type=function&category=publishers-and-subscribers&s_tid=CRUX_topnav)

Fichier: "test1.md"

## test publisher / suscriber
resultat après execution
Fichier: "test2.md"
```matlab
>> test2
Launching ROS Core...
...................Done in 2.8316 seconds.
Initializing ROS master on http://192.168.56.1:11311.
Initializing global node /matlab_global_node_47227 with NodeURI http://DESKTOP-K3CV3BK:58462/

scandata = 

  ROS LaserScan message with properties:

       MessageType: 'sensor_msgs/LaserScan'
            Header: [1×1 Header]
          AngleMin: -0.5216
          AngleMax: 0.5243
    AngleIncrement: 0.0016
     TimeIncrement: 0
          ScanTime: 0.0330
          RangeMin: 0.4500
          RangeMax: 10
            Ranges: [640×1 single]
       Intensities: [0×1 single]

  Use showdetails to show the contents of the message
  ```

<img src="test2.png"  alt="resultat /scan" height="300"/>

Fichier: "publisher"

```matlab
>> publisher
Launching ROS Core...
...................Done in 2.6536 seconds.
Initializing ROS master on http://192.168.56.1:11311.
Initializing global node /matlab_global_node_33567 with NodeURI http://DESKTOP-K3CV3BK:59467/

chatterpub = 

  Publisher with properties:

         TopicName: '/chatter'
    NumSubscribers: 0
        IsLatching: 1
       MessageType: 'std_msgs/String'


chattersub = 

  Subscriber with properties:

        TopicName: '/chatter'
    LatestMessage: [0×1 String]
      MessageType: 'std_msgs/String'
       BufferSize: 1
    NewMessageFcn: @exampleHelperROSChatterCallback


chattermsg = 

  ROS String message with properties:

    MessageType: 'std_msgs/String'
           Data: 'hello world'

  Use showdetails to show the contents of the message

Chatter Callback message data: 

ans =

    'hello world'

/chatter
/rosout 
/tf     
```

## Messages

[Basic message](https://fr.mathworks.com/help/ros/ug/work-with-basic-ros-messages.html)

[Messages spéciaux](https://fr.mathworks.com/help/ros/ug/work-with-specialized-ros-messages.html)
