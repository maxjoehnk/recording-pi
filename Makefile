OBJS = helper.o ui.o
CC = g++
DEBUG = -g
CFLAGS = -Wall -pthread -c $(DEBUG) $(LIBS)
LFLAGS = -Wall -pthread $(DEBUG) $(LIBS)
LIBS = -lpigpio -lrt

ui : $(OBJS)
	$(CC) $(LFLAGS) $(OBJS) -o ui

helper.o : src/helper.cpp src/helper.h src/ports.h
	$(CC) $(CFLAGS) src/helper.cpp

ui.o : src/ui.cpp src/helper.h src/ports.h
	$(CC) $(CFLAGS) src/ui.cpp

clean:
	\rm *.o *~ ui
