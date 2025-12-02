f = open("input", "r")

line = f.read()
split = line.split(",")
# print(split)

id_count = 0
for i in split:
    first, second = i.split("-")

    len1 = len(first)
    len2 = len(second)

    # print(first,second)

    for j in range(int(first),int(second)+1):
        string_val = str(j)
        length = len(string_val) 
        # print(string_val, length, int(length/2)+2)


        # We have the length. No factor is bigger than length /2
        # Loop over all possible lengths 
        for k in range(2, 20):
            # print(k, "k")
            if(length % k == 0):
                # print("Factor of ", k)

                # print(int(length/k))
                # print(length, k, "LENGTH K")
                chunk_size = int(length/k)
                # print("Chunk size = ", chunk_size)
                prev_val = ""
                chunk_count = 0
                for l in range(k+1):
                    val1 = string_val[0+l*chunk_size:(l+1)*chunk_size]
                    # print(val1, "val")
                    # print(prev_val, "prev")
                    if(prev_val == val1):
                        chunk_count += 1
                        # print("We have matched the previous chunk")
                    prev_val = val1
                # print("Chunk counter = ", chunk_count)
                if(chunk_count +1  == k):
                    print("Invalid id found at ", j)
                    id_count += j
                    break



        # if(length %2 == 0):
        #     if(string_val[0:int(length/2)] == string_val[int(length/2):]):
        #         # print("Invalid")
        #         id_count += int(j)
print(id_count)

