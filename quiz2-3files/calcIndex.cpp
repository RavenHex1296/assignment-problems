# include <iostream>
# include <cassert>

int calcIndex(int n)
{
  int terms[n];
    terms[0] = 0;
    terms[1] = 1;

    for(int i = 2; i <= n; i++)
    {
      terms[i] = terms[i-1]+terms[i-2];
    }

    for(int i = 0; i <= n; i++)
    {
      if (n < terms[i])
      {
        return i;
      }
    }


}

int main()
{
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}