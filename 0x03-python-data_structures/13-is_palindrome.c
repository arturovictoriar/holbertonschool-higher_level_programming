#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * list_len - fills memory with a constant byte
  * @h: is the owner of the dog
  * Return: a number
  */
size_t list_len(const listint_t *h)
{
	int i;

	for (i = 0; h != NULL; i++)
		h = h->next;
	return (i);
}

/**
  * is_palindrome - checks if a singly linked list is a palindrome.
  * @head: single list
  * Return: 1 if it is a palin or 0 if not
  */

int is_palindrome(listint_t **head)
{
	int len = 0, *num, pal = 1, i = 0;
	listint_t *copyh = *head;

	if (!*head && !((*head)->next))
		return (1);
	len = list_len(*head);

	num = malloc(sizeof(int) * len);
	if (num == NULL)
		return (-1);

	for (i = 0; copyh; i++, copyh = copyh->next)
		num[i] = copyh->n;

	for (i = 0; i < len; i++)
	{
		if (num[i] != num[len - 1 - i])
		{
			pal = 0;
			break;
		}
	}

	free(num);
	return (pal);
}
