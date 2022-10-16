#include <stdio.h>
#include  <stdlib.h>

int sum(int *arr){
    int sum = 0;
    // int size = sizeof(arr)/sizeof(int);
    for (int i=0;i<5;i++){
        sum = sum + arr[i];
    }
    return sum;
}

int main(int argc,char *argv[]){
    int *n = malloc(sizeof(int));
    int *arr = malloc(sizeof(int));
    for (int i = 0;i < 5;i++){
        scanf("%d",n);
        arr[i] = *n;
    }
    // printf("ENTER SIZE\n");
    // int *size = malloc(sizeof(int));
    // scanf("%d",size);
    // printf("%d",*size);
    // int arr[*size];
    // printf("Enter %d digits\n",*size);
    // for (int i = 0;i < *size;i++){
    //     scanf("%d",&arr[i]);
    // }

    printf("\nPRINTING THE ARRAY\n");
    for (int i = 0;i < 5;i++)
    {
        printf("%d\n",arr[i]);
    }
    // int result;
    // result = sum(arr);
    // printf("%d",result);
}