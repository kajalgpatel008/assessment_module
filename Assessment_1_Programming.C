#include <stdio.h>
#include <string.h>
#include <conio.h>

void reverseString(char s1[])
{
    strrev(s1);
    printf("\nReversed string s1 is : %s",s1);

}

void concatenateString(char s1[])
{
    char s2[50];
    printf("Enter string s2 to concatenate: ");
    scanf("%s", &s2);
    strcat(s1,s2);
    printf("Concatenated string: %s\n", s1);
}

void checkPalindrome(char s1[])
{
    char s2[50];
    int x;
    printf("\n Enter string s1 : ");
    gets(s1);
    strcpy(s2,s1);
    strrev(s2);
    x=strcmp(s1,s2);
    if(x==0)
    {
	printf("\ns1 is palindrome");
    }
    else
    {
	printf("\ns1 is not a palindrome");
    }
}

void copyString(char s1[])
{
    char s2[50];
    strcpy(s2, s1);
    printf("Copied string: %s\n", s2);
}

void stringLength(char s1[])
{
    int len;
    len=strlen(s1);
    printf("\nLength of the string is : %d",len);
}

void charFrequency(char str[])
{
    int i;
    int freq[256] = {0};
    for (i=0; str[i] !=0; i++)
    {
	freq[(unsigned char)str[i]]++;
    }

    printf("Character frequencies:\n");
    for (i = 0; i < 256; i++)
    {
	if (freq[i] > 0)
	{
	    printf("'%c' = %d\n", i, freq[i]);
	}
    }
}

void countVowelsConsonants(char s1[])
{
    int i;
    int vowels = 0, consonants = 0;
    for (i = 0; s1[i] !=0; i++)
     {
	char ch = tolower(s1[i]);
	if (isalpha(ch))
	 {
	    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
		vowels++;
	    else
		consonants++;
	 }
    }
   printf("Vowels: %d, Consonants: %d\n", vowels, consonants);
}

void countSpacesDigits(char s1[])
{
    int i,spaces = 0,digits = 0;
    for (i = 0; s1[i] !=0; i++)
    {
	if (s1[i] == ' ')
	    spaces++;
	else if (isdigit(s1[i]))
	    digits++;
    }
   printf("Blank Spaces: %d, Digits: %d\n", spaces, digits);
}

int main()
{
    char s1[50];
    int choice;
    char cont;
    clrscr();

    do {
	printf("\nEnter a string: ");
	scanf(" %[^\n]", &s1);      //accepts full line with spaces

	printf("\nChoose an operation:\n");
	printf("1. Reverse the string\n");
	printf("2. Concatenation\n");
	printf("3. Check if palindrome\n");
	printf("4. Copy the string\n");
	printf("5. Length of the string\n");
	printf("6. Frequency of each character\n");
	printf("7. Count vowels and consonants\n");
	printf("8. Count blank spaces and digits\n");

	printf("Enter your choice (1-8): ");
	scanf("%d", &choice);

	switch (choice)
	 {
	    case 1:
		 reverseString(s1);
		 break;
	    case 2:
		 concatenateString(s1);
		 break;
	    case 3:
		 checkPalindrome(s1);
		 break;
	    case 4:
		 copyString(s1);
		 break;
	    case 5:
		 stringLength(s1);
		 break;
	    case 6:
		 charFrequency(s1);
		 break;
	    case 7:
		 countVowelsConsonants(s1);
		 break;
	    case 8:
		 countSpacesDigits(s1);
		 break;
	    default:
		printf("Invalid choice! No operation performed.\n");
		break;
	}

	printf("\nDo you want to continue? (y/n): ");
	scanf(" %c", &cont);

    }while (cont == 'y' || cont == 'Y');

    printf("Thank you! Exiting the program.\n");
    return 0;
}
