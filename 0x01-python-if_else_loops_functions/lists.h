#ifndef LIST_H
#define LIST_H
#include <stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<stddef.h>
/**
 * struct listint_s - singly linked list
 * @n: integer to be added
 * @next: pointer to the next node
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
listint_t *add_nodeint_end(listint_t **head, const int n);
listint_t *insert_node(listint_t **head, int number);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);


#endif
