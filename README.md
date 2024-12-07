# Movie Sentiment Analysis with Hadoop and Python


This repository contains a project for performing sentiment analysis on movie reviews using **Hadoop Streaming**, **PySpark**, and **Python**. It uses **HDFS** for data storage, **MapReduce** for processing, and **PySpark** for parallel data handling. The goal of the project is to analyze the sentiment of movie reviews from a large dataset.

---

## Project Setup

### Step 1: Prerequisites

1. **Install Anaconda**  
   [Download and install Anaconda](https://www.anaconda.com/products/distribution) for managing the Python environment.

2. **Setup Hadoop [Single Node Cluster](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)**  
   Ensure Hadoop is installed and configured on your system. This project assumes Hadoop is running on a single-node cluster.

3. **Datasets**
   [FIrst](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv)
  [Second](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews?select=rotten_tomatoes_movie_reviews.csv)

---

### Step 2: Setup the Anaconda Environment

1. **Create and Activate Environment**

   ```bash
   conda create --name movie_sentiment
   conda activate movie_sentiment
   ```

2. **Install the required Python packages** using `pip`:
    ```bash
    pip install pandas matplotlib numpy nltk wordcloud pyspark
    ```

    - `pandas`: For data manipulation and analysis.
    - `matplotlib`: For creating static, animated, and interactive visualizations.
    - `numpy`: For numerical computations.
    - `nltk`: For natural language processing tasks.
    - `wordcloud`: For generating word clouds from text data.
    - `pyspark`: For distributed computing and processing large datasets in parallel.

3. **Execute the jupyter notebook until**
```df.to_csv('big_movies.csv', header=True, index=False)```

### Step 3: Hadoop Setup and Commands

You will need **Hadoop** and **HDFS** setup on your system. Please follow the setup instructions for installing **Hadoop** and configuring **HDFS**. After the setup, you will run the following Hadoop commands for starting the Hadoop Distributed File System (HDFS) and uploading your data:

#### Start HDFS and YARN:

1. **Start the Hadoop HDFS services**:
    ```bash
    start-dfs.sh
    ```

2. **Start the YARN services**:
    ```bash
    start-yarn.sh
    ```

#### Working with HDFS:

1. **Create a directory in HDFS for storing movie reviews**:
    ```bash
    hdfs dfs -mkdir /movies_sentiment
    ```

2. **Upload the `big_movies.csv` file from your local system to HDFS**:
    ```bash
    hdfs dfs -copyFromLocal /path/to/big_movies.csv /movies_sentiment/big_movies.csv
    ```

3. **List the files in `/movies_sentiment` directory in HDFS**:
    ```bash
    hdfs dfs -ls /movies_sentiment
    ```

4. **View the first few lines of the uploaded file**:
    ```bash
    hdfs dfs -cat /movies_sentiment/big_movies.csv | head
    ```

### Step 4: Run the Hadoop MapReduce Job for Sentiment Analysis

You can now process your data with the following **MapReduce** commands:

1. **Create the output directory in HDFS**:
    ```bash
    output_dir="/movies_sentiment/output"
    hdfs dfs -mkdir -p $output_dir
    ```

2. **Process each chunk of the data**:
    ```bash
    for chunk in $(hdfs dfs -ls /movies_sentiment/chunks/ | awk '{print $8}')
    do
        echo "Processing $chunk"
        hdfs dfs -cat $chunk | python3 ~/Documents/movies/mapper.py | sort | python3 ~/Documents/movies/reducer.py >> /tmp/output.csv
    done
    ```

3. **Upload the final output to HDFS**:
    ```bash
    hdfs dfs -put /tmp/output.csv $output_dir/output.csv
    ```

4. **Optionally, download the result to your local system**:
    ```bash
    hdfs dfs -get $output_dir/output.csv /path/to/local/output.csv
    ```

### Step 5: Execute the rest of the jupyter notebook
	
