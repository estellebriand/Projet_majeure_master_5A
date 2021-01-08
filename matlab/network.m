%% Init
%to share variable for calling callback function
global pos
global orient
%set python environment
pe = pyenv('Version','2.7');
pe.Version

%start roscore
rosinit("192.168.1.54",22)