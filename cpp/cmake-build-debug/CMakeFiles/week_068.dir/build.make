# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.30

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Users/aayushsood/Applications/CLion.app/Contents/bin/cmake/mac/aarch64/bin/cmake

# The command to remove a file.
RM = /Users/aayushsood/Applications/CLion.app/Contents/bin/cmake/mac/aarch64/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/aayushsood/Development/leetcode/cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/aayushsood/Development/leetcode/cpp/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/week_068.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/week_068.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/week_068.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/week_068.dir/flags.make

CMakeFiles/week_068.dir/week-068.cpp.o: CMakeFiles/week_068.dir/flags.make
CMakeFiles/week_068.dir/week-068.cpp.o: /Users/aayushsood/Development/leetcode/cpp/week-068.cpp
CMakeFiles/week_068.dir/week-068.cpp.o: CMakeFiles/week_068.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/aayushsood/Development/leetcode/cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/week_068.dir/week-068.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/week_068.dir/week-068.cpp.o -MF CMakeFiles/week_068.dir/week-068.cpp.o.d -o CMakeFiles/week_068.dir/week-068.cpp.o -c /Users/aayushsood/Development/leetcode/cpp/week-068.cpp

CMakeFiles/week_068.dir/week-068.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/week_068.dir/week-068.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/aayushsood/Development/leetcode/cpp/week-068.cpp > CMakeFiles/week_068.dir/week-068.cpp.i

CMakeFiles/week_068.dir/week-068.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/week_068.dir/week-068.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/aayushsood/Development/leetcode/cpp/week-068.cpp -o CMakeFiles/week_068.dir/week-068.cpp.s

# Object files for target week_068
week_068_OBJECTS = \
"CMakeFiles/week_068.dir/week-068.cpp.o"

# External object files for target week_068
week_068_EXTERNAL_OBJECTS =

week_068: CMakeFiles/week_068.dir/week-068.cpp.o
week_068: CMakeFiles/week_068.dir/build.make
week_068: CMakeFiles/week_068.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/aayushsood/Development/leetcode/cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable week_068"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/week_068.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/week_068.dir/build: week_068
.PHONY : CMakeFiles/week_068.dir/build

CMakeFiles/week_068.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/week_068.dir/cmake_clean.cmake
.PHONY : CMakeFiles/week_068.dir/clean

CMakeFiles/week_068.dir/depend:
	cd /Users/aayushsood/Development/leetcode/cpp/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/aayushsood/Development/leetcode/cpp /Users/aayushsood/Development/leetcode/cpp /Users/aayushsood/Development/leetcode/cpp/cmake-build-debug /Users/aayushsood/Development/leetcode/cpp/cmake-build-debug /Users/aayushsood/Development/leetcode/cpp/cmake-build-debug/CMakeFiles/week_068.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/week_068.dir/depend

