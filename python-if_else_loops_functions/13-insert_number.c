#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to the head of the list
 * @number: number to insert
 *
 * Return: address of new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *previous = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	current = *head;

	/* Insert at beginning */
	if (number < current->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	/* Find insertion point */
	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	previous->next = new;
	new->next = current;

	return (new);
}
