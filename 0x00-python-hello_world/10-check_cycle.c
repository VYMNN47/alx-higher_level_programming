#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: ptr to the list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
 int check_cycle(listint_t *list)
{
	listint_t *rapide = list, *lent = list;

	while (rapide && fast->next)
	{
		lent = lent->next;
		rapide = rapide->next->next;
		if (lent == rapide)
			return (1);
	}
	return (0);
}
