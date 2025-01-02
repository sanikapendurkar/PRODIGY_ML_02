# Customer Segmentation Using K-Means Clustering

This project involves implementing a K-Means clustering algorithm to segment customers of a retail store based on their purchase history. The goal is to identify distinct customer groups to enhance targeted marketing strategies.

## About the Project

Customer segmentation is a crucial aspect of retail marketing, allowing businesses to tailor their strategies to different customer groups. In this project, we apply K-Means clustering to group customers based on their purchasing behavior, enabling more personalized marketing efforts.

## Dataset

The dataset used for this project is `mall.csv`, which contains the following columns:

- **CustomerID**: Unique identifier for each customer.
- **Gender**: Gender of the customer.
- **Age**: Age of the customer.
- **Annual Income (k$)**: Annual income of the customer in thousand dollars.
- **Spending Score (1-100)**: Spending score assigned by the mall based on customer behavior and spending nature.

## Features

- **Data Preprocessing**: Handling missing values, encoding categorical variables, and feature scaling.
- **Exploratory Data Analysis (EDA)**: Visualizing relationships between features to understand customer distribution.
- **K-Means Clustering**: Implementing the algorithm to identify distinct customer segments.
- **Cluster Visualization**: Plotting clusters to interpret and analyze customer groups.

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Jupyter Notebook or JupyterLab
- Necessary Python libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/heemit/PRODIGY_ML_02.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd PRODIGY_ML_02
   ```
  
3. **Install the required packages**:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

## Usage

1. **Open the Jupyter Notebook:**   
   ```bash
   jupyter notebook task2.py
   ```

2. **Run the cells sequentially:**
   Execute the cells in sequence to preprocess the data, train the model, and evaluate its performance.

## Results

The K-Means clustering algorithm segments customers into distinct groups based on their purchasing behavior. These segments can be visualized to understand different customer profiles, aiding in the development of targeted marketing strategies.
