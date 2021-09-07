#include "lists.h"

/**
 * check_cycle - checks if list is looped
 * @list: input list
 *
 * Return: 1 if it is looped cycle, 0 if not looped cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL;
	listint_t *slow = NULL;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = slow->next;

	while (fast != NULL)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);


}
