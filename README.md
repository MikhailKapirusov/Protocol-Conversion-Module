# **Robot Movement Control**
![Screenshot](https://github.com/MikhailKapirusov/ROS_GUI/blob/main/APP/Logo.PNG)

# Protocol Conversion Module
Protocol conversion module for a mobile robot based on the ROS framework.
*This module has its flaws and will be improved in the future*

## Background
The main purpose of a software system for controlling the movement of a mobile robot is to provide the average user with the opportunity to control a mobile robot, both within the same local network and remotely.
The main feature of the software system is the previously taken developments of the autonomous navigation algorithm of the mobile robot and an early prototype of the client application, which need to be implemented into the software system. 
The requirement for the system was to provide the ability to control the robot from a remote device in NAT conditions. 
In view of these features, it was determined that the software system should consist of three parts: a client application, a protocol conversion module as part of the built-in software of the mobile robot and a server.

***The protocol conversion module is provided here, offline navigation for the client application is provided, and the server installer is provided in other repositories.***

![Screenshot](https://github.com/MikhailKapirusov/ROS_GUI/blob/main/Pic1.JPG)

For the robot you need to install ROS + explorer_lite (or m-explore-2) + protocol conversion module

- m-explore-2 (https://github.com/MikhailKapirusov/m-explore-2)

- protocol conversion module (https://github.com/MikhailKapirusov/Protocol-Conversion-Module)

For the server, you need to install and configure the ejabberd server and cotunr as a STUN server.

## Installation
*!Before executing the script, you must create the /usr/local/lib/ directory. You need to move the files module_proxy.py!*

*1*. To install the ***"Protocol Conversion Module"*** client application, use the bash installer ***"install_proxy.sh"***

*1.1*. Make the installation file ***"install_proxy.sh"*** executable with the command: `chmod +x ./install_proxy.sh`

*1.2*. Run the installer with the command: `install_proxy.sh`

As a result, the protocol conversion module service will be launched in the background:

![Screenshot](https://github.com/MikhailKapirusov/Protocol-Conversion-Module/blob/main/PCM-service.png)
