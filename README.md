# NCAA Team Financial Analysis
## Overview
This project is a short analysis of NCAA sports teams. Data is taken from Equity in Athletics Data Analysis 2022 (EADA), found at https://ope.ed.gov/athletics/#/datafile/list. I was curious to see how funding was allocated to different sports teams at different schools (particularly to investigate gender parity in funding), and to see what sort of revenue these teams brought in.

While this data set is highly imperfect and does not show the full financial impact of sports teams at their respective institutions, it was the best set redily available, and seems to be generally accurate.

I focused on a few schools that were personally significant to me, in addition to the country as a whole.

## Data
The data was recievd in the form of a .xlsx file, which I converted to a .csv file. The data was then read into a Pandas dataframe.

The data is imperfect at best, as it does not include secondary donations, increased recognition, and other factors that sports teams bring to their respective institutions. Additionally, many schools have team expenses exactly equal to their revenue, meaning that the reporting is likely not exactly accurate.

https://ope.ed.gov/athletics/#/datafile/list

## Initial Findings
Men's football and basketball are the two sports that most consistently bring in positive net revenue to universities. This is not surprising, as these are the two most popular sports in the NCAA. What was surprising, however, was that at a large number of schools, these two sports were the only ones that brought in positive net revenue, and were enough to offset the negative net profit of all other sports.

While it is ***highly likely*** that this dataset does not consider the secondary donations, effects of increased recognition, and other factors that sports teams bring to their respective institutions, it is still interesting to see that the magnitude to which most collegiate sports teams are not profitable on their own.

## Next Steps
Next steps include looking at each sport individually, and clustering schools to see which schools are similar in athletic programs. I would like to see if there is a correlation between funding and success in a program.

I also want to look at historical EADA data to see how funding has changed over time. Additionally, I would like to look at the impact of COVID-19 on funding, and to see how it reshaped the landscape of collegiate sports.