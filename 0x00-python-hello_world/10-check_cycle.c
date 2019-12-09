#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - check if the list has a cycle
  * @list: pointer for checking if the list has a cycle
  * Return: 1 if list has a cycle or 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *copylist = list;

	while (copylist != NULL)
	{
		copylist = copylist->next;
		if (copylist == list)
			return (1);
	}
	return (0);
}
