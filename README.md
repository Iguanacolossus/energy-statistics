# Energy Statistics

## The Data:
The data set that will be used in this project is called 'US Energy Statistics' and can be found [here.](https://www.kaggle.com/sohier/us-energy-statistics?select=TOTAL.json) It consists of nine JSON files:<br>
 - **Coal:** Ash content for each US state per year and import/export prices.
 - **Electric system operating data:** hourly demand for electric per state
 - **International:** annual petroleum stock per country per year
 - **Natural Gas:**
     - Weekly working underground storage by US region
     - Price and amount of monlthy re-exports to Portugal
     - Weekly and daily futures contracts
 - **Petroleum:**  Cushing, OK WTI Spot Price FOB, Daily
 - **Petroleum Imports:** Monthly imports per US region and international export location, per refinment level
 - **State energy data system:** 
    - Net interstate flow of electricity per state
    - Biomass total consumtion per state
    - Biomass inputs per state

 - **Short term energy outlook:** Quarterly Consumption and production for crude and distilled oil in different sectors internationaly
  - **Total energy:** 
     - Monthly solar energy consumption and generation in residential, and utility-scale sectors
     - Monthly transportation sector total energy consumption and CO2 emissions
     - US department of agriculture and transportation sectors total consumptions annually
     - Primary energy stock change annually
## The Raw Data:
I read the data in from the individual json files directly to a pandas data frame: Below is a snap shot of what they looked like. The top photot is the left side of the data framt and the bottom photo is the right side:<br>
<img src="images/raw1.png" alt="raw" width="250" height='75'/><img src="images/raw2.png" alt="raw" width="250" height='75'/>
<br>
In this data set there was 20 columns and so many rows it was crashing my kernal so i read in only 1000 rows. Each row has a is a data set in intself. There is a couple long sting descriptino columns, units, source, geografical region, copyright, last updated and more. there are more columns then many of the rows have entries for so there are alot on nan values. The column that actually has the data for each row is the data column. This column consists of a dictionary of years(keys) and the measurments during that year(value). some of the rows are reported quartery and some are reported annually. <br>
<br>
My baseline wranggler set of helper functions takes this imbedded data dictionay, creates a new column for each key (year) and fills each column with its associated values.



## Questions:

 - **Which state produces the most?**
 - **Statistical differences in production and usege amongst regions.**
 - **What are the "greenest" states**
 - **Compair energy demand between residential, commercial, trasportation, and agruculture and the offset of solar energy**
<br>

 *The list goes on and on*

## Techniques:
 - frequentist hypothesis testing
 - Lots of maps and graphs
 - 

## Technologies:
 - Python
    - Pandas
    - Numpy
    - Scipy
    - Matplotlib

 __________

 ## Polution

**Is Coal burning getting cleaner?**<br>
 I dug into the coal dataset and pulled out the information on coal ash percentages in diffent sectors. To give my self a summary I averaged the coal ash production produced off all the sectors , and plotted each state's/region's average over time. </b>
 ![title](images/coal-ash-ugly.png)
 </b>
**Wow is that ugly!**<br>
This plot shows me that reporting of coal ash has been very inconsistent. There are some regions that stop reporting then start again. <br>
**What happend between 2007 and 2008?**
In 2008 is when Obama took office and was pushng for cleaner energy production. This plot leads me to believe that , due to Obama being elected, energy stations had to change how they report there ash waste around that time. Or, some Bush era regulations on coal polution expired around that time. Further research is needed.<br>
**This ugly graph is worth showing because it highlights the inconsistancy of reporting, especialy in 2008, but lets look at the same exact data in a different way.**<br>
![plot](images/ave-coal-ash3.png)


<br>
Next I wanted to look at the diffent sectors but i wanted to narrow my view to clean up what im looking at. I decided to look at the mountain region of the US because that is where I live. <br>

![plot](images/mountain-ash.png)
<br>
There are few few things worth noting in this graph. On first inspection "electric utility non-cogen" appears to be missing. Upon further inspection of the data table I saw that non-cogen utility and independent power measurments of ash ar almost exactly the same every year. This make me wonder if almost all independant power producers do not use cogeneration technologies. Also reporting on electric utility plants seems to have stopped in 2012 because all values drop to zero. As a summary I would say that independant power producers, electric utility and other industrial are are not burning coal any cleaner since recording started, but the commercial and industrial is making some changes and I would love to see data in the more recient years. (Remember this is only for the mountain region of the us)
<br>
<br>
I would like to take a bigger picture approach and look at more regions , but narrow down to electric production becasue thats where most of our coal is used. 




**How about CO2 emission in the same time frame?**

![title](images/co2-res-2000.png)
</br>
As a quick peek into CO2 emissions reporting, I plotted the CO2 emissions from coal burning in the resedential sector. The data all goes to zero which support the idea that in 2008 some reporting standards were changed. 
<br>
**Lets look more boadly**<br> A good portion of our coal energy is to produce electrisity. Lets look there.
![title](images/co20coal-electric.png)

This graph is more revealing and supports the idea that emission standards changed 2008. It also reviels that those standards are working. The rate of decreas is faster then the rate of increase since reporting started.

Although the coal ash data is hard to evaluate due to the change in reporting in 2008, the new standards are really healping polution do to CO2 emissions
_____
## Renewable Energy
![title](images/renewable-production.png)<br>
This plot is the production/consumption of all the renewable energy sources in the us. The verticle line is on 2008, during the administration and policy changes. It looks like our primary renewable energy sectors, nuclear and hydroelectric kept as a consistant rate. Wind power was alreay on the rise starting in abour 2005 but it really rampted up after 2008. Was there more money being diverted in to wind or was this rise enevitable? Solar genrated power didnt make any changes in 2008 but has started to ramp up around 2013. This may be due to the technology becomeing more afordable or more efficiant. <br>

It is also a hopeful observation to see that at the curent rate solar energy production may over come hydro electric power. This is exciting becasue thereare some arguments against hydro electric power sources due to the destruction of river ecosystems and the social threats when dam construction destroys riverside commuities up streal from the damn.
<br>

**Are we anyware close to overcomeing coal plant production with any of there renewable energys?** <br>

It apears from the graph above that nuclear produces by far the most energy. Lets see how this compairs to coal fired electric plants.

![image](17yr-monthly-coal-nuc.png)

NOPE
<br>
<br>
But maybe energy is getting cleaner. What about if we look at the most recient year alone (2016)
? <br>
![image](2016-coal-nuc.png)

It looks like coal production is lower but the diffence beween coal and nuclear is just as vast.

<br>
<br>

**Maybe we can get a better picture of clean vs dirty energy by look at the percentage of each in our total energy consumtion**
![image](percent-clean.png)
YAY
