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
int *channel(listint_t **head)
{
	int *int_arr, i = 0;
	listint_t *temp = *head;

	int_arr = malloc((sizeof(int) * len(head)) + 4);
	while (temp != NULL)
	{
		int_arr[i] = temp->n;
		i++;
		temp = temp->next;
	}
	int_arr[i] = '\0';
	return(int_arr);
}
int pali(int *arr, int fst, int lst)
{
	if (arr[fst] == arr[lst])
	{
		if (fst + 1 == lst - 1 || lst == fst + 1)
			return (1);
		return (pali(arr, fst + 1, lst - 1));
	}
	return (0);
}
/**
 * is_palindrome - a function that checks a list
 * @head: the head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int *arr = channel(head), i = 0;
	while (arr[i] != '\0')
		i++;
	i = pali(arr, 0, i - 1);
	free(arr);
	return (i);
}
