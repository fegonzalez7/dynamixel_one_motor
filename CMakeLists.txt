cmake_minimum_required(VERSION 3.0.2)
project(dynamixel_one_motor)

find_package(catkin REQUIRED COMPONENTS
  dynamixel_workbench_controllers
  roscpp
  rospy
  std_msgs
)

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )


## Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   std_msgs
# )


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES dynamixel_one_motor
#  CATKIN_DEPENDS dynamixel_workbench_controllers roscpp rospy std_msgs
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/jointSrv.py
  scripts/jointSub.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


