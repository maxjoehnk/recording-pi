OBJS = helper.o ui.o
CC = g++
DEBUG = -g
CFLAGS = -Wall -pthread -c $(DEBUG) $(LIBS)
LFLAGS = -Wall -pthread $(DEBUG) $(LIBS)
LIBS = -lpigpio -lrt `pkg-config --cflags --libs gstreamer-1.0`

ui : $(OBJS)
	$(CC) $(LFLAGS) $(OBJS) -o ui

audio : audio.o helper.o
	$(CC) $(LFLAGS) audio.o helper.o -o audio

helper.o : src/helper.cpp src/helper.h src/ports.h
	$(CC) $(CFLAGS) src/helper.cpp

ui.o : src/ui.cpp src/helper.h src/ports.h
	$(CC) $(CFLAGS) src/ui.cpp

audio.o : src/audio.cpp src/helper.h
	$(CC) $(CFLAGS) src/audio.cpp

clean:
	\rm *.o *~ ui
