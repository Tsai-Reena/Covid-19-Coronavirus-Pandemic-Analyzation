# Covid-19-Coronavirus-Pandemic-Analyzation

## Background  
Coronavirus disease 2019 (COVID-19(, also known as severe special infectious pneumonia, is an infectious disease caused by SARS-CoV-2. Since it was first diagnosed in Wuhan, Hubei Province, China in late 2019, it has spread rapidly and the epidemic has spread to countries around the world. The number of infections and deaths is high, and it is still spreading, and it is not known when it will stop. It is arguably the most serious challenge facing humanity since the Second World War.  

1. Data Scource  
Kaggle: [COVID-19. Exploratory Data Analysis](https://www.kaggle.com/code/georgyzubkov/covid-19-exploratory-data-analysis/data)  
2. Objective  
COVID-19 is already a global disease that cannot be separated from its effects on human societies everywhere in the world. This resource set contains information on countries, regions, and the impact of the coronavirus. By analyzing the correlation of this information, we hope to understand the spread and role of the epidemic in different parts of the world, and discuss the possible causes accordingly.  


## Data Analysis
1. **Data Preperation**  
    - Missing Values Processing
    - Data Scaling
2. **Summary of the Data**
    - DataFrame Information
    - DataFrame Statistical Information
  
  
## Data Visualization
1. Use the **scatter plot** to plot the population of different countries for the Country and Population:  
    As can be seen from the data, the number of countries is huge, so the population of each country is plotted one by one in the form of a scatter chart.  
    <img src="./images/01.png" width="80%">  
    $\implies$ It can be found that the population of each country in this data is different, and the difference between the most populous and least populous countries is even $10^3$ times.
2. Use the **bar chart** to plot the data value size of different continents and regions for different continents and each field:  
    - Population v.s. Continent
    <img src="./images/02.png" width="80%">  
      
    - Total Cases v.s. Continent
    <img src="./images/03.png" width="80%">  
      
    - Total Deaths v.s. Continent
    <img src="./images/04.png" width="80%">  
      
    $\implies$ The chart of total cases and total deaths is similar in shape, indicating that the fatality rate of the virus does not vary by region. South America, on the other hand, has a much higher number of deaths than the number of infections, which may indicate that the number of infections recorded is not close to the facts.  
    $\implies$ The "Total Cases v.s. Continent" chart shows that among all the cases in the continent, Europe has the largest number of cases, which even surpasses Asia, the birthplace of Covid-19. It may be due to the degree of internationalization in Europe, and as the birthplace, Asia's epidemic prevention measures are more timely, which also leads to the largest number of cases in Europe in the figure above.  
    $\implies$ Africa has the second largest population, but the number of infections and deaths is the bottom. The possible reasons are as follows:
    >> The government has put less effort into keeping track of the coronavirus figures.
    >> The economic model is different from other continents. There is less interaction between traffic and interaction, and the virus is more difficult to spread.
