#include "lists.h"

/**
 * len - a function that returns the lenght of a list
 * @head: the head of the list
 * Return: the length
 */

int len(listint_t **head)
{
	listint_t *temp = *head;
	int count = 0;

	while (temp != NULL)
	{
		temp = temp->next;
		count++;
	}
	return (count);
}
/**
 * nvgt - a function that navigates in a list
 * @head: the head of the list
 * @count: the index
 * Return: a pointer to the node
 */

listint_t *nvgt(listint_t **head, int count)
{
	listint_t *temp = *head;

	while (count > 0)
	{
		temp = temp->next;
		count--;
	}
	return (temp);
}

/**
 * is_palindrome - a function that checks a list
 * @head: the head
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	int lst = len(head) - 1, i = 0;
	listint_t *temp1, *temp2;

	while (i <= lst / 2)
	{
		temp1 = nvgt(head, i);
		temp2 = nvgt(head, lst);
		if (temp1->n != temp2->n)
			return (0);
		i++;
		lst--;
	}
	return (1);
}
