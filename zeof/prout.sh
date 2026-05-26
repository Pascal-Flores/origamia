#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./render_all.sh /chemin/vers/repertoire /chemin/vers/blockly_svg_cli.js
#
# Example:
#   ./render_all.sh ./programmes ./blockly_svg_cli.js

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <source_dir> <cli_script> [extra args...]"
  exit 1
fi

SOURCE_DIR=$1
CLI_SCRIPT=$2
shift 2

find "$SOURCE_DIR" -type f -name '*.txt' | while IFS= read -r input; do
  output="${input%.txt}.svg"
  echo "Rendering: $input -> $output"
  node "$CLI_SCRIPT" "$input" -o "$output" "$@"
done