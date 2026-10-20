def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	result=[]
	row_len=len(matrix)
	col_len=len(matrix[0])
	if mode=='column':
		for i in range(col_len):
			temp_sum=0
			for j in range(row_len):
				temp_sum+=matrix[j][i]

			result.append(temp_sum/row_len)

	elif mode=='row':
		for i in range(row_len):
			temp_sum=0
			for j in range(col_len):
				temp_sum+=matrix[i][j]

			result.append(temp_sum/col_len)
			

	return result