#include <stdio.h>

int main()
{
    char buf[100];
    scanf("%s", buf);
    while (1)
    {
        printf("%s\n", buf);
    }
    printf("Hello %s\n", buf);
    return 0;
}