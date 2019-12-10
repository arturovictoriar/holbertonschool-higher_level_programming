#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * insert_node - insert a new node at sort of a listint_t list
  * @head: pointer to pointer of first node of listint_t list
  * @number: integer to be included in new node
  * Return: address of the new element or NULL if it fails
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copyhead = *head, *oldnode = NULL, *new;

	if (head == NULL || *head == NULL)
		return (NULL);

	for (; copyhead != NULL; copyhead = copyhead->next)
	{
		if (number < copyhead->n)
			break;
		oldnode = copyhead;
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = copyhead;

	oldnode->next = new;
	return (new);
}
