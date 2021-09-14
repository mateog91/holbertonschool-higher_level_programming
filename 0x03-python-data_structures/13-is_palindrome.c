#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: Head of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, count;
	listint_t *current = *head, *final = *head;

	if (*head == NULL)
		return (1);

	/* Encontrar longitud */
	while (final->next != NULL)
	{
		final = final->next;
		len++;
	}

	while (len - i >= i)
	{
		/* Resetiar final y count */
		final = current;
		count = i;
		/* Avanzar final hasta el final respectivo */
		while (count < len - i)
		{
			final = final->next;
			count++;
		}
		/* comparo current con final*/
		if (current->n != final->n)
			return (0);
		/* Avanzar current e i */
		current = current->next;
		i++;
	}
	/* Si sale sin antes retornar es Palindrom */
	return (1);
}
