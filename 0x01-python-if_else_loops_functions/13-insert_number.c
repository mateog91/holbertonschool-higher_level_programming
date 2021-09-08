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

	while (next->n <= number && next != NULL)
	{
		current = next;
		next = next->next;
	}
	if (!(next->n <= number))
	{
		new->next = next;
		current->next = new;
	}
	else
	{
		current->next = new;
		new->next = NULL;
	}
	return (new);
}
