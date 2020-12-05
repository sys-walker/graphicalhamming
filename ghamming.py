import sys, re


class Matrix(object):
    @classmethod
    def transpose(cls, a):
        return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


class Hamming():
    def __str__(self):
        pass

    def __init__(self, binary_string: str, option: str):
        self.binary_string = binary_string.replace(" ", "")
        self.option = option.upper()
        self.header = None
        self.table = None
        self.footer = None
        self.error_bit = None

    def start(self):

        if self.option == "E":
            self.encode()
        elif self.option == "D":
            self.decode()
        else:
            print("Unknown option")

    def is_binary_str_format(self, binary_string):
        return not bool(re.compile(r'[^0-1]').search(binary_string))

    def find_parity_bits(self, binary_string=None, hamming_length=0):
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

    def get_hamming_table_header(self, binary_string, hamming_length):
        header = []
        if len(binary_string) == hamming_length:
            header = list(binary_string)
            bit = 1
            for i in range(len(header)):
                if i == bit - 1:
                    header[i] = "P"
                    bit = bit << 1

            return header
        bp = 1
        str_itr = 0
        for i in range(hamming_length):
            if i == bp - 1:
                header.append("P")
                bp = bp << 1
            else:
                header.append(binary_string[str_itr])
                str_itr += 1
        return header

    def get_hamming_table(self, header_table, hamming_length, n_parity):
        """
        for parity bit position n
        * jump (n-1)
        loop:
            * check n bits if not data then ignore
            * jump n bits
        repeat until end of table rows
        """

        table = self.generate_table(hamming_length, n_parity)

        self.compute_hamming_table(table, header_table)

        self.clean_up_table(table)

        return table

    def generate_table(self, hamming_length, n_parity):
        # ------------------- sets "b" into parity bits columns -------------------
        table = [["*" for _ in range(hamming_length)] for _ in range(n_parity)]
        for row in table:
            bit_paridad = 1
            for j in range(len(row)):
                if j == bit_paridad - 1:
                    row[j] = "b"
                    bit_paridad = bit_paridad << 1

        return table

    def compute_hamming_table(self, table, header_table):
        # ------------------- sets bits according to the header's table if they are data -------------------
        bit = 1
        for row in table:
            jump = bit
            ign = True
            for i in range(jump - 1, len(row), jump):

                ign = False if (ign == True) else True

                if ign == False:
                    for index in range(i, i + jump):
                        if index >= len(row):
                            break
                        if row[index] != "b":
                            row[index] = int(header_table[index])

            bit = bit << 1
        self.put_parity_bits(table)

    def put_parity_bits(self, table):
        # ------------------- Sets the parity bits for each row -------------------
        i = 0
        bit_pos = 1
        for row in table:
            table[i][(bit_pos - 1)] = row.count(1) % 2
            i += 1
            bit_pos = bit_pos << 1

    def clean_up_table(self, table):
        # ------------------- cleans up "b" of hamming table columns -------------------
        for row in table:
            for j in range(0, len(row)):
                if row[j] == "*" or row[j] == "b":
                    row[j] = " "

    def get_hamming_table_footer(self, table):
        footer = []
        for row in Matrix.transpose(table):
            footer.append("1" if 1 in row else "0")
        return footer

    def print_table(self, header=None, table=None, footer=None):
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

    def encode(self):
        if len(self.binary_string) == 0:
            sys.exit("No data bits were found!")
        if not self.is_binary_str_format(self.binary_string):
            sys.exit("Not a string of {0,1}!")

        hamming_length, n_parity = self.find_parity_bits(self.binary_string)

        self.header = self.get_hamming_table_header(self.binary_string, hamming_length)

        self.table = self.get_hamming_table(self.header, hamming_length, n_parity)

        self.footer = self.get_hamming_table_footer(self.table)

        self.print_table(self.header, self.table, self.footer)

    def decode(self):

        if len(self.binary_string) == 0:
            sys.exit("No encoded data were found!")
        if not self.is_binary_str_format(self.binary_string):
            sys.exit("Not hamming encode was found!")

        n_parity = self.find_parity_bits(hamming_length=len(self.binary_string))

        self.header = self.get_hamming_table_header(self.binary_string, hamming_length=len(self.binary_string))

        self.table = self.get_hamming_table(self.header, hamming_length=len(self.binary_string), n_parity=n_parity)

        self.footer = self.get_hamming_table_footer(self.table)

        self.print_table(self.header, self.table, self.footer)

        self.error_bit = self.get_error_hamming(self.binary_string, self.footer)

        if self.error_bit == -1:
            print("No errors were found")
        else:
            print("error at bit num=", self.error_bit)

    def get_error_hamming(self, received, decoded):
        err = []
        enc = self.get_hamming_parity_code(received)
        dec = self.get_hamming_parity_code(decoded)
        for i in range(len(enc)):

            if enc[i] == dec[i]:
                err.append("0")
            else:
                err.append("1")

        return -1 if int("".join(err), 2) == 0 else int("".join(err), 2)

    def get_hamming_parity_code(self, received):
        bit = 1
        dataLen = len(received)
        s = []
        while bit < dataLen + 1:
            s.append(received[bit - 1])
            bit = bit << 1

        return list(reversed(s))


if __name__ == '__main__':
    option = input("E [Encode], D [Find Errors]\n>")
    binary_string = input("Enter binary string code >")
    s = Hamming(binary_string, option)
    s.start()
