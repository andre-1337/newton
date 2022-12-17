#include "mem.h"


void *NEWTON_NEW(size_t sz) {
	void *ptr = malloc(sz);

	return ptr;
}

void *NEWTON_SAFE_NEW(size_t sz) {
	void *ptr = malloc(sz);

	if (ptr == NULL) {
		printf("ERROR : ALLOCATED MEMORY POINTS TO NULL");
		exit(-1);
	}

	return ptr;
}