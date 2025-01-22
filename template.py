import os

# Project structure configuration
config = {
    'files': [
        {
            'path': 'include/storage_manager.h',
            'content': '''#ifndef STORAGE_MANAGER_H
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
'''
        },
        {
            'path': 'src/storage_manager.c',
            'content': '''#include "storage_manager.h"
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
'''
        },
        {
            'path': 'include/record.h',
            'content': '''#ifndef RECORD_H
#define RECORD_H

typedef struct {
    int id;
    char name[50];
    float salary;
} Record;

void serialize_record(unsigned char *buffer, const Record *record, int offset);
Record deserialize_record(const unsigned char *buffer, int offset);

#endif
'''
        },
        {
            'path': 'src/record.c',
            'content': '''#include "record.h"
#include "storage_manager.h"

void serialize_record(unsigned char *buffer, const Record *record, int offset) {
    // Implementation here
}

Record deserialize_record(const unsigned char *buffer, int offset) {
    // Implementation here
    Record r = {0};
    return r;
}
'''
        },
        {
            'path': 'Makefile',
            'content': '''CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -Iinclude

SRC = src/main.c src/storage_manager.c src/record.c src/query_parser.c src/utilities.c
OBJ = $(SRC:.c=.o)
EXEC = minidb

all: $(EXEC)

$(EXEC): $(OBJ)
\t$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
\t$(CC) $(CFLAGS) -c $< -o $@

clean:
\trm -f $(OBJ) $(EXEC)

.PHONY: all clean
'''
        },
        {
            'path': 'src/main.c',
            'content': '''#include <stdio.h>
#include "storage_manager.h"
#include "record.h"

int main() {
    printf("MiniDB starting...\\n");
    // Add test code here
    return 0;
}
'''
        }
    ]
}

def create_project_structure():
    # Create directories
    os.makedirs('include', exist_ok=True)
    os.makedirs('src', exist_ok=True)
    
    # Create files
    for file in config['files']:
        with open(file['path'], 'w') as f:
            f.write(file['content'])
        print(f"Created: {file['path']}")
    
    print("\\nProject structure created successfully!")
    print("Next steps:")
    print("1. Run 'make' to build the project")
    print("2. Add implementations to the .c files")
    print("3. Add additional features as needed")

if __name__ == "__main__":
    create_project_structure()