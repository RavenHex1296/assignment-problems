#include <iostream>
#include <cassert>

int calcSum(int m, int n){
  int ascendingMatrix[m][n];
  int ascendingMatrixEntry = 1;
  int descendingMatrix[n][m];
  int descendingMatrixEntry = m*n;
  int productMatrix[m][m];
  int sum = 0;

  for (int row = 0; row < m; row++)
  {
    for (int column = 0; column < n; column++)
    {
      ascendingMatrix[row][column] = ascendingMatrixEntry;
      ascendingMatrixEntry += 1;
    }
  }

  for (int row = 0; row < n; row++)
  {
    for (int column = 0; column < m; column++)
    {
      descendingMatrix[row][column] = descendingMatrixEntry;
      descendingMatrixEntry -= 1;
    }
  }

  for (int row = 0; row < m; row++)
  {
    for (int column = 0; column < m; column++)
    {
      for (int num = 0; num < n; num++)
      {
        productMatrix[row][column] += ascendingMatrix[row][num] * descendingMatrix[num][column];
      }
       sum += productMatrix[row][column];
    }
  }

  return sum;
}

int main() {
    assert(calcSum(2, 3)==131);
    std::cout << "PASSED";
}