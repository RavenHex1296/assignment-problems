def calculate_coefficients(self):
    coefficients_dict = {}
    system_of_equations = [[1 for x in list(self.df.data_dict.values())[0][0]]]
    independent_variables = {}

    for key in self.df.data_dict:
      if key != self.dependent_variable:
        independent_variables[key] = self.df.data_dict[key]

    for row in range(len(independent_variables)):
      system_of_equations.append(list(self.df.data_dict.values())[row][0])

    sys_matrix = Matrix(system_of_equations)
    tr  ansposed_matrix = sys_matrix.transpose()
    mat_mult = transposed_matrix @ sys_matrix.transpose()
    pseudoinverse = mat_mult.inverse() @ transposed_matrix
    multiplier = [[num] for num in list(self.df.data_dict.values())[1][0]]
    multiplier_mat = pseudoinverse @ Matrix(multiplier)

    for num in range(len(multiplier_mat.elements)):
      if num == 0:
        key = 'constant'

      else:
        key = list(self.df.data_dict.keys())[num-1]

      coefficients_dict[key] = [row[0] for row in multiplier_mat.elements][num]

    return coefficients_dict
