def analyse(trace_file):
    instruction_pages = {}
    data_pages = {}

    with open(trace_file, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 2:
                continue

            for i in range(1, len(parts[1])):
                if parts[1][-i] == ",":
                    memory_address = parts[1][:len(parts)-i]
            page_number = hex(int(memory_address, 16) // 4096)

            if parts[0] == 'I':
                if page_number in instruction_pages:
                    instruction_pages[page_number] += 1
                else:
                    instruction_pages[page_number] = 1
            elif parts[0] in ('S', 'L', 'M'):
                if page_number in data_pages:
                    data_pages[page_number] += 1
                else:
                    data_pages[page_number] = 1

    return instruction_pages, data_pages

def print_results(page_accesses, title):
    print(title)
    for page, count in page_accesses.items():
        print(f"{page}, {count}\n")

if __name__ == "__main__":
    instruction_pages, data_pages = analyse("traces/addr-blocked.ref")
    print_results(instruction_pages, "Instructions")
    print_results(data_pages, "Data")

    instruction_pages, data_pages = analyse("traces/addr-repeatloop.ref")
    print_results(instruction_pages, "Instructions")
    print_results(data_pages, "Data")
    
    instruction_pages, data_pages = analyse("traces/addr-simpleloop.ref")
    print_results(instruction_pages, "Instructions")
    print_results(data_pages, "Data")
    
    instruction_pages, data_pages = analyse("traces/addr-matmul.ref")
    print_results(instruction_pages, "Instructions")
    print_results(data_pages, "Data")