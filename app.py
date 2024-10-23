import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Set page options for the overall app, including a title and making it fillable
ui.page_opts(title="P1: Browser Interactive App", fillable=True)

# Create a sidebar with a slider input for controlling the number of bins in the histogram
with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram. 
    # The ui.input_slider function is called with 5 arguments:
    # 1. A string ID ("selected_number_of_bins") that uniquely identifies this input.
    # 2. A string label ("Number of Bins") to be displayed alongside the slider.
    # 3. An integer representing the minimum number of bins.
    # 4. An integer representing the maximum number of bins.
    # 5. An integer representing the initial value of the slider.
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

# Define a plot rendering function that generates and displays a histogram
@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    # Define the number of points to generate. Use optional type hinting to indicate this is an integer.
    count_of_points: int = 1000000
    # Set a random seed to ensure reproducibility.
    np.random.seed(1000)
    
    # Generate random data:
    # - np.random.randn(count_of_points) generates 'count_of_points' samples from a standard normal distribution.
    # Each sample is then scaled by 15 (to increase spread) and shifted by 100 (to center the distribution around 100).
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    
    # Create a histogram of the random data using matplotlib's hist() function:
    # The second argument specifies the number of bins, dynamically set by the input slider's current value.
    # The density parameter, when True, normalizes the histogram so that the total area under the histogram equals 1.
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color="red")
    
    # Label the x and y axes of the histogram
    plt.xlabel('Value')
    plt.ylabel('Frequency')
