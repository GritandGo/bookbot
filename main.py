def num_of_words(booktext):
    words = booktext.split()
    return len(words)


def count_char(booktext):
    c_count = {}
    for c in booktext.lower():
        if c in c_count:
            c_count[c] += 1
        else:
            c_count[c] = 1
    return c_count


def print_report(booktext):
    character_count = count_char(booktext)
    filtered_counts = {char: count for char, count in character_count.items() if char.isalpha()} 
    
    # Convert to a list of dictionaries and sort
    sorted_counts = [{"char": char, "num": count} for char, count in filtered_counts.items()]
    sorted_counts.sort(reverse=True, key=lambda item: item["num"])

    # Build the report
    report_lines = []
    report_lines.append("--- Begin report ---")  # Header
    for entry in sorted_counts:
        report_lines.append(f"The '{entry['char']}' character was found {entry['num']} times")
    report_lines.append("--- End report ---")  # Footer

    # Return the full report as a single string
    final_report = "\n".join(report_lines)
    return final_report


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        number_of_words = num_of_words(file_contents)
        print(f"{number_of_words} words found in the document.")

        filtered_counts = print_report(file_contents)
        print(filtered_counts)

    
main()



