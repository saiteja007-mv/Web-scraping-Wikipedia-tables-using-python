import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_districts_in_India"
tables = pd.read_html(url)
type(tables)
