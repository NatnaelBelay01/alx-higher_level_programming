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
 * channel -  a function that channels all the data of alist
 * @head: the head of the list
 * Return: an array of the data from the list
 */
int *channel(listint_t **head)
{
	int *int_arr, i = 1;
	listint_t *temp = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (NULL);
	int_arr = malloc(sizeof(int) * (len(head) + 2));
	if (int_arr == NULL)
		return (NULL);
	while (temp != NULL)
	{
		int_arr[i] = temp->n;
		i++;
		temp = temp->next;
	}
	int_arr[0] = i - 1;
	int_arr[i] = '\0';
	return (int_arr);
}
/**
 * pali - a function that checks for palindrome
 * @arr: an array to be checked
 * @fst: index of the first number
 * @lst: index of the last number
 * Return: 0 or 1
 */
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
	int *arr = channel(head), i;

	if (arr == NULL)
		return (1);
	i = pali(arr, 1, arr[0]);
	free(arr);
	return (i);
}
