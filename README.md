### **Requirements**
- Python 3 (tested on versions 3.9 and 3.10 on mac/windows)
- Required packages:
1. [pandas](https://pandas.pydata.org/docs/getting_started/install.html) (command: `pip install pandas`)
2. [msoffcypto](https://github.com/nolze/msoffcrypto-tool) (command: `pip install msoffcrypto-tool`)
3. [streamlit](https://streamlit.io) (command: `pip install streamlit`)
4. [numpy](https://numpy.org/install/) (command: `pip install numpy`)


to run the script, either 
1. enter `python3 find_it.py` in terminal (mac) or cmd (windows)
2. use right click on the asp_visual.py file and launch with **python launcher** 


### This script has two function options
* Process Epic exported file
  * first prompt will ask for number of files to be processed/combined.
  * (this is due to limitations of Epic Find Susceptibility Report limiting to 6 months.)
  * Then enter path to the first file, password, then repeat for all reports.
  * Script will perform data transformation and export out two dataframes:
    * gram positives (first specimen removed)   
  * Finally, enter path to procssed file, 
