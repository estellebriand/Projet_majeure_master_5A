classdef obstacle_class
    %OBSTACLE_CLASS create a class for obstacle
    
    properties
        Front % BOOL
        Back  % BOOL
        Right % BOOL
        Left  % BOOL      
    end
    
    methods
        function obj = obstacle_class()
            %OBSTACLE_CLASS Construct an instance of this class
            %   Detailed explanation goes here
            obj.Front = 'False';
            obj.Back = 'False';
            obj.Right = 'False';
            obj.Left = 'False';
        end    
        function obj = update(obj,map_obstacles)
            obj.Front = map_obstacles('devant');
            obj.Back = map_obstacles('derriere');
            obj.Right = map_obstacles('droite');
            obj.Left = map_obstacles('gauche');
        end
    end
end

