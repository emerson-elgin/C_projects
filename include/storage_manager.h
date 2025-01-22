#ifndef STORAGE_MANAGER_H
#define STORAGE_MANAGER_H

#include <stdio.h>

#define PAGE_SIZE 4096
#define BUFFER_POOL_SIZE 100

typedef struct {
    unsigned char bytes[PAGE_SIZE];
    int page_number;
    int is_dirty;
} Page;

typedef struct {
    FILE *data_file;
    Page *buffer_pool;
    int total_pages;
    int current_page;
} StorageManager;

StorageManager* create_storage(const char *filename);
Page* fetch_page(StorageManager *sm, int page_number);
void flush_page(StorageManager *sm, int page_number);
void close_storage(StorageManager *sm);

#endif
