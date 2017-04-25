#include "paths.h"
#include <stdlib.h>
#include <string>

using namespace std;

string get_base_path() {
    return string(getenv("HOME")) + "/recordingpi";
}
