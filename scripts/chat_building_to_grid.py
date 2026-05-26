from __future__ import annotations

from pathlib import Path
import argparse
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from x2g_agent.chat import ChatAgent


def main() -> int:
    parser = argparse.ArgumentParser(description="Chat with X2G-Agent about the Building-to-Grid case.")
    parser.add_argument("--config", default="configs/building_to_grid.yaml", help="Base YAML config.")
    parser.add_argument("--backend", choices=["rule", "openai"], default="rule", help="Intent parser backend.")
    parser.add_argument("--debug", action="store_true", help="Print raw LLM responses and validation errors.")
    args = parser.parse_args()

    agent = ChatAgent(args.config, backend=args.backend, debug=args.debug)
    print(f"X2G-Agent Building-to-Grid chat ({args.backend} backend). Try: run mock Building-to-Grid")
    while True:
        try:
            user_text = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return 0
        response, should_exit = agent.handle(user_text)
        print(response)
        if should_exit:
            return 0


if __name__ == "__main__":
    raise SystemExit(main())
