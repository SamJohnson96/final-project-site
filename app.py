from flask import Flask
from flask import Flask, render_template
from database_wrapper import DatabaseWrapper
from file_manager import FileManager
from chart_builder import ChartBuilder
from table_builder import PredictionBuilder

app = Flask(__name__)

# Create wrappers
database_wrapper = DatabaseWrapper()
file_manager = FileManager()
chart_builder = ChartBuilder()


# Get the predictions
all_predictions = database_wrapper.get_all_predictions()
# Get the results
all_results = database_wrapper.get_all_results()

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/naive-bayes-classifier")
def naive_bayes():
	naive_content = file_manager.get_text_file('content/naive_bayes.txt')
	return render_template('classification.html',classifier='Naive Bayes Classifier',content=naive_content)

@app.route("/topic-classification")
def topic_classification():
	topic_content = file_manager.get_text_file('content/topic_classification.txt')
	return render_template('classification.html',classifier='Topic Classifier',content=topic_content)

@app.route("/linear-perceptron")
def linear_perceptron():
	linear_perceptron_content = file_manager.get_text_file('content/linear_perceptron.txt')
	return render_template('classification.html',classifier='Linear Perceptron',content=linear_perceptron_content)

@app.route("/support-vector-machine")
def support_vector_machine():
	support_vector_machine_content = file_manager.get_text_file('content/support_vector_machine.txt')
	return render_template('classification.html',classifier='Support Vector Machine',content=support_vector_machine_content)

@app.route("/extra-trees-classifier")
def extra_trees_classifier():
	extra_tree_content = file_manager.get_text_file('content/extra_trees_classifier.txt')
	return render_template('classification.html',classifier='Extra Trees Classifier',content=extra_tree_content)

@app.route("/k-nearest-neighbors")
def k_nearest_neighbors():
	k_neighbors = file_manager.get_text_file('content/k_neighbors.txt')
	return render_template('classification.html',classifier='K Neighbors Classifier',content=k_neighbors)

@app.route("/current-apple-predictions")
def current_predictions():
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

# @app.route("/current-facebook-predictions")
# def current_predictions():
# 	prediction_table_builder = PredictionBuilder()
# 	apple_hour_data, apple_hour_labels = chart_builder.create_apple_hour_array(all_predictions)
# 	apple_daily_data, apple_daily_labels = chart_builder.create_apple_daily_array(all_predictions)
# 	apple_weekly_data, apple_weekly_labels = chart_builder.create_apple_weekly_array(all_predictions)
# 	tables = prediction_table_builder.create_all_tables(all_predictions)
# 	return render_template('predictions.html', classifier='Current Predictions',
# 											   prediction_table=tables['FACEBOOK'],
# 											   company_hour_data=apple_hour_data,
# 											   company_hour_labels=apple_hour_labels,
# 											   company_daily_data = apple_daily_data,
# 											   company_daily_labels = apple_daily_labels,
# 											   company_weekly_data = apple_weekly_data,
# 											   company_weekly_labels = apple_weekly_labels
# 											   )



if __name__ == "__main__":
	app.run()
