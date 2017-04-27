#include <string>

int init_recorder();
void terminate_recorder();

void group_channels(int first_channel, bool grouped);

void record_channel(std::string path, std::string prefix, int first_channel, bool pair);

void stop_recording();

void main_loop();

bool is_recording();
