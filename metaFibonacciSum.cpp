# include <iostream>
# include <cassert>

int metaFibonacciSum(int n)
{
    if (n < 2)
    {
      if (n < 1)
      {
        return 0;
      }
      else
      {
        return 1;
      }
    }

    int terms[n];
    terms[0] = 0;
    terms[1] = 1;

    for(int i = 2; i <= n; i++)
    {
      terms[i] = terms[i-1]+terms[i-2];
    }

    int extendedTerms[terms[n]];
    extendedTerms[0] = 0;
    extendedTerms[1] = 1;

    for (int i = 2; i <= terms[n]; i++) { 
      extendedTerms[i] = extendedTerms[i-1] + extendedTerms[i-2] + 1;
    }

    int partialSums[n];


    for (int i = 0 ; i <= n; i++) {
        int partialSum = 0;
        partialSums[i] = partialSum + extendedTerms[terms[i]];
    }

    int metaSum;

    for (int i = 0; i <= n; i++)
    {
      metaSum += partialSums[i];
    }

    return metaSum;

}

int main()
{
    std::cout << "Testing...\n";

    assert(metaFibonacciSum(6)==74);

    std::cout << "Success!";

    return 0;
}