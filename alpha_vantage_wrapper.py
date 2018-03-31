import pandas as pd
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.timeseries import TimeSeries

class AlphaVantageWrapper:

    ts = TimeSeries(key='QL2Z176B6Q3JYM6A', output_format='pandas')
    sp = SectorPerformances(key='QL2Z176B6Q3JYM6A', output_format='pandas')

    def get_intraday(self,company="AAPL",timegap="60min"):
        """Calls AlphaVantages API and gets the intraday figures for the given company.
        Args:
            company (string): Company name that we will look for
            timegap (string): The time interval we look at during the day
        Returns:
            Panda Dataframe: Dataframe of stock information for the given request

        """
        data, meta_data = self.ts.get_intraday(symbol=company,interval=timegap)
        return data

    def get_days_information(self,company="AAPL"):
        """Calls AlphaVantages API and gets the days figures for the given company.
        Args:
            company (string): Company name that we will look for
        Returns:
            Panda Dataframe: Dataframe of stock information for the given request

        """
        data, meta_data = self.ts.get_daily(symbol=str(company))
        return data

    def get_weekly_information(self,company="AAPL"):
        """Calls AlphaVantages API and gets the weeks figures for the given company.
        Args:
            company (string): Company name that we will look for
        Returns:
            Panda Dataframe: Dataframe of stock information for the given request
        """
        data, meta_data = self.ts.get_weekly(symbol=str(company))
        return data

    def get_monthly_information(self,company="AAPL"):
        """Calls AlphaVantages API and gets the months figures for the given company.
        Args:
            company (string): Company name that we will look for
        Returns:
            Panda Dataframe: Dataframe of stock information for the given request

        """
        data, meta_data = self.ts.get_monthly(symbol=str(company))
        return data

    def get_sector_intraday(self):
        sp = SectorPerformances(key='QL2Z176B6Q3JYM6A', output_format='pandas')
        data, meta_data = self.sp.get_sector()
        realtime = data['Rank A: Real-Time Performance']
        return realtime.get('Information Technology')

    def get_sector_daily(self):
        data, meta_data = self.sp.get_sector()
        day = data['Rank B: Day Performance']
        return day.get('Information Technology')

    def get_sector_weekly(self):
        data, meta_data = self.sp.get_sector()
        week = data['Rank C: Day Performance']
        return week.get('Information Technology')

    def get_sector_monthly(self):
        data, meta_data = self.sp.get_sector()
        month = data['Rank D: Month Performance']
        return month.get('Information Technology')
