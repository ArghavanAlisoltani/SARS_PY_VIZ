## Collection of Python scripts for SARS-CoV-2 interactive data visualization


#### This repository contains Python scripts that provide interactive visualizations of SARS-CoV-2 sequencing data. The visualizations are created using Plotly, a popular graphing library for making interactive plots.

---
### Library installation

You can install the necessary libraries using pip.
For instance, copying the below code in the terminal results in the installation of pandas and plotly libraries

```
pip install pandas plotly
```

---
## Usage
Place your data in the root of this repository see the example data. 
The data should be in a tab-separated format (TSV) and named your_data_file.tsv.
Run the script of interest with the following command format:

```
python 1-StackedBar.py /path/to/input_file.tsv /path/to/output_file.html
```

---
### Overview of Scripts 

#### 1- StackedBar.py 
The script processes data to display lineage distribution over time in the form of stacked bars specifically highlighting the count and percentage of different virus lineages over time. 

#### Data Format
The script expects a TSV file with the following key columns:

Collection date: The date of sample collection.
Lineage: The identified lineage of the SARS-CoV-2 from each sample. 

** Ensure your data adheres to this format to avoid processing errors. **

---

#### 2- AreaChart.py 
The script processes data to display lineage distribution over time in the form of stacked bars specifically highlighting the count and percentage of different virus lineages over time

#### Data Format
The script expects a TSV file with the following key columns:

Collection date: The date of sample collection.
Lineage: The identified lineage of the SARS-CoV-2 from each sample. 

** Ensure your data adheres to this format to avoid processing errors. **

---
### Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
