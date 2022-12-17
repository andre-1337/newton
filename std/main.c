#include "mem.h"

typedef struct Person {
	char *name;
	int age;
} Person;

int main(void) {
	Person *person = NEWTON_SAFE_NEW(-1);
	
	person->name = "John";
	person->age = 69;

	printf("%s %d\n", person->name, person->age);

	return 0;
}