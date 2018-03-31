from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    classes = ['table','table-bordered','table-sm']
    time_interval = Col('Time Interval')
    k_nearest_daily = Col('K Nearest')
    linear_perceptron = Col('Linear Perceptron')
    support_vector_machine = Col('Support Vector Machine')
    naive_bayes = Col('Naive Bayes')
    extra_trees = Col('Extra Trees Classifier')
    average = Col('Average prediction')

# Get some objects
class Item(object):
    def __init__(self, time_interval, k_nearest_daily,linear_perceptron,support_vector_machine,naive_bayes,extra_trees,average):
        self.time_interval = time_interval
        self.k_nearest_daily = k_nearest_daily
        self.linear_perceptron = linear_perceptron
        self.support_vector_machine = support_vector_machine
        self.naive_bayes = naive_bayes
        self.extra_trees = extra_trees
        self.average = average


class PredictionBuilder:

    def create_all_tables(self,predictions):
        tables = {}
        tables['FACEBOOK'] = self.create_facebook_table(predictions)
        tables['TECHNOLOGY'] = self.create_technology_table(predictions)
        tables['APPLE'] = self.create_apple_table(predictions)
        return tables

    def create_facebook_table(self,predictions):
        print('creating facebook table')

        facebook_hourly = predictions['HOUR']['facebook']
        facebook_daily = predictions['DAY']['facebook']
        facebook_weekly = predictions['WEEK']['facebook']
        facebook_monthly = predictions['MONTH']['facebook']

        # TIME INTERVAL, K NEAREST, LINEAR PERCEPTRON, SUPPORT VECTOR, NAIVE BAYES, EXTRA TREES, AVERAGE
        items = [Item('Hour', str(facebook_hourly['K_NEIGHBORS_MACHINE']),str(facebook_hourly['LINEAR_PERCEPTRON']),str(facebook_hourly['SUPPORT_VECTOR_MACHINE']),str(facebook_hourly['NAIVE_BAYES']),str(facebook_hourly['EXTRA_TREES']),str(facebook_hourly['TOTAL'])),
                Item('Day', str(facebook_daily['K_NEIGHBORS_MACHINE']),str(facebook_daily['LINEAR_PERCEPTRON']),str(facebook_daily['SUPPORT_VECTOR_MACHINE']),str(facebook_daily['NAIVE_BAYES']),str(facebook_daily['EXTRA_TREES']),str(facebook_daily['TOTAL'])),
                Item('Week', str(facebook_weekly['K_NEIGHBORS_MACHINE']),str(facebook_weekly['LINEAR_PERCEPTRON']),str(facebook_weekly['SUPPORT_VECTOR_MACHINE']),str(facebook_weekly['NAIVE_BAYES']),str(facebook_weekly['EXTRA_TREES']),str(facebook_weekly['TOTAL'])),
                Item('Month', str(facebook_monthly['K_NEIGHBORS_MACHINE']),str(facebook_monthly['LINEAR_PERCEPTRON']),str(facebook_monthly['SUPPORT_VECTOR_MACHINE']),str(facebook_monthly['NAIVE_BAYES']),str(facebook_monthly['EXTRA_TREES']),str(facebook_monthly['TOTAL']))
                ]

        table = ItemTable(items)

        return table

    def create_technology_table(self,predictions):
        print('creating technology table')

        technology_hourly = predictions['HOUR']['technology']
        technology_daily = predictions['DAY']['technology']
        technology_weekly = predictions['WEEK']['technology']
        technology_monthly = predictions['MONTH']['technology']

        # TIME INTERVAL, K NEAREST, LINEAR PERCEPTRON, SUPPORT VECTOR, NAIVE BAYES, EXTRA TREES, AVERAGE
        items = [Item('Hour', str(technology_hourly['K_NEIGHBORS_MACHINE']),str(technology_hourly['LINEAR_PERCEPTRON']),str(technology_hourly['SUPPORT_VECTOR_MACHINE']),str(technology_hourly['NAIVE_BAYES']),str(technology_hourly['EXTRA_TREES']),str(technology_hourly['TOTAL'])),
                Item('Day', str(technology_daily['K_NEIGHBORS_MACHINE']),str(technology_daily['LINEAR_PERCEPTRON']),str(technology_daily['SUPPORT_VECTOR_MACHINE']),str(technology_daily['NAIVE_BAYES']),str(technology_daily['EXTRA_TREES']),str(technology_daily['TOTAL'])),
                Item('Week', str(technology_weekly['K_NEIGHBORS_MACHINE']),str(technology_weekly['LINEAR_PERCEPTRON']),str(technology_weekly['SUPPORT_VECTOR_MACHINE']),str(technology_weekly['NAIVE_BAYES']),str(technology_weekly['EXTRA_TREES']),str(technology_weekly['TOTAL'])),
                Item('Month', str(technology_monthly['K_NEIGHBORS_MACHINE']),str(technology_monthly['LINEAR_PERCEPTRON']),str(technology_monthly['SUPPORT_VECTOR_MACHINE']),str(technology_monthly['NAIVE_BAYES']),str(technology_monthly['EXTRA_TREES']),str(technology_monthly['TOTAL']))
                ]

        table = ItemTable(items)

        return table

    def create_apple_table(self,predictions):
        print ('creating apple table')
        apple_hourly = predictions['HOUR']['technology']
        apple_daily = predictions['DAY']['technology']
        apple_weekly = predictions['WEEK']['technology']
        apple_monthly = predictions['MONTH']['technology']

        # TIME INTERVAL, K NEAREST, LINEAR PERCEPTRON, SUPPORT VECTOR, NAIVE BAYES, EXTRA TREES, AVERAGE
        items = [Item('Hour', str(apple_hourly['K_NEIGHBORS_MACHINE']),str(apple_hourly['LINEAR_PERCEPTRON']),str(apple_hourly['SUPPORT_VECTOR_MACHINE']),str(apple_hourly['NAIVE_BAYES']),str(apple_hourly['EXTRA_TREES']),str(apple_hourly['TOTAL'])),
                Item('Day', str(apple_daily['K_NEIGHBORS_MACHINE']),str(apple_daily['LINEAR_PERCEPTRON']),str(apple_daily['SUPPORT_VECTOR_MACHINE']),str(apple_daily['NAIVE_BAYES']),str(apple_daily['EXTRA_TREES']),str(apple_daily['TOTAL'])),
                Item('Week', str(apple_weekly['K_NEIGHBORS_MACHINE']),str(apple_weekly['LINEAR_PERCEPTRON']),str(apple_weekly['SUPPORT_VECTOR_MACHINE']),str(apple_weekly['NAIVE_BAYES']),str(apple_weekly['EXTRA_TREES']),str(apple_weekly['TOTAL'])),
                Item('Month', str(apple_monthly['K_NEIGHBORS_MACHINE']),str(apple_monthly['LINEAR_PERCEPTRON']),str(apple_monthly['SUPPORT_VECTOR_MACHINE']),str(apple_monthly['NAIVE_BAYES']),str(apple_monthly['EXTRA_TREES']),str(apple_monthly['TOTAL']))
                ]

        table = ItemTable(items)

        return table
