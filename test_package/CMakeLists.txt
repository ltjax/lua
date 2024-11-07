cmake_minimum_required(VERSION 3.25)
project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 11)

find_package(lua CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example lua::lua)

