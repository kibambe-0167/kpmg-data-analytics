# gengder column.
- the samples are not consistent. happen to find 'F', 'M', which are clear for female and male respectively. but 'U', in unclear where its belongs. sample distribution: {'F': 1, 'Male': 1872, 'Female': 2037, 'U': 88, 'Femal': 1, 'M': 1}


# past_3_years_bike_related_purchases
- all good.

# date column.
- {'1843-12-21': 1} found a sample year with the following year, not valid.
- dates months and days are within ranges.

# job_title
- there is more than 500 missing(nan) job titles in the dataset.


# job_industry_category
- there is a lot of missing(nan) values in the datasets.
- feature sample distribution: {'Telecommunications': 72,
 'Argiculture': 113,
 'Entertainment': 136,
 'IT': 223,
 'Property': 267,
 'Retail': 358,
 'Health': 602,
 nan: 656,
 'Financial Services': 774,
 'Manufacturing': 799}

# wealth_segment
- all good on this feature sample

# deceased_indicator
- unique: ['N' 'Y']
- data distribution: {'Y': 2, 'N': 3998}

# default
- i am confused by this feature.
- 

# owns_car
- feature sample shape: (4000,)
- unique values: ['Yes' 'No']
- data distribution: {'No': 1976, 'Yes': 2024}

# tenure
- might be the tensure of the bicycle, most of the values are missing(nan)
- 