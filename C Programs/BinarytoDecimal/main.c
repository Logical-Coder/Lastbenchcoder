#include <stdio.h>
#include <math.h>
int convert(long long n);
int main()
{       long long number;
        printf("Enter the Binary Number:");
        scanf("%lld",&number);
        printf("the converted decimal number is %d ",convert(number));
        return 0;
}
       int convert(long long n){
           int dec=0,i=0,rem;
       while(n!=0){
            rem=n%10;
            n/=10;
            dec+=rem*pow(2,i);
            ++i;

    }
    return dec;
       }



