'''
1 byte = 8 bit

1 kilobyte = 1024 byte

1 megabyte = 1024 kilobyte

1 gigabyte = 1024 megabyte
'''
# reads the input.
userGB = float(input("Input a number of gigabytes: "))

# takes the integer.
gigabytes = int(userGB)

# multiplies via the 1:1024 ratio, then divides and finds the remainder which is the leftover after previosuly being allocated.
megabytes = userGB*1024%1024
kilobytes = megabytes*1024%1024
byteValue = kilobytes*1024%1024

# output the result on one line (see examples), and only takes the integer form for simplicity.
print(userGB, "GB =", int(gigabytes), "GB,", int(megabytes), "MB,", int(kilobytes), "KB,", int(byteValue) , "B")