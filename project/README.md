# Algorithm Performance Dashboard

An interactive web application for visualizing and comparing the performance of different search algorithms in real-time. Built with Dash and Python, this dashboard allows users to generate random datasets and compare the execution times of various search algorithms including Linear Search, Binary Search, Binary Search Tree, and Red-Black Tree.

## Features

- Interactive data generation with customizable dataset size
- Real-time performance comparison of multiple search algorithms
- Visual representation of execution times through graphs
- Support for four search algorithms:
  - Linear Search
  - Binary Search
  - Binary Search Tree (BST)
  - Red-Black Tree
- Responsive design with Bootstrap styling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/algorithm-performance-dashboard.git
cd algorithm-performance-dashboard
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix or MacOS
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
algorithm-performance-dashboard/
├── app.py                    # Main application file
├── layout.py                 # Dashboard layout definition
├── callbacks.py              # Callback functions for interactivity
├── assets/                   # Static assets
│   └── styles.css           # Custom CSS styles
├── algorithms/               # Algorithm implementations
│   ├── __init__.py
│   ├── linear_search.py
│   ├── binary_search.py
│   ├── binary_search_tree.py
│   └── red_black_tree.py
├── requirements.txt          # Project dependencies
└── README.md                # Project documentation
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://127.0.0.1:8050/`

3. Using the dashboard:
   - Enter the desired number of elements in the "Number of Elements" field
   - Click "Generate Numbers" to create a random dataset
   - Enter a target value to search for
   - Click "Run Algorithms" to execute all search algorithms
   - View the results in the graphs and execution time display

## Algorithm Implementations

### Linear Search
- Time Complexity: O(n)
- Simple iterative search through the array

### Binary Search
- Time Complexity: O(log n)
- Requires sorted array
- Divides search interval in half at each step

### Binary Search Tree
- Average Time Complexity: O(log n)
- Worst Case: O(n) if unbalanced
- Dynamic data structure

### Red-Black Tree
- Time Complexity: O(log n)
- Self-balancing binary search tree
- Guarantees balanced structure

## Development

### Adding New Algorithms

1. Create a new file in the `algorithms/` directory
2. Implement your algorithm
3. Update `callbacks.py` to include the new algorithm in performance comparisons
4. Update the layout if necessary in `layout.py`

### Modifying the UI

1. Layout changes can be made in `layout.py`
2. Custom styles can be added to `assets/styles.css`
3. New callbacks can be added in `callbacks.py`

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Future Improvements

- Add more search and sorting algorithms
- Implement algorithm visualization
- Add complexity analysis visualization
- Include memory usage metrics
- Add export functionality for results
- Add unit tests
- Implement batch testing capabilities

## Contact

Dev Dalal - dalaldev2002@gmail.com.com
Project Link: [https://github.com/devdalal2002/algorithm-performance-dashboard](https://github.com/devdalal2002/algorithm-performance-dashboard)

## Acknowledgments

- Dash documentation
- Plotly documentation
- Bootstrap documentation
