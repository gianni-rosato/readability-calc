import argparse
import nltk
from readability import Readability

nltk.download("punkt")
nltk.download('punkt_tab')

# ANSI color codes
class Color:
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

def calculate_readability_scores(text: str) -> list[float]:
    r = Readability(text)

    results: list[float] = []

    fk = r.flesch_kincaid()
    fl = r.flesch()
    gf = r.gunning_fog()
    cl = r.coleman_liau()
    dc = r.dale_chall()
    ar = r.ari()
    lw = r.linsear_write()
    # sg = r.smog()
    sp = r.spache()

    results.append(float(fk.score))
    results.append(float(fl.score))
    results.append(float(gf.score))
    results.append(float(cl.score))
    results.append(float(dc.score))
    results.append(float(ar.score))
    results.append(float(lw.score))
    try:
        results.append(float(r.smog().score))
    except:
        results.append(0.0)
    results.append(float(sp.score))

    return results

def calculate_readability_grades(text: str) -> list[str]:
    r = Readability(text)

    results: list[str] = []

    fk = r.flesch_kincaid()
    fl = r.flesch()
    gf = r.gunning_fog()
    cl = r.coleman_liau()
    dc = r.dale_chall()
    ar = r.ari()
    lw = r.linsear_write()
    # sg = r.smog()
    sp = r.spache()

    results.append(fk.grade_level)
    results.append(fl.grade_levels[0])
    results.append(gf.grade_level)
    results.append(cl.grade_level)
    results.append(dc.grade_levels[0])
    results.append(ar.grade_levels[0])
    results.append(lw.grade_level)
    try:
        results.append(r.smog().grade_level)
    except:
        results.append("n/a")
    results.append(sp.grade_level)

    return results



def main():
    parser = argparse.ArgumentParser(description="Calculate various readability scores for a piece of text using py-readability-metrics")
    parser.add_argument("input", help="Source text input for readability analysis")
    parser.add_argument("output", help="Output CSV file for readability results")
    args = parser.parse_args()
    input = args.input
    output = args.output

    with open(input, "r") as file:
        text: str = file.read()

    print(f"Reading file {input} and calculating readability scores ...")

    results: list[float] = calculate_readability_scores(text)

    print(f"{Color.BOLD}Readability Scores{Color.RESET}:")
    print("Flesch-Kincaid:\t", results[0])
    print("Flesch:\t\t", results[1])
    print("Gunning Fog:\t", results[2])
    print("Coleman-Liau:\t", results[3])
    print("Dale-Chall:\t", results[4])
    print("ARI:\t\t", results[5])
    print("Linsear Write:\t", results[6])
    print("SMOG:\t\t", results[7])
    print("Spache:\t\t", results[8])

    results_grades: list[str] = calculate_readability_grades(text)

    print(f"{Color.BOLD}Readability Grades{Color.RESET}:")
    print("Flesch-Kincaid:\t", results_grades[0])
    print("Flesch:\t\t", results_grades[1])
    print("Gunning Fog:\t", results_grades[2])
    print("Coleman-Liau:\t", results_grades[3])
    print("Dale-Chall:\t", results_grades[4])
    print("ARI:\t\t", results_grades[5])
    print("Linsear Write:\t", results_grades[6])
    print("SMOG:\t\t", results_grades[7])
    print("Spache:\t\t", results_grades[8])

    # Open file and write results as CSV
    with open(output, "w") as csv:
        csv.write(f"Readability Scores for {input}\n")
        csv.write("Type, Flesch-Kincaid, Flesch, Gunning Fog, Coleman-Liau, Dale-Chall, Automated Readability Index, Linsear Write, SMOG, Spache\n")
        csv.write(f"Score, {results[0]}, {results[1]}, {results[2]}, {results[3]}, {results[4]}, {results[5]}, {results[6]}, {results[7]}, {results[8]}\n")
        csv.write(f"Grade, {results_grades[0]}, {results_grades[1]}, {results_grades[2]}, {results_grades[3]}, {results_grades[4]}, {results_grades[5]}, {results_grades[6]}, {results_grades[7]}, {results_grades[8]}\n")




if __name__ == "__main__":
    main()
