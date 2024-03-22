#include <unistd.h> // For execl and fork

int main() {
    system("/bin/sh");
}