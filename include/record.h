#ifndef RECORD_H
#define RECORD_H

typedef struct {
    int id;
    char name[50];
    float salary;
} Record;

void serialize_record(unsigned char *buffer, const Record *record, int offset);
Record deserialize_record(const unsigned char *buffer, int offset);

#endif
