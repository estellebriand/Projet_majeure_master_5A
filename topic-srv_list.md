# Robot 

Robot est un objet décrit comme suit:
```
classdef robot_class
    %ROBOT Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        Name % Name of the robot
        Obstacle %  classe Obstacle: return booleans if obstacles place on the Front/Back/Left/Right --> robot.Obstacle.Back
        Scan % raw data from the LIDAR 
        Map %  matrix filled with 0 or 1 representing the map
    end
    
    methods
        function obj = robot_class(name)
            %ROBOT Construct an instance of this class
            obj.Name = name;
        end
        
        function bool = is_obstacle(obj,position)
            %ROBOT Construct an instance of this class
            if position == "devant"
                bool = obj.Obstacle.Front;
            end
            if position == "derriere"
                bool = obj.Obstacle.Back;
            end
            if position == "droite"
                bool = obj.Obstacle.Right;
            end
            if position == "gauche"
                bool = obj.Obstacle.Left;
            end
        end

    end
end
```

# Choix des topics et services spécifique au projet

- /map => sous forme de matrice de flot

```
float[] map_matrice
--
```
- std_msgs/String -> /obstacles_spot
" 
