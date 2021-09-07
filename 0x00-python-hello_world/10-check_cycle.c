#include "lists.h"

/**
 * check_cycle - checks if list is looped
 * @list: input list
 *
 * Return: 1 if it is looped cycle, 0 if not looped cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
