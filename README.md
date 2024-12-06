# Trolley Problem AI

## Overview

Trolley Problem AI is an educational tool designed to spark discussions about the ethical dilemmas and controversies in artificial intelligence decision-making. Combining K-Nearest Neighbors (KNN) and Decision Tree algorithms, this program models the infamous trolley problem, allowing users to explore how AI systems handle moral quandaries.

The tool allows users to:
- Train machine learning models.
- Simulate scenarios for ethical decision-making.
- Analyze model behavior and visualize its decision-making processes.
- Provide their own ethical input via surveys.

This project is perfect for showcasing the complexities of ethics in AI and opening the floor for engaging conversations about morality in machine learning.

---

## Features

- **Train Models**  
  Train either a KNN or a Decision Tree model using a provided dataset.

- **Simulate Predictions**  
  See how the trained model would handle a random trolley problem scenario.

- **Survey User Decisions**  
  Answer ethical dilemmas yourself and feed your decisions back into the model for retraining.

- **Analysis & Reporting**  
  Generate a comprehensive analysis of model performance across multiple scenarios.

- **Visualization**  
  Visualize how the model makes decisions to gain deeper insights into its logic.

- **Customizable Scenarios**  
  Load or create custom trolley problem scenarios for specific simulations.

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/loganliddiard/Trolly-KNN
    cd Trolly-KNN
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the program:
    ```bash
    python main.py
    ```

---

## Usage

When you run the program, you'll be greeted with an ASCII banner and a list of available commands:

### Commands:
- **`train`**  
  Train a new model (KNN or Decision Tree).
  
- **`predict`**  
  See how the current model handles a random scenario.

- **`survey`**  
  Provide your own ethical choices and save them to the dataset.

- **`visualize`**  
  Display a graphical representation of the model's decision-making.

- **`load`**  
  Load or customize specific trolley problem scenarios.

- **`analysis`**  
  Run multiple simulations and analyze model behavior.

- **`exit`**  
  Exit the program.

---

## File Structure

- **`main.py`**  
  Entry point of the application.
  
- **`KNN.py`**  
  Implementation of the K-Nearest Neighbors algorithm.
  
- **`DecisionTree.py`**  
  Implementation of the Decision Tree algorithm.
  
- **`survey.py`**  
  Handles user surveys and scenarios.
  
- **`analysis.py`**  
  Tools for analyzing model performance across scenarios.

- **`dummy_data.csv`**  
  Sample dataset for testing purposes.

- **`survey.csv`**  
  Stores user-inputted decisions for training.



## Contact

For questions or suggestions, please contact:
**Logan Liddiard**  
**logan.r.liddiard@gmail.com**


