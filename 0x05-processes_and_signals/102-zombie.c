#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop
 *
 * Return: always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point.
 *
 * Return: always 0.
 */
int main(void)
{
	int i = 0, pid = 0;

	for (; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
			continue;
		else if (pid == 0)
			exit(1);
		else
			printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();
	return (0);
}
