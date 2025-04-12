flag = "LKSJ{fake_flag_jangan_disubmit}"

numbers = "0123456789"
big_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alphabet = "abcdefghijklmnopqrstuvwxyz"
possible_flag_printable = "{}_?!@"

transformed = ""
for i in range(len(flag)):
	if flag[i].isupper():
		transformed += big_alphabet[(big_alphabet.index(flag[i]) - i) % len(big_alphabet)]
	elif flag[i].islower():
		transformed += small_alphabet[(small_alphabet.index(flag[i]) - i) % len(small_alphabet)]
	else:
		transformed += possible_flag_printable[(possible_flag_printable.index(flag[i]) - i) % len(possible_flag_printable)]

print(transformed)

# Transformed = LJQG_ycw{pej_gqwv?ul{ys?lvss!zdvhzw?jws@ytxda@osxr{qltq_@