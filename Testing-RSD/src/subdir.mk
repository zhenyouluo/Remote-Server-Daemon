################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/ConnectionContext.cpp \
../src/JsonRPC.cpp \
../src/RSD.cpp \
../src/Registration.cpp \
../src/RsdMsg.cpp \
../src/TcpWorker.cpp \
../src/UdsComClient.cpp \
../src/UdsComWorker.cpp \
../src/UdsRegServer.cpp \
../src/UdsRegWorker.cpp 

OBJS += \
./src/ConnectionContext.o \
./src/JsonRPC.o \
./src/RSD.o \
./src/Registration.o \
./src/RsdMsg.o \
./src/TcpWorker.o \
./src/UdsComClient.o \
./src/UdsComWorker.o \
./src/UdsRegServer.o \
./src/UdsRegWorker.o 

CPP_DEPS += \
./src/ConnectionContext.d \
./src/JsonRPC.d \
./src/RSD.d \
./src/Registration.d \
./src/RsdMsg.d \
./src/TcpWorker.d \
./src/UdsComClient.d \
./src/UdsComWorker.d \
./src/UdsRegServer.d \
./src/UdsRegWorker.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -g -DTESTMODE -DDEBUG -I/home/dnoack/cpputest-3.6/include/CppUTest -I/home/dnoack/cpputest-3.6/include/CppUTestExt -I/home/dnoack/libs/rapidjson/include/rapidjson -I"/home/dnoack/workspace/RSD-and-Plugin-lib/include" -O3 -Wall -c -fmessage-length=0 ${CXXFLAGS} -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

