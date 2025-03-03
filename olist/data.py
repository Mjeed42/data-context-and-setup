import os
import pandas as pd



class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities


        csv_path = os.path.join(os.path.dirname(__file__) , "..", "data" ,"csv")

        pd.read_csv(os.path.join(csv_path, 'olist_sellers_dataset.csv')).head()
        self.file_names = ['olist_customers_dataset.csv'
        ,'olist_geolocation_dataset.csv'
        ,'olist_order_items_dataset.csv'
        ,'olist_order_payments_dataset.csv'
        ,'olist_order_reviews_dataset.csv'
        ,'olist_orders_dataset.csv'
        ,'olist_products_dataset.csv'
        ,'olist_sellers_dataset.csv'
        ,'product_category_name_translation.csv' ]

        self.key_names = []

        for i in self.file_names:
         clear = i.removeprefix("olist_").removesuffix("_dataset.csv").removesuffix(".csv")
         self.key_names.append(clear)

         data = {}

        for x, y in zip(self.key_names, self.file_names):
            data[x]= pd.read_csv(os.path.join(csv_path, y))


        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
