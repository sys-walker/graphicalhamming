import sys


class Matrix(object):
    @classmethod
    def transpose(cls, a):
        return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def graphic_hamming():
    binary_string = input("Enter binary code >")
    # binary_string = "0110101"

    hamming_length, n_parity = find_parity_bits(binary_string)

    header = get_hamming_table_header(binary_string, hamming_length)

    table = get_hamming_table(header, hamming_length, n_parity)

    footer = get_hamming_table_footer(table)

    print_table(header, table, footer)


def graphic_hamming_find_errors():
    received = input("Enter received binary code >")

    n_parity = find_parity_bits(hamming_length=len(received))

    header_table = get_hamming_table_header(received, hamming_length=len(received))

    ss = get_hamming_table(header_table, hamming_length=len(received), n_parity=n_parity)

    sss = get_hamming_table_footer(ss)

    print_table(header_table, ss, sss)

    get_error_hamming(received, sss)


def find_parity_bits(binary_string=None, hamming_length=0):
    if binary_string is None and hamming_length != 0:
        if hamming_length <= 2:
            sys.exit("No data bits were found!")
        bits = 1
        count = 0
        for i in range(hamming_length):
            if i == (bits - 1):
                bits = bits << 1
                count += 1
        print(hamming_length - count, "data bits found + ", count, " checker bits found")
        print("Hamming Found-> Hamming(", hamming_length - count, ",", count, ")")
        return count
    else:
        m = len(binary_string)

        # 2^k >= k+m+1
        k = 1
        while True:
            if pow(2, k) >= k + m + 1:
                break
            k = k + 1
        print(m, "data bits + ", k, " checker bits")
        print("Hamming used -> Hamming(", m, ",", k, ")")
        return k + m, k


def get_hamming_table_header(binary_string, hamming_length):
    if len(binary_string) == hamming_length:
        received = list(binary_string)
        bit = 1
        for i in range(len(received)):
            if i == bit - 1:
                received[i] = "P"
                bit = bit << 1

        return "".join(received)

    data = ""
    bp = 1
    str_itr = 0
    for i in range(hamming_length):
        if i == bp - 1:
            data += "P"
            bp = bp << 1
        else:
            data += binary_string[str_itr]
            str_itr += 1
    return data


def get_hamming_table(header_table, hamming_length, n_parity):
    """
    for parity bit positin n
    - jump (n-1)
    loop:
        check n bits if data the ignore
        jump n bits
    repeat until n<hamming_length


    :param header_table:
    :param hamming_length:
    :param n_parity:
    :return:
    """
    s = [["*" for j in range(hamming_length)] for i in range(n_parity)]

    bit = 0
    first_time = True
    itr = 1
    for row in s:
        if first_time:
            bit = 1
            first_time = False
        else:
            bit = bit << 1

        salt = bit

        # print("==================== FILA "+str(itr)+"=========================")
        ###################################

        fit = 0
        bit_paridad = 1

        while fit < len(row):
            if fit + 1 == bit_paridad:
                row[fit] = "b"
                bit_paridad = bit_paridad << 1
            fit += 1

        i = salt - 1
        ign = True
        while i < len(row):
            if ign == True:
                ign = False
            else:
                ign = True

            if ign == False:

                for index in range(i, i + salt):
                    if index >= len(row):
                        break
                    if row[index] != "b":
                        row[index] = int(header_table[index])
            i += salt

        ###################################
        itr += 1
    for row in s:
        for j in range(0, len(row)):
            if row[j] == "*" or row[j] == "b":
                row[j] = " "
    bit_pos = 1
    i = 0
    for row in s:
        # print("count ",row," ",row.count(1)%2)

        # print(i,bit_pos-1," --->")
        s[i][(bit_pos - 1)] = row.count(1) % 2
        i += 1
        bit_pos = bit_pos << 1

    return s


def get_hamming_table_footer(s):
    k = ""
    for row in Matrix.transpose(s):
        k = k + ("1" if 1 in row else "0")
    return k


def get_hamming_parity_code(received):
    bit = 1
    dataLen = len(received)
    s = []
    while bit < dataLen + 1:
        s.append(received[bit - 1])
        bit = bit << 1

    return list(reversed(s))


def get_error_hamming(received, decoded):
    err = []
    enc = get_hamming_parity_code(received)
    dec = get_hamming_parity_code(decoded)
    for i in range(len(enc)):

        if enc[i] == dec[i]:
            err.append("0")
        else:
            err.append("1")
    if int("".join(err), 2) == 0:
        print("No errors were found")
    else:
        print("error at bit num=", int("".join(err), 2))


def print_table(header=None, table=None, footer=None):
    if table is None:
        table = []
    print("\n")
    if header is not None:
        print(" ".join(list(header)))
        print("-" * len(header) * 2)
    for row in table:
        print(" ".join(list(map(str, row))))
    if footer is not None:
        print("-" * len(footer) * 2)
        print(" ".join(list(footer)))
    print("\n")


if __name__ == '__main__':

    option = input("E [Encode], D [Find Errors]\n>")
    if option.upper() == "E":
        graphic_hamming()
    elif option.upper() == "D":
        graphic_hamming_find_errors()
    else:
        print("unknown option")
