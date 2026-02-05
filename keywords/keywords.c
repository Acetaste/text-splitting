#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#define AFILE "input.txt"
#define CFILE "output.txt"
#define str_len(array) (sizeof(array)-1)/sizeof(array[0])


int size(int* size, FILE* fp);
int move(char** List,int starting_point, int amount, int* length_m, char replacement);
int removemultiple(char* List, char* List_of_char, int *len_List, int number_of_characters);
int replacechar(char* List, char* List_of_char, int len_List, int numb_of_char, char replacement);
int sepuppercase(char* List, int len_List, char replacement);

int main(void)
{
	 int length=0;
	 int i=0;
	 char List_sep_char[] = {"\n;&"};
	 char List_mult_char[] = {" ,"};


	 FILE* fpin = fopen(AFILE, "r");
	 if (fpin == NULL)
	 {
		 printf("Fehler beim öffnen von input.txt\n");
		 fclose(fpin);
		 return -1;
	  }

	  FILE* fpout = fopen(CFILE, "w");
	  if (fpout == NULL)
  	  {
 	    printf("Fehler beim öffnen von output.txt\n");
 	    fclose(fpin);
 	    fclose(fpout);
  	    return -2;
  	  }
	  size(&length,fpin);

	  char* List= malloc(length*sizeof(char));
	  if(List == NULL)
	  {
		  printf("Memory error");
		  return 1;
	  }
	  fread(List, sizeof(List[0]),length,fpin);



	  replacechar(List,List_sep_char,length,str_len(List_sep_char),*",");

	  //add Space after comma
	  for(i = 0; i<length;i++)
	  	  {
	  		  if((*(List+i) == ',') && (*(List+i+1) != ' '))
	  		  {
	  			  move(&List, i+1, 1, &length, ' ');

	  		  }
	  	  }
	  //remove Space before comma
	  for(i = 0; i<length;i++)
	  	  {
	  		  if((*(List+i)==' ') && (*(List+i+1)==','))
	  		  {
	  			  move(&List, i+1, -1, &length, ' ');
	  			  i--;

	  		  }
	  	  }
	  removemultiple(List,List_mult_char, &length, str_len(List_mult_char));
	  //sepuppercase(List,length,*",");




	 fwrite(List, sizeof(char),(length-1),fpout);

	 free(List);
	 fclose(fpin);
	 fclose(fpout);
	 return 0;
}



int size(int* size, FILE* fp)
{
	(*size)= 0;
	while(1)
		  	  {
			  	  if (feof(fp))
			  	  {
			  		  break;
			  	  }
			  	  fgetc(fp);

			  	  	(*size)++;
		  	  }
	rewind(fp);
	return 0;
}

int move(char** List,int starting_point, int amount, int* length_m, char replacement)
{
	int i;
	char* old_List= malloc((*length_m)*sizeof(char));
		  if(old_List == NULL)
		  {
			  printf("Memory error");
			  return 1;
		  }
	for(i=0;i<(*length_m); i++)
	{
		*(old_List+i) = *((*List)+i);
	}
	 *List = realloc((*List), ((*length_m)+amount)* sizeof(char));
	 if((*List) == NULL)
	 		  {
	 			  return 1;
	 		  }
	 /*for(i=0;i<starting_point;i++)
	 {
		 *(List+i)=*(old_List+i);
	 }*/
	 for(i = starting_point;i<(starting_point+amount);i++)
	 {
		 *((*List)+i)= replacement;
	 }
	 for(i=(starting_point);i<(*length_m);i++)
	 {
		 *((*List)+i+amount)= *(old_List+i);
	 }
	 *length_m = (*length_m)+amount;
	 free(old_List);
	return 0;
}
int removemultiple(char* List, char* List_of_char, int *len_List, int numb_of_char)
{
	int i,j,count=0;
	for(i = 0; i<numb_of_char;i++)
	{
		for(j = 0; j<*len_List;j++)
	  	  	  {
	  	  		  if(((*(List+j))==(*(List_of_char+i))) && (*(List+j+1)==(*(List_of_char+i))))
	  	  		  {
	  	  			  move(&List, j+1, -1, len_List, *(List_of_char+i));
	  	  			  j--;
	  	  			  count++;
	  	  		  }
	  	  	  }
	}
	return count;
}

int replacechar(char* List, char* List_of_char, int len_List, int numb_of_char, char replacement)
{
	int i,j, count = 0;
	for(j = 0;j<numb_of_char;j++)
	{
		for(i = 0; i<len_List;i++)
		  {
			  if(*(List+i) == *(List_of_char+j))
			  {
				  *(List+i) = replacement;
				  count++;
			  }

		  }
	}
	return count;
}
int sepuppercase(char* List, int len_List, char replacement)
{
	int i, count = 0;
	for(i = 0; i< len_List;i++)
	{
		if(*(List+i)>='a' && *(List+i)<='z' && *(List+i+1)>='A' && *(List+i+1)<='Z' )
		{
			move(&List,i+1,1,&len_List,replacement);
			count++;
		}
	}
	return count;
}
