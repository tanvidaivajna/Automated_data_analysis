# Automated Data Analysis Report

## Dataset: goodreads.csv

### Summary Statistics

|        |   book_id |   goodreads_book_id |     best_book_id |         work_id |   books_count |         isbn |         isbn13 | authors      |   original_publication_year | original_title   | title          | language_code   |   average_rating |    ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |      ratings_4 |       ratings_5 | image_url                                                                                | small_image_url                                                                        |
|:-------|----------:|--------------------:|-----------------:|----------------:|--------------:|-------------:|---------------:|:-------------|----------------------------:|:-----------------|:---------------|:----------------|-----------------:|-----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|---------------:|----------------:|:-----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| count  |  10000    |     10000           |  10000           | 10000           |    10000      | 9300         | 9415           | 10000        |                    9979     | 9415             | 10000          | 8916            |     10000        |  10000           |      10000           |                  10000    |    10000    |    10000    |     10000   | 10000          | 10000           | 10000                                                                                    | 10000                                                                                  |
| unique |    nan    |       nan           |    nan           |   nan           |      nan      | 9300         |  nan           | 4664         |                     nan     | 9274             | 9964           | 25              |       nan        |    nan           |        nan           |                    nan    |      nan    |      nan    |       nan   |   nan          |   nan           | 6669                                                                                     | 6669                                                                                   |
| top    |    nan    |       nan           |    nan           |   nan           |      nan      |    3.757e+08 |  nan           | Stephen King |                     nan     |                  | Selected Poems | eng             |       nan        |    nan           |        nan           |                    nan    |      nan    |      nan    |       nan   |   nan          |   nan           | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| freq   |    nan    |       nan           |    nan           |   nan           |      nan      |    1         |  nan           | 60           |                     nan     | 5                | 4              | 6341            |       nan        |    nan           |        nan           |                    nan    |      nan    |      nan    |       nan   |   nan          |   nan           | 3332                                                                                     | 3332                                                                                   |
| mean   |   5000.5  |         5.2647e+06  |      5.47121e+06 |     8.64618e+06 |       75.7127 |  nan         |    9.75504e+12 | nan          |                    1981.99  | nan              | nan            | nan             |         4.00219  |  54001.2         |      59687.3         |                   2919.96 |     1345.04 |     3110.89 |     11475.9 | 19965.7        | 23789.8         | nan                                                                                      | nan                                                                                    |
| std    |   2886.9  |         7.57546e+06 |      7.82733e+06 |     1.17511e+07 |      170.471  |  nan         |    4.42862e+11 | nan          |                     152.577 | nan              | nan            | nan             |         0.254427 | 157370           |     167804           |                   6124.38 |     6635.63 |     9717.12 |     28546.4 | 51447.4        | 79768.9         | nan                                                                                      | nan                                                                                    |
| min    |      1    |         1           |      1           |    87           |        1      |  nan         |    1.9517e+08  | nan          |                   -1750     | nan              | nan            | nan             |         2.47     |   2716           |       5510           |                      3    |       11    |       30    |       323   |   750          |   754           | nan                                                                                      | nan                                                                                    |
| 25%    |   2500.75 |     46275.8         |  47911.8         |     1.00884e+06 |       23      |  nan         |    9.78032e+12 | nan          |                    1990     | nan              | nan            | nan             |         3.85     |  13568.8         |      15438.8         |                    694    |      196    |      656    |      3112   |  5405.75       |  5334           | nan                                                                                      | nan                                                                                    |
| 50%    |   5000.5  |    394966           | 425124           |     2.71952e+06 |       40      |  nan         |    9.78045e+12 | nan          |                    2004     | nan              | nan            | nan             |         4.02     |  21155.5         |      23832.5         |                   1402    |      391    |     1163    |      4894   |  8269.5        |  8836           | nan                                                                                      | nan                                                                                    |
| 75%    |   7500.25 |         9.38223e+06 |      9.63611e+06 |     1.45177e+07 |       67      |  nan         |    9.78083e+12 | nan          |                    2011     | nan              | nan            | nan             |         4.18     |  41053.5         |      45915           |                   2744.25 |      885    |     2353.25 |      9287   | 16023.5        | 17304.5         | nan                                                                                      | nan                                                                                    |
| max    |  10000    |         3.32886e+07 |      3.55342e+07 |     5.63996e+07 |     3455      |  nan         |    9.79001e+12 | nan          |                    2017     | nan              | nan            | nan             |         4.82     |      4.78065e+06 |          4.94236e+06 |                 155254    |   456191    |   436802    |    793319   |     1.4813e+06 |     3.01154e+06 | nan                                                                                      | nan                                                                                    |

### Missing Values

|                           |    0 |
|:--------------------------|-----:|
| book_id                   |    0 |
| goodreads_book_id         |    0 |
| best_book_id              |    0 |
| work_id                   |    0 |
| books_count               |    0 |
| isbn                      |  700 |
| isbn13                    |  585 |
| authors                   |    0 |
| original_publication_year |   21 |
| original_title            |  585 |
| title                     |    0 |
| language_code             | 1084 |
| average_rating            |    0 |
| ratings_count             |    0 |
| work_ratings_count        |    0 |
| work_text_reviews_count   |    0 |
| ratings_1                 |    0 |
| ratings_2                 |    0 |
| ratings_3                 |    0 |
| ratings_4                 |    0 |
| ratings_5                 |    0 |
| image_url                 |    0 |
| small_image_url           |    0 |

### Correlation Matrix

|                           |    book_id |   goodreads_book_id |   best_book_id |    work_id |   books_count |      isbn13 |   original_publication_year |   average_rating |   ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |   ratings_4 |   ratings_5 |
|:--------------------------|-----------:|--------------------:|---------------:|-----------:|--------------:|------------:|----------------------------:|-----------------:|----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|------------:|------------:|
| book_id                   |  1         |           0.115154  |      0.104516  |  0.113861  |    -0.263841  | -0.011291   |                  0.0498747  |      -0.0408798  |     -0.373178   |          -0.382656   |               -0.419292   | -0.239401   |  -0.345764  |  -0.413279  |  -0.407079  | -0.332486   |
| goodreads_book_id         |  0.115154  |           1         |      0.96662   |  0.929356  |    -0.164578  | -0.048246   |                  0.13379    |      -0.0248484  |     -0.073023   |          -0.0637601  |                0.118845   | -0.0383752  |  -0.0565712 |  -0.075634  |  -0.0633104 | -0.0561447  |
| best_book_id              |  0.104516  |           0.96662   |      1         |  0.899258  |    -0.15924   | -0.0472525  |                  0.131442   |      -0.021187   |     -0.0691819  |          -0.0558346  |                0.125893   | -0.0338938  |  -0.0492842 |  -0.0670141 |  -0.054462  | -0.0495245  |
| work_id                   |  0.113861  |           0.929356  |      0.899258  |  1         |    -0.109436  | -0.0393198  |                  0.107972   |      -0.0175554  |     -0.0627204  |          -0.0547121  |                0.0969853  | -0.0345903  |  -0.0513668 |  -0.0667459 |  -0.0547754 | -0.0467453  |
| books_count               | -0.263841  |          -0.164578  |     -0.15924   | -0.109436  |     1         |  0.0178649  |                 -0.321753   |      -0.0698883  |      0.324235   |           0.333664   |                0.198698   |  0.225763   |   0.334923  |   0.383699  |   0.349564  |  0.279559   |
| isbn13                    | -0.011291  |          -0.048246  |     -0.0472525 | -0.0393198 |     0.0178649 |  1          |                 -0.00461214 |      -0.0256669  |      0.00890359 |           0.00916556 |                0.00955286 |  0.00605369 |   0.0103455 |   0.0121425 |   0.0101608 |  0.00662185 |
| original_publication_year |  0.0498747 |           0.13379   |      0.131442  |  0.107972  |    -0.321753  | -0.00461214 |                  1          |       0.0156076  |     -0.0244147  |          -0.0254478  |                0.0277841  | -0.019635   |  -0.0384716 |  -0.0424592 |  -0.0257847 | -0.0153877  |
| average_rating            | -0.0408798 |          -0.0248484 |     -0.021187  | -0.0175554 |    -0.0698883 | -0.0256669  |                  0.0156076  |       1          |      0.0449904  |           0.0450416  |                0.00748112 | -0.0779966  |  -0.115875  |  -0.0652372 |   0.0361082 |  0.115412   |
| ratings_count             | -0.373178  |          -0.073023  |     -0.0691819 | -0.0627204 |     0.324235  |  0.00890359 |                 -0.0244147  |       0.0449904  |      1          |           0.995068   |                0.779635   |  0.723144   |   0.845949  |   0.935193  |   0.978869  |  0.964046   |
| work_ratings_count        | -0.382656  |          -0.0637601 |     -0.0558346 | -0.0547121 |     0.333664  |  0.00916556 |                 -0.0254478  |       0.0450416  |      0.995068   |           1          |                0.807009   |  0.718718   |   0.848581  |   0.941182  |   0.987764  |  0.966587   |
| work_text_reviews_count   | -0.419292  |           0.118845  |      0.125893  |  0.0969853 |     0.198698  |  0.00955286 |                  0.0277841  |       0.00748112 |      0.779635   |           0.807009   |                1          |  0.572007   |   0.69688   |   0.762214  |   0.817826  |  0.76494    |
| ratings_1                 | -0.239401  |          -0.0383752 |     -0.0338938 | -0.0345903 |     0.225763  |  0.00605369 |                 -0.019635   |      -0.0779966  |      0.723144   |           0.718718   |                0.572007   |  1          |   0.92614   |   0.795364  |   0.672986  |  0.597231   |
| ratings_2                 | -0.345764  |          -0.0565712 |     -0.0492842 | -0.0513668 |     0.334923  |  0.0103455  |                 -0.0384716  |      -0.115875   |      0.845949   |           0.848581   |                0.69688    |  0.92614    |   1         |   0.949596  |   0.838298  |  0.705747   |
| ratings_3                 | -0.413279  |          -0.075634  |     -0.0670141 | -0.0667459 |     0.383699  |  0.0121425  |                 -0.0424592  |      -0.0652372  |      0.935193   |           0.941182   |                0.762214   |  0.795364   |   0.949596  |   1         |   0.952998  |  0.82555    |
| ratings_4                 | -0.407079  |          -0.0633104 |     -0.054462  | -0.0547754 |     0.349564  |  0.0101608  |                 -0.0257847  |       0.0361082  |      0.978869   |           0.987764   |                0.817826   |  0.672986   |   0.838298  |   0.952998  |   1         |  0.933785   |
| ratings_5                 | -0.332486  |          -0.0561447 |     -0.0495245 | -0.0467453 |     0.279559  |  0.00662185 |                 -0.0153877  |       0.115412   |      0.964046   |           0.966587   |                0.76494    |  0.597231   |   0.705747  |   0.82555   |   0.933785  |  1          |

### AI-Generated Insights

# Data Story: Insights into Book Ratings and Characteristics

## Summary
The dataset consists of 10,000 books with a myriad of attributes, including ratings, authorship, original publication years, and additional bibliographic details. Key metrics reveal important trends in book reception and characteristics, illuminating the landscape of reader preferences and book success.

## Key Insights

### 1. **Publication Trends and Timeline**
The books in the dataset span a significant timeline, with original publication years ranging as far back as 1750 up to 2017. 
- **Mean Publication Year**: Approximately 1982, with a notable skew towards more recent releases.
- **Median**: The median indicates that half of the books were published post-2004, suggesting a focus on more modern literature in readers' preferences.

### 2. **Authors and Popularity**
The dataset identifies an array of authors, with Stephen King being notably prominent (appearing 60 times), indicating his significant influence and popularity within the Goodreads community.
- **Centralization of Ratings**: Many books are being rated by large numbers of readers, with the most popular books capturing thousands of ratings. This centralization hints at successful marketing strategies, strong fandoms, or the author's previous accolades playing a crucial role in their continued popularity.

### 3. **Average Ratings and Variability**
- The mean average rating across the books is around **4.00**, indicating a generally positive reception from readers. 
- Ratings range markedly, (minimum `2.47`, maximum `4.82`), highlighting variability in reader experiences and potentially differing quality or engagement levels across genres or author styles.
- The standard deviation of `0.25` suggests that while most ratings cluster around the mean, some outlier books (either very disliked or exceedingly loved) contribute to a broader spectrum of ratings.

### 4. **Correlation Between Features**
A notable correlation matrix presents varied relationships between book characteristics:
- **Ratings Count vs. Work Ratings Count**: Strong positive correlation (`0.995`), indicating that books with more readers tend to accumulate higher ratings collectively.
- **Work Text Reviews Count** also shows a strong correlation with ratings count (`0.779`), hinting that books that engage readers to write reviews likely resonate well with them, contributing to the overall rating.
- Conversely, a negative correlation with `books_count` suggests that self-contained works or standalone novels garner different reader engagement compared to collections or series.

### 5. **Missing Data and Its Implications**
The dataset exhibits some missing values, particularly in the `isbn`, `isbn13`, `original_publication_year`, and `language_code` columns (with `language_code` having 1084 missing entries).
- This raises questions about the dataset's completeness and introduces potential biases in analyzing specific categories of books, particularly in global literature or multilingual works.

## Possible Implications

### Trend Observations
- The trending toward newer publications may suggest a shift in reader preferences, driven by contemporary themes and current cultural relevance.
- Authors with high visibility (like King) dominate social reading platforms, inferring a need for new authors to leverage marketing skills or social media presence to break into the mainstream.

### Opportunities for Further Research
- Investigating the causes behind outlier ratings could provide insights into genre-specific reader preferences and highlight opportunities for publishers and authors regarding marketing.
- Exploring potential biases in the data due to missing information might instigate wider studies into how different demographics engage with literature differently based on language and publication origins.

### Conclusions
The dataset illustrates the complex interplay between book characteristics and reader engagement, revealing insights into how contemporary literature is received and consumed. By leveraging these insights, publishers and authors can better strategize their work to meet reader expectations and preferences, ultimately resonating in a saturated market.

### Visualizations

![correlation_heatmap](correlation_heatmap.png)

![rating_distribution](rating_distribution.png)

