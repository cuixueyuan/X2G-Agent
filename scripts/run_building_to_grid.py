from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from x2g_agent.cases.building_to_grid.workflow import run_building_to_grid


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the X2G-Agent Building-to-Grid workflow.")
    parser.add_argument("--config", default="configs/building_to_grid.yaml", help="Path to YAML config.")
    args = parser.parse_args()

    final_state = run_building_to_grid(Path(args.config))
    print(f"Output root: {final_state['output_root']}")
    print("Output paths:")
    for name, path in sorted(final_state["artifacts"].items()):
        print(f"- {name}: {path}")
