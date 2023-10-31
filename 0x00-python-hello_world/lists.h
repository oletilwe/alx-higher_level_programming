#!/usr/bin/python3
#ifndef LISTS.H
#define LISTS.H

#include <stdio.h>
#include <stdlib.h>
struct listint_s
{
int n;
struct listint_s *next;
};
typedef struct listint_s listint_t;
int check_cycle(listint_t *list);
#endif
