# Install script for directory: /fs03/share/users/jeremie.kahan/home/Bureau/s5_g7_briand_guy_kahan_martinez/Progression_Jeremie_Kahan/Projet_de_Majeure/moveit_HIL/src/HIL_movit_setup

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/fs03/share/users/jeremie.kahan/home/Bureau/s5_g7_briand_guy_kahan_martinez/Progression_Jeremie_Kahan/Projet_de_Majeure/moveit_HIL/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/fs03/share/users/jeremie.kahan/home/Bureau/s5_g7_briand_guy_kahan_martinez/Progression_Jeremie_Kahan/Projet_de_Majeure/moveit_HIL/build/HIL_movit_setup/catkin_generated/installspace/HIL_movit_setup.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/HIL_movit_setup/cmake" TYPE FILE FILES
    "/fs03/share/users/jeremie.kahan/home/Bureau/s5_g7_briand_guy_kahan_martinez/Progression_Jeremie_Kahan/Projet_de_Majeure/moveit_HIL/build/HIL_movit_setup/catkin_generated/installspace/HIL_movit_setupConfig.cmake"
    "/fs03/share/users/jeremie.kahan/home/Bureau/s5_g7_briand_guy_kahan_martinez/Progression_Jeremie_Kahan/Projet_de_Majeure/moveit_HIL/build/HIL_movit_setup/catkin_generated/installspace/HIL_movit_setupConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/HIL_movit_setup" TYPE FILE FILES "/fs03/share/users/jeremie.kahan/home/Bureau/s5_g7_briand_guy_kahan_martinez/Progression_Jeremie_Kahan/Projet_de_Majeure/moveit_HIL/src/HIL_movit_setup/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/HIL_movit_setup" TYPE DIRECTORY FILES "/fs03/share/users/jeremie.kahan/home/Bureau/s5_g7_briand_guy_kahan_martinez/Progression_Jeremie_Kahan/Projet_de_Majeure/moveit_HIL/src/HIL_movit_setup/launch" REGEX "/setup\\_assistant\\.launch$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/HIL_movit_setup" TYPE DIRECTORY FILES "/fs03/share/users/jeremie.kahan/home/Bureau/s5_g7_briand_guy_kahan_martinez/Progression_Jeremie_Kahan/Projet_de_Majeure/moveit_HIL/src/HIL_movit_setup/config")
endif()
