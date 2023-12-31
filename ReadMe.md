# A simple house price calculator app 


The house price calculator is an [OLS](https://en.wikipedia.org/wiki/Ordinary_least_squares) model trained on the "House Prices - Advanced Regression Techniques" from Kaggle. If interested in how the model was created check the section "Creating a simplified linear model" in [my notebook](https://www.kaggle.com/code/asmailabdulkarim/house-prices-advanced-regression-techniques/edit). 

The web app is built using [Dash](https://dash.plotly.com/) and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/index.html).
The model is based on Scikit-Learn and uses 8 inputs:


- Have a fire place.
- Have a wood deck.
- Have a porch.
- Size of above grade (ground) living area in square feet.
- Size of garage in square feet.
- Size of basement area in square feet.
- Original construction date.
- Total number of bathrooms.

####  Build the web app (on linux)
run `./create_app.sh`

#### Run the web app
run `./dist/run` 

## Sources
Dataset: <https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques>.

App icon: <https://www.freepik.com/icon/loan_2721134>.
