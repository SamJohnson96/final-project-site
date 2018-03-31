from alpha_vantage_wrapper import AlphaVantageWrapper


class ChartBuilder:

    alpha_vantage = AlphaVantageWrapper()

    def create_apple_hour_array(self,predictions):
        prediction = predictions['HOUR']['apple']['TOTAL']
        print (prediction)
        apple_hour = self.alpha_vantage.get_intraday()
        apple_hour = apple_hour[len(apple_hour)-10:]
        apple_hour_data = []
        apple_hour_labels = []
        for index, row in apple_hour.iterrows():
            apple_hour_labels.append(str(row.name))
            apple_hour_data.append(float(row[3]))

        latest_price = apple_hour_data[len(apple_hour_data)-1]
        percentage_of_price = float(latest_price) / 100
        prediction_label = 'Next hour average prediction'

        if(prediction == 1):
            prediction_row = latest_price + percentage_of_price
        else:
            prediction_row = latest_price - percentage_of_price

        apple_hour_labels.append(prediction_label)
        apple_hour_data.append(prediction_row)

        return apple_hour_data,apple_hour_labels

    def create_apple_daily_array(self,predictions):
        prediction = predictions['DAY']['apple']['TOTAL']
        apple_day = self.alpha_vantage.get_days_information()
        apple_day = apple_day[len(apple_day)-10:]
        apple_daily_data = []
        apple_daily_labels = []
        for index, row in apple_day.iterrows():
            apple_daily_labels.append(str(row.name))
            apple_daily_data.append(float(row[3]))

        latest_price = apple_daily_data[len(apple_daily_data)-1]
        percentage_of_price = float(latest_price) / 100
        prediction_label = 'Next daily average prediction'

        if(prediction == 1):
            prediction_row = latest_price + percentage_of_price
        else:
            prediction_row = latest_price - percentage_of_price

        apple_daily_labels.append(prediction_label)
        apple_daily_data.append(prediction_row)


        return apple_daily_data,apple_daily_labels

    def create_apple_weekly_array(self,predictions):
        prediction = predictions['WEEK']['apple']['TOTAL']
        apple_week = self.alpha_vantage.get_weekly_information()
        apple_week = apple_week[len(apple_week)-10:]
        apple_weekly_data = []
        apple_weekly_labels = []
        for index, row in apple_week.iterrows():
            apple_weekly_labels.append(str(row.name))
            apple_weekly_data.append(float(row[3]))

        latest_price = apple_weekly_data[len(apple_weekly_data)-1]
        percentage_of_price = float(latest_price) / 100
        prediction_label = 'Next weekly average prediction'

        if(prediction == 1):
            prediction_row = latest_price + percentage_of_price
        else:
            prediction_row = latest_price - percentage_of_price

        apple_weekly_labels.append(prediction_label)
        apple_weekly_data.append(prediction_row)

        return apple_weekly_data,apple_weekly_labels

    def create_apple_monthly_array(self,predictions):
        prediction = predictions['MONTH']['apple']['TOTAL']
        apple_month = self.alpha_vantage.get_monthly_information()
        apple_month = apple_month[len(apple_month)-10:]
        apple_monthly_data = []
        apple_monthly_labels = []
        for index, row in apple_month.iterrows():
            apple_monthly_labels.append(str(row.name))
            apple_monthly_data.append(float(row[3]))
            
        latest_price = apple_monthly_data[len(apple_monthly_data)-1]
        percentage_of_price = float(latest_price) / 100
        prediction_label = 'Next monthly average prediction'

        if(prediction == 1):
            prediction_row = latest_price + percentage_of_price
        else:
            prediction_row = latest_price - percentage_of_price
        apple_monthly_labels.append(prediction_label)
        apple_monthly_data.append(prediction_row)

        return apple_monthly_data,apple_monthly_labels
