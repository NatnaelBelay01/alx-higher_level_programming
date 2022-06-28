#include "lists.h"
/**
 * insert_node - a function that inserts a node
 * @head: the head of the node
 * @number: the number value
 * Return: head
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
		return (*head);
	}
	temp = *head;
	if (temp->n > node->n)
	{
		node->next = temp;
		*head = node;
		return (*head);
	}
	while (temp->next != NULL)
	{
		if (node->n < temp->next->n)
		{
			node->next = temp->next;
			temp->next = node;
			return (*head);
		}
		temp =  temp->next;
	}
	temp->next = node;
	node->next = NULL;
	return (*head);
}
