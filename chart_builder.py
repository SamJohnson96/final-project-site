from alpha_vantage_wrapper import AlphaVantageWrapper


class ChartBuilder:

    alpha_vantage = AlphaVantageWrapper()

    def create_apple_hour_array(self,predictions):
        prediction = predictions['HOUR']['apple']['TOTAL']
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


    def create_facebook_hour_array(self,predictions):
        prediction = predictions['HOUR']['facebook']['TOTAL']
        facebook_hour = self.alpha_vantage.get_intraday('FB')
        facebook_hour = facebook_hour[len(facebook_hour)-10:]
        facebook_hour_data = []
        facebook_hour_labels = []
        for index, row in facebook_hour.iterrows():
            facebook_hour_labels.append(str(row.name))
            facebook_hour_data.append(float(row[3]))

        latest_price = facebook_hour_data[len(facebook_hour_data)-1]
        percentage_of_price = float(latest_price) / 100
        prediction_label = 'Next hour average prediction'

        if(prediction == 1):
            prediction_row = latest_price + percentage_of_price
        else:
            prediction_row = latest_price - percentage_of_price

        facebook_hour_labels.append(prediction_label)
        facebook_hour_data.append(prediction_row)

        return facebook_hour_data,facebook_hour_labels

    def create_facebook_daily_array(self,predictions):
        prediction = predictions['DAY']['facebook']['TOTAL']
        facebook_day = self.alpha_vantage.get_days_information('FB')
        facebook_day = facebook_day[len(facebook_day)-10:]
        facebook_daily_data = []
        facebook_daily_labels = []
        for index, row in facebook_day.iterrows():
            print(row[3])
            facebook_daily_labels.append(str(row.name))
            facebook_daily_data.append(float(row[3]))

        latest_price = facebook_daily_data[len(facebook_daily_data)-1]
        percentage_of_price = float(latest_price) / 100
        prediction_label = 'Next daily average prediction'

        if(prediction == 1):
            prediction_row = latest_price + percentage_of_price
        else:
            prediction_row = latest_price - percentage_of_price

        facebook_daily_labels.append(prediction_label)
        facebook_daily_data.append(prediction_row)

        return facebook_daily_data,facebook_daily_labels

    def create_facebook_weekly_array(self,predictions):
        prediction = predictions['WEEK']['facebook']['TOTAL']
        facebook_week = self.alpha_vantage.get_weekly_information('FB')
        facebook_week = facebook_week[len(facebook_week)-10:]
        facebook_weekly_data = []
        facebook_weekly_labels = []
        for index, row in facebook_week.iterrows():
            facebook_weekly_labels.append(str(row.name))
            facebook_weekly_data.append(float(row[3]))

        latest_price = facebook_weekly_data[len(facebook_weekly_data)-1]
        percentage_of_price = float(latest_price) / 100
        prediction_label = 'Next weekly average prediction'

        if(prediction == 1):
            prediction_row = latest_price + percentage_of_price
        else:
            prediction_row = latest_price - percentage_of_price

        facebook_weekly_labels.append(prediction_label)
        facebook_weekly_data.append(prediction_row)

        return facebook_weekly_data,facebook_weekly_labels

    def create_facebook_monthly_array(self,predictions):
        prediction = predictions['MONTH']['facebook']['TOTAL']
        facebook_month = self.alpha_vantage.get_monthly_information('FB')
        facebook_month = facebook_month[len(facebook_month)-10:]
        facebook_monthly_data = []
        facebook_monthly_labels = []
        for index, row in facebook_month.iterrows():
            facebook_monthly_labels.append(str(row.name))
            facebook_monthly_data.append(float(row[3]))

        latest_price = facebook_monthly_data[len(facebook_monthly_data)-1]
        percentage_of_price = float(latest_price) / 100
        prediction_label = 'Next monthly average prediction'

        if(prediction == 1):
            prediction_row = latest_price + percentage_of_price
        else:
            prediction_row = latest_price - percentage_of_price
        facebook_monthly_labels.append(prediction_label)
        facebook_monthly_data.append(prediction_row)

        return facebook_monthly_data,facebook_monthly_labels
