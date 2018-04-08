import sys
import boto3
from sqlalchemy import Column, Integer, String, Float
from models.result import Result
from models.database_tools import Base, create_all_tables, create_new_engine, setup_database, create_new_session

class WebsiteDatabaseWrapper:

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('predictions')
    pk_key = 'sector'
    sectors = ['apple','facebook','technology']

    def get_all_results(self):
        engine = create_new_engine('stockbot')
        Session = create_new_session(engine)
        session = Session()
        query = session.query(Result)
        articles = query.all()
        return articles

    def get_all_predictions(self):
        results = {}
        results['HOUR'] = self.get_hourly_predictions()
        results['DAY'] = self.get_daily_predictions()
        results['WEEK'] = self.get_weekly_predictions()
        results['MONTH'] = self.get_monthly_predictions()
        return results

    def get_hourly_predictions(self):
        company_predictions = {}
        for sector in self.sectors:
            predictions = {}
            response = self.table.get_item(Key={self.pk_key: sector})
            predictions['TOTAL'] = response['Item']['total_average_hourly']
            predictions['NAIVE_BAYES'] = response['Item']['naive_bayes_hourly']
            predictions['SUPPORT_VECTOR_MACHINE'] = response['Item']['support_vector_machine_hourly']
            predictions['K_NEIGHBORS_MACHINE'] = response['Item']['k_nearest_hourly']
            predictions['LINEAR_PERCEPTRON'] = response['Item']['linear_perceptron_hourly']
            predictions['EXTRA_TREES'] = response['Item']['extra_trees_hourly']
            predictions['HAS_CHANGED'] = response['Item']['hour_change']
            company_predictions[sector] = predictions
        return company_predictions

    def get_daily_predictions(self):
        company_predictions = {}
        for sector in self.sectors:
            predictions = {}
            response = self.table.get_item(Key={self.pk_key: sector})
            predictions['TOTAL'] = response['Item']['total_average_daily']
            predictions['NAIVE_BAYES'] = response['Item']['naive_bayes_daily']
            predictions['SUPPORT_VECTOR_MACHINE'] = response['Item']['support_vector_machine_daily']
            predictions['K_NEIGHBORS_MACHINE'] = response['Item']['k_nearest_daily']
            predictions['LINEAR_PERCEPTRON'] = response['Item']['linear_perceptron_daily']
            predictions['EXTRA_TREES'] = response['Item']['extra_trees_daily']
            predictions['HAS_CHANGED'] = response['Item']['day_change']
            company_predictions[sector] = predictions
        return company_predictions

    def get_weekly_predictions(self):
        company_predictions = {}
        for sector in self.sectors:
            predictions = {}
            response = self.table.get_item(Key={self.pk_key: sector})
            predictions['TOTAL'] = response['Item']['total_average_weekly']
            predictions['NAIVE_BAYES'] = response['Item']['naive_bayes_weekly']
            predictions['SUPPORT_VECTOR_MACHINE'] = response['Item']['support_vector_machine_weekly']
            predictions['K_NEIGHBORS_MACHINE'] = response['Item']['k_nearest_weekly']
            predictions['LINEAR_PERCEPTRON'] = response['Item']['linear_perceptron_weekly']
            predictions['EXTRA_TREES'] = response['Item']['extra_trees_weekly']
            predictions['HAS_CHANGED'] = response['Item']['week_change']
            company_predictions[sector] = predictions
        return company_predictions

    def get_monthly_predictions(self):
        company_predictions = {}
        for sector in self.sectors:
            predictions = {}
            response = self.table.get_item(Key={self.pk_key: sector})
            predictions['TOTAL'] = response['Item']['total_average_monthly']
            predictions['NAIVE_BAYES'] = response['Item']['naive_bayes_monthly']
            predictions['SUPPORT_VECTOR_MACHINE'] = response['Item']['support_vector_machine_monthly']
            predictions['LINEAR_PERCEPTRON'] = response['Item']['linear_perceptron_monthly']
            predictions['K_NEIGHBORS_MACHINE'] = response['Item']['k_nearest_monthly']
            predictions['EXTRA_TREES'] = response['Item']['extra_trees_monthly']
            predictions['HAS_CHANGED'] = response['Item']['month_change']
            company_predictions[sector] = predictions
        return company_predictions
