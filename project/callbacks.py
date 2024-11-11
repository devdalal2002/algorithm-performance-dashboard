from dash import Input, Output, State
import plotly.graph_objects as go
import random
import time
from algorithms.linear_search import perform_linear_search
from algorithms.binary_search import perform_binary_search
from algorithms.binary_search_tree import insert_bst, search_bst
from algorithms.red_black_tree import RedBlackTree


def register_callbacks(app):
    
    @app.callback(
        Output("generated-numbers", "children"),
        Input("generate-btn", "n_clicks"),
        State("num-elements", "value")
    )
    def generate_numbers(n_clicks, num_elements):
        if n_clicks > 0:
            if not num_elements or num_elements <= 0:
                return "Please enter a valid number of elements"
            data = [random.randint(0, 1000) for _ in range(num_elements)]
            return f"Generated Numbers: {', '.join(map(str, data))}"
        return ""

    @app.callback(
        [
            Output("algorithm-times", "children"),
            Output("time-graph", "figure"),
            Output("size-time-graph", "figure")  
        ],
        Input("run-btn", "n_clicks"),
        [
            State("generated-numbers", "children"), 
            State("target-value", "value")
        ]
    )
    def run_algorithms(n_clicks, generated_numbers, target):
        if n_clicks > 0:
            if not generated_numbers:
                return "Please generate numbers first", {}, {}

            data = list(map(int, generated_numbers.replace("Generated Numbers: ", "").split(", ")))

            if target is None:
                return "Please enter a target value", {}, {}

            sorted_data = sorted(data)

            times = {}
            results = {}
            repetitions = 100

            
            start_time = time.perf_counter()
            for _ in range(repetitions):
                perform_linear_search(data, target)
            times["Linear Search"] = (time.perf_counter() - start_time) * 1000
            results["Linear Search"] = "Found" if perform_linear_search(data, target) != -1 else "Not Found"

            
            start_time = time.perf_counter()
            for _ in range(repetitions):
                perform_binary_search(sorted_data, target)
            times["Binary Search"] = (time.perf_counter() - start_time) * 1000
            results["Binary Search"] = "Found" if perform_binary_search(sorted_data, target) != -1 else "Not Found"

            
            bst_root = None
            for num in data:
                bst_root = insert_bst(bst_root, num)
            start_time = time.perf_counter()
            for _ in range(repetitions):
                search_bst(bst_root, target)
            times["Binary Search Tree"] = (time.perf_counter() - start_time) * 1000
            results["Binary Search Tree"] = "Found" if search_bst(bst_root, target) else "Not Found"

            
            rbt = RedBlackTree()
            for num in data:
                rbt.insert(num)
            start_time = time.perf_counter()
            for _ in range(repetitions):
                rbt.search_tree(rbt.root, target)
            times["Red-Black Tree"] = (time.perf_counter() - start_time) * 1000
            results["Red-Black Tree"] = "Found" if rbt.search_tree(rbt.root, target) != rbt.TNULL else "Not Found"

            
            time_text = "\n".join([f"{alg}: {round(time, 2)} ms, {results[alg]}" 
                                 for alg, time in times.items()])

            
            time_fig = go.Figure(data=[
                go.Bar(name=alg, x=[alg], y=[time], 
                      text=f"{round(time, 2)} ms", textposition="outside")
                for alg, time in times.items()
            ])
            time_fig.update_layout(
                title="Execution Time Comparison",
                xaxis_title="Algorithm",
                yaxis_title="Time (ms)"
            )

            
            input_sizes = [100, 500, 1000, 5000]  
            algorithm_times = {alg: [] for alg in times.keys()}
            
            for size in input_sizes:
                test_data = [random.randint(0, 1000) for _ in range(size)]
                test_sorted_data = sorted(test_data)

                
                start_time = time.perf_counter()
                for _ in range(repetitions):
                    perform_linear_search(test_data, target)
                algorithm_times["Linear Search"].append((time.perf_counter() - start_time) * 1000)

                
                start_time = time.perf_counter()
                for _ in range(repetitions):
                    perform_binary_search(test_sorted_data, target)
                algorithm_times["Binary Search"].append((time.perf_counter() - start_time) * 1000)

                
                bst_root = None
                for num in test_data:
                    bst_root = insert_bst(bst_root, num)
                start_time = time.perf_counter()
                for _ in range(repetitions):
                    search_bst(bst_root, target)
                algorithm_times["Binary Search Tree"].append((time.perf_counter() - start_time) * 1000)

                
                rbt = RedBlackTree()
                for num in test_data:
                    rbt.insert(num)
                start_time = time.perf_counter()
                for _ in range(repetitions):
                    rbt.search_tree(rbt.root, target)
                algorithm_times["Red-Black Tree"].append((time.perf_counter() - start_time) * 1000)

            
            size_time_fig = go.Figure()
            for alg, times in algorithm_times.items():
                size_time_fig.add_trace(go.Scatter(x=input_sizes, y=times, mode="lines+markers", name=alg))

            size_time_fig.update_layout(
                title="Running Time vs Input Size",
                xaxis_title="Input Size",
                yaxis_title="Time (ms)"
            )

            return time_text, time_fig, size_time_fig

        return "", {}, {}
