## Sam Deslandes - Lab 5

#####Step 1  
'''
ubuntu@ubuntu:~/Documents/Lab5/Step1$ cmake .
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ubuntu/Documents/Lab5/Step1
ubuntu@ubuntu:~/Documents/Lab5/Step1$ make
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
'''  

#####Step 2  
'''
ubuntu@ubuntu:~/Documents/Lab5/Step2$ cmake .
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ubuntu/Documents/Lab5/Step2
ubuntu@ubuntu:~/Documents/Lab5/Step2$ make
Scanning dependencies of target MathFunctions
[ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
'''  

#####Step 3  
'''
ubuntu@ubuntu:~/Documents/Lab5/Step3$ make
[ 50%] Built target MathFunctions
[100%] Built target Tutorial
ubuntu@ubuntu:~/Documents/Lab5/Step3$ ctest
Test project /home/ubuntu/Documents/Lab5/Step3
    Start 1: TutorialRuns
1/5 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialComp25
2/5 Test #2: TutorialComp25 ...................   Passed    0.00 sec
    Start 3: TutorialNegative
3/5 Test #3: TutorialNegative .................***Failed  Required regular expression not found.Regex=[-25 is 0
]  0.00 sec
    Start 4: TutorialSmall
4/5 Test #4: TutorialSmall ....................   Passed    0.00 sec
    Start 5: TutorialUsage
5/5 Test #5: TutorialUsage ....................   Passed    0.00 sec

80% tests passed, 1 tests failed out of 5

Total Test time (real) =   0.01 sec

The following tests FAILED:
	  3 - TutorialNegative (Failed)
Errors while running CTest
'''

#####Step 4  
'''
ubuntu@ubuntu:~/Documents/Lab5/Step4$ cmake .
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ubuntu/Documents/Lab5/Step4
ubuntu@ubuntu:~/Documents/Lab5/Step4$ make
Scanning dependencies of target MathFunctions
[ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
'''  

######Step 5
'''
ubuntu@ubuntu:~/Documents/Lab5/Step5$ cmake .
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ubuntu/Documents/Lab5/Step5
ubuntu@ubuntu:~/Documents/Lab5/Step5$ make
Scanning dependencies of target MakeTable
[ 25%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.o
Linking CXX executable MakeTable
[ 25%] Built target MakeTable
[ 50%] Generating Table.h
Scanning dependencies of target MathFunctions
[ 75%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 75%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
'''

'''test'''
