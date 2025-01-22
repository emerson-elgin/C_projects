#include "storage_manager.h"
#include <stdlib.h>
#include <string.h>

StorageManager* create_storage(const char *filename) {
    StorageManager *sm = malloc(sizeof(StorageManager));
    sm->data_file = fopen(filename, "a+");
    fseek(sm->data_file, 0, SEEK_END);
    sm->total_pages = ftell(sm->data_file) / PAGE_SIZE;
    rewind(sm->data_file);
    sm->buffer_pool = calloc(BUFFER_POOL_SIZE, sizeof(Page));
    sm->current_page = 0;
    return sm;
}

// Implement other functions here
