#include<stdio.h>
int main(){
int num,i,a[16],s;//Declaring Local variables and arrays initialization array size is 16 using 16 memory location
printf("Enter the Decimal Number:");// printing text
scanf("%d",&num); // reading the decimal input

for(i=0;num>0;i++){
    a[i]=num%2;// Extracting remainder when doing divide
    num=num/2; //Dividing itself

}
s=sizeof(a)/sizeof(a[0]);
printf("The Binary number of given number: ");
for(i=i-1;i>=0;i--){


        printf("%d",a[i]);// printing reverse direction
}
return 0;
}
//code by praveen
