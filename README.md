# Algorithm Performance Dashboard

An interactive Dash app that generates random datasets and compares the real execution time of four search strategies side by side.

**Stack:** Python · Dash · Plotly · Bootstrap

| Algorithm | Time complexity |
|---|---|
| Linear search | O(n) |
| Binary search | O(log n), needs sorted input |
| Binary search tree | O(log n) average, O(n) worst case |
| Red-black tree | O(log n) guaranteed (self-balancing) |

## Quickstart

```bash
git clone https://github.com/devdalal2002/algorithm-performance-dashboard.git
cd algorithm-performance-dashboard/project
pip install -r requirements.txt
python app.py        # open http://127.0.0.1:8050
```

Choose a dataset size, generate the numbers, pick a target, and run all four algorithms to compare their timings.

More detail is in [`project/README.md`](project/README.md).
