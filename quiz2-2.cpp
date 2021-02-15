# include <iostream>
# include <cassert>

int seqSum(int n)
{
  int sequenceSum = 0;

  if (n == 0)
  {
    return sequenceSum;
  }

  int terms[n + 1];
  terms[0] = 0;
  terms[1] = 1;

  sequenceSum += terms[0] + terms[1];

  for (int i = 2; i <= n; i++)
  {
    terms[i] = terms[i - 1] + 2 * terms[i - 2];
    sequenceSum +=  terms[i - 1] + 2 * terms[i - 2];
  }

  return sequenceSum;
}

int extendedSeqSum (int n)
{
  int extendedSum = 0;

  if (n == 0)
  {
    return extendedSum;
  }

  int terms[n + 1];
  terms[0] = 0;
  terms[1] = 1;

  for (int i = 2; i <= n; i++)
  {
    terms[i] = terms[i - 1] + 2 * terms[i - 2];
  }

  int extendedTerms[terms[n] + 1];
  extendedTerms[0] = 0;
  extendedTerms[1] = 1;
  extendedSum += extendedTerms[0] + extendedTerms[1];

  for (int i = 2; i <= extendedTerms[n]; i++)
  {
    extendedTerms[i] = extendedTerms[i - 1] + 2 * extendedTerms[i - 2];
    extendedSum += extendedTerms[i];
  }

  return extendedSum;

}

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

    return 0;
}