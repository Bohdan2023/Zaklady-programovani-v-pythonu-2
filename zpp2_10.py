import matice_txt_IO
M = [[111, 2, 3], [4, 5, 6], [7, 8, 99]]
matice_txt_IO.save_matrix(M, "matice.txt")
nactena_matice = matice_txt_IO.load_matrix("matice.txt")
print(nactena_matice)