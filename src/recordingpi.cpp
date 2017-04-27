#include <gst/gst.h>
//#include "helper.h"
#include "session.h"
#include "recorder.h"
#include "paths.h"
#include <sys/time.h>
#include <sstream>

std::string get_name() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    std::ostringstream prefix;
    prefix << "recording-" << tv.tv_sec;
    return prefix.str();
}

int main(int argc, char** argv) {
    //setup();
    gst_init(&argc, &argv);
    create_session();
    init_recorder();
    main_loop();
    terminate_recorder();
    //terminate();
    return 0;
}
