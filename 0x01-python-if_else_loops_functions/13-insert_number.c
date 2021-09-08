#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - insert node in list
 * @head: first node
 * @number: integer with number in new node
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	current = *head;
	next = current->next;
	if (new->n < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (next != NULL && next->n <= number)
	{
		current = next;
		next = next->next;
	}
	if (next == NULL)
	{
		current->next = new;
		new->next = NULL;
	}
	else
	{
		new->next = next;
		current->next = new;
	}
	return (new);
}
