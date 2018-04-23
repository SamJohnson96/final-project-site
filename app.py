from flask import Flask
from flask import Flask, render_template
from website_database_wrapper import WebsiteDatabaseWrapper
from file_manager import FileManager
from chart_builder import ChartBuilder
from table_builder import PredictionBuilder

app = Flask(__name__)

# Create wrappers
website_database_wrapper = WebsiteDatabaseWrapper()
file_manager = FileManager()
chart_builder = ChartBuilder()


# GET PREDICTIONS FROM DYNAMODB
all_predictions = website_database_wrapper.get_all_predictions()

# GET RESULTS
all_results = website_database_wrapper.get_all_results()

@app.route("/")
def main():
	home_content = file_manager.get_text_file('content/home.txt')
	return render_template('index.html',content=home_content)

@app.route("/naive-bayes-classifier")
def naive_bayes():
	naive_content = file_manager.get_text_file('content/naive_bayes.txt')
	return render_template('classification.html',classifier='Naive Bayes Classifier',content=naive_content,url="http://ec2-35-177-151-51.eu-west-2.compute.amazonaws.com/classify-naive")

@app.route("/topic-classification")
def topic_classification():
	topic_content = file_manager.get_text_file('content/topic_classification.txt')
	return render_template('classification.html',classifier='Topic Classifier',content=topic_content,url="http://ec2-35-177-151-51.eu-west-2.compute.amazonaws.com/classify-topic")

@app.route("/linear-perceptron")
def linear_perceptron():
	linear_perceptron_content = file_manager.get_text_file('content/linear_perceptron.txt')
	return render_template('classification.html',classifier='Linear Perceptron',content=linear_perceptron_content,url="http://ec2-35-177-151-51.eu-west-2.compute.amazonaws.com/classify-linear")

@app.route("/support-vector-machine")
def support_vector_machine():
	support_vector_machine_content = file_manager.get_text_file('content/support_vector_machine.txt')
	return render_template('classification.html',classifier='Support Vector Machine',content=support_vector_machine_content,url="http://ec2-35-177-151-51.eu-west-2.compute.amazonaws.com/classify-svm")

@app.route("/extra-trees-classifier")
def extra_trees_classifier():
	extra_tree_content = file_manager.get_text_file('content/extra_trees_classifier.txt')
	return render_template('classification.html',classifier='Extra Trees Classifier',content=extra_tree_content,url="http://ec2-35-177-151-51.eu-west-2.compute.amazonaws.com/classify-extra-trees")

@app.route("/k-nearest-neighbors")
def k_nearest_neighbors():
	k_neighbors = file_manager.get_text_file('content/k_neighbors.txt')
	return render_template('classification.html',classifier='K Neighbors Classifier',content=k_neighbors,url="http://ec2-35-177-151-51.eu-west-2.compute.amazonaws.com/classify-knearest")

@app.route("/predictions/apple")
def current_apple_predictions():
	prediction_table_builder = PredictionBuilder()
	apple_hour_data, apple_hour_labels = chart_builder.create_apple_hour_array(all_predictions)
	apple_daily_data, apple_daily_labels = chart_builder.create_apple_daily_array(all_predictions)
	apple_weekly_data, apple_weekly_labels = chart_builder.create_apple_weekly_array(all_predictions)
	apple_monthly_data, apple_monthly_labels = chart_builder.create_apple_monthly_array(all_predictions)
	tables = prediction_table_builder.create_all_tables(all_predictions)
	return render_template('predictions.html', company='Apple',
											   prediction_table=tables['APPLE'],
											   company_hour_data=apple_hour_data,
											   company_hour_labels=apple_hour_labels,
											   company_daily_data = apple_daily_data,
											   company_daily_labels = apple_daily_labels,
											   company_weekly_data = apple_weekly_data,
											   company_weekly_labels = apple_weekly_labels,
											   company_monthly_data = apple_monthly_data,
											   company_monthly_labels = apple_monthly_labels
											   )

@app.route("/predictions/facebook")
def current_facebook_predictions():
	prediction_table_builder = PredictionBuilder()
	facebook_hour_data, facebook_hour_labels = chart_builder.create_facebook_hour_array(all_predictions)
	facebook_daily_data, facebook_daily_labels = chart_builder.create_facebook_daily_array(all_predictions)
	facebook_weekly_data, facebook_weekly_labels = chart_builder.create_facebook_weekly_array(all_predictions)
	facebook_monthly_data, facebook_monthly_labels = chart_builder.create_facebook_monthly_array(all_predictions)
	tables = prediction_table_builder.create_all_tables(all_predictions)
	return render_template('predictions.html', company='Facebook',
											   prediction_table=tables['FACEBOOK'],
											   company_hour_data=facebook_hour_data,
											   company_hour_labels=facebook_hour_labels,
											   company_daily_data = facebook_daily_data,
											   company_daily_labels = facebook_daily_labels,
											   company_weekly_data = facebook_weekly_data,
											   company_weekly_labels = facebook_weekly_labels,
											   company_monthly_data = facebook_monthly_data,
											   company_monthly_labels = facebook_monthly_labels
											   )

if __name__ == "__main__":
	app.run()
