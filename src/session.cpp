#include "session.h"
#include "paths.h"
#include <fcntl.h>
#include <string>

using namespace std;

string name;

int open_session(string name) {
    string path = get_base_path() + "/" + name + "/session";
    int fh = open(path.c_str(), O_RDONLY);
}

int close_session() {

}

int save_session() {

}

int create_session() {

}

void set_session_name() {

}
