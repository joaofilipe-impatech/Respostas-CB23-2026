import AulasPraticas.AP_03_ordenacao as ap3
import random
import time
import sys

LIST_LENGTHS = [100, 500, 1000, 5000]
REC_LIMIT = 10050
SEED = 1001

def avg_case(N):
    return random.sample(range(1,N+1), N)

def worst_case_quick(N):
    return [x for x in range(N)][::-1]

def test(sorting_method, case, list_len, repeat=1):
    times = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        sorting_method(case(list_len))
        t = time.perf_counter()
        times.append(t - t0)

    return sum(times)/repeat

CASES = [avg_case, worst_case_quick]
METHODS = [ap3.selection_sort, ap3.divide_and_conquer_sort, ap3.quick_sort]

sys.setrecursionlimit(REC_LIMIT)
random.seed(SEED)

times = dict()

for length in LIST_LENGTHS:
    times[length] = dict()
    for case in CASES:
        times[length][case.__name__] = dict()
        for method in METHODS:
            times[length][case.__name__][method.__name__] = test(method, case, length, 50)

for case in CASES:
    method_names = [method.__name__ for method in METHODS]

    headers = [str(length) for length in LIST_LENGTHS]

    values = {
        method.__name__: [
            f"{times[length][case.__name__][method.__name__]:.12f}"
            for length in LIST_LENGTHS
        ]
        for method in METHODS
    }

    method_width = max(
        len("Método"),
        *(len(name) for name in method_names)
    )

    column_width = max(
        *(len(header) for header in headers),
        *(len(value) for row in values.values() for value in row)
    )

    total_width = (
        method_width
        + 3
        + len(headers) * column_width
        + 3 * (len(headers) - 1)
    )

    print()
    print("=" * total_width)
    print(f"{case.__name__} — tempo em segundos".center(total_width))
    print("=" * total_width)

    print(
        f"{'Método':>{method_width}} │ " +
        " │ ".join(
            f"{header:>{column_width}}"
            for header in headers
        )
    )

    print(
        "─" * method_width
        + "─┼─"
        + "─┼─".join("─" * column_width for _ in headers)
    )

    for method in method_names:
        print(
            f"{method:>{method_width}} │ " +
            " │ ".join(
                f"{value:>{column_width}}"
                for value in values[method]
            )
        )

    print("=" * total_width)