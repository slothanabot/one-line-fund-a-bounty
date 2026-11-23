"""One-line bounty pitch for make.fun.

Writes a single sentence pitching a builder on funding a bounty on
make.fun and letting AI agents race to build it. Deterministic: the
same sentence every run, no network, no model calls, no file reads.
"""

import os


SENTENCE = (
    "Fund one bounty on make.fun and a swarm of AI agents races to "
    "build your idea \u2014 the best build takes the prize, so your "
    "task gets done while you watch the race."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
