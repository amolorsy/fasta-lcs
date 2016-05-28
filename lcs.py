import sys

def setup(file_path, type):
    seq_tuples = []
    f = open(file_path, "r")
    lines = [e.strip() for e in f.readlines()[1:]]
    seq_str = "".join(lines)
    for i in range(len(seq_str) / 50):
        position = i * 50
        bin_id = type + str(position)
        seq_tuples.append((bin_id, seq_str[position:(position + 100)].strip()))
    f.close()
    return seq_tuples

def lcs(a, b):
    size_a, size_b = len(a), len(b)
    lens = [[0 for j in range(size_b + 1)] for i in range(size_a + 1)]

    for i in range(size_a + 1):
        for j in range(size_b + 1):
            if i == 0 or j == 0:
                continue    
            elif a[i - 1] == b[j - 1]:
                lens[i][j] = lens[i - 1][j - 1] + 1
            else:
                lens[i][j] = max(lens[i - 1][j], lens[i][j - 1])

    lcs_str = ""
    i, j = size_a, size_b
    while (i != 0 and j != 0):
        if a[i - 1] == b[j - 1]:
            lcs_str = a[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif lens[i - 1][j] > lens[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return lcs_str

def align_by_lcs(str, lcs):
    result = ""
    i = 0
    for c in str:
        if i == len(lcs):
            result += "_"
        elif c == lcs[i]:
            result += c
            i += 1
        else:
            result += "_"
    return result

if __name__ == "__main__":
    seq_a_tuples = setup(sys.argv[1], "A")
    seq_b_tuples = setup(sys.argv[2], "B")
    
    for (x1, y1) in seq_a_tuples:
        longest_lcs_case = tuple()
        longest_lcs = ""
        for (x2, y2) in seq_b_tuples:
            result = lcs(y1, y2)
            if len(result) <= len(longest_lcs):
                continue
            else:
                longest_lcs_case = ((x1, y1), (x2, y2))
                longest_lcs = result
        output_a = align_by_lcs(longest_lcs_case[0][1], longest_lcs)
        output_b = align_by_lcs(longest_lcs_case[1][1], longest_lcs)
        print longest_lcs_case[0][0] + "," + longest_lcs_case[1][0]
        print output_a
        print output_b
    
    for (x1, y1) in seq_b_tuples:
        longest_lcs_case = tuple()
        longest_lcs = ""
        for (x2, y2) in seq_a_tuples:
            result = lcs(y1, y2)
            if len(result) <= len(longest_lcs):
                continue
            else:
                longest_lcs_case = ((x1, y1), (x2, y2))
                longest_lcs = result
        output_b = align_by_lcs(longest_lcs_case[0][1], longest_lcs)
        output_a = align_by_lcs(longest_lcs_case[1][1], longest_lcs)
        print longest_lcs_case[0][0] + "," + longest_lcs_case[1][0]
        print output_b
        print output_a
