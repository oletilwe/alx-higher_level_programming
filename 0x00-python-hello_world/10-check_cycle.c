#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: input value
*/

struct listint_s {
int n;
struct listint_s *next;
};
typedef struct listint_s listint_t;
listint_t *slow = list;
listint_t*fast = list;
	while (slow && fast && fast->next)
{
	slow = slow->next;
	fast = fast->next->next
		if (slow == fast) {
			return (-1);
		}
}
return (0);
}

