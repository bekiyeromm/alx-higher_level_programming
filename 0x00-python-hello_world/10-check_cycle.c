#include<stdio.h>
#include"lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: A singly-linked list.
 * Return: 0 If there is no cycle.
 *         If there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *new;
	
	if (list == NULL || list->next == NULL)
		return (0);
	current = list->next;
	new = list->next->next;
	while (current && new && new->next)
	{
		if (current == new)
			return (1);
		current = current->next;
		new = new->next->next;
	}
	return (0);
}
