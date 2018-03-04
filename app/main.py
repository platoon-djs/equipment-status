from flask import Flask, request, render_template
import sys, csv, datetime

# Global variables
app = Flask(__name__)
app.config['CSV_FILE'] = '/var/www/stored/reports.csv'
reports = [] # This guy holds the current reports during runtime. They're still saved to file though.
status_options = ["Minor Malfunction", "Major Malfunction", "Unusable"]

# Index page
@app.route('/')
def my_index():
	return render_template('index.html', reports=reports)

# Add and edit reports
@app.route('/manage')
def my_form():
	return render_template('manage.html', reports=reports, status_options=status_options)

# When something is added or updated in /manage, they end up here.
# The use of eval() is kind of bad practice, but this is such a small site so I think it's fine.
@app.route('/manage', methods=['POST'])
def manage():
	# Add a new report
	if request.form['btn'] == 'add':
		time = datetime.date.today().strftime("%d-%m-%Y")
		report = [str(getNextID()), request.form['unit'], request.form['status'], request.form['desc'], time]
		reports.append(report)
		saveToCsvFile()
		return render_template('manage.html', report=report, reports=reports, status_options=status_options, message="Added")

	# If a report is to be edited, show an edit page
	elif request.form['btn'] == 'edit':
		report = eval(request.form['report']) # Convert the report to a list
		return render_template('edit.html', report=report, status_options=status_options)

	# Remove a report
	elif request.form['btn'] == 'remove':
		report = eval(request.form['report']) # Convert the report to a list
		reports.remove(report)
		saveToCsvFile()
		return render_template('manage.html', report=report, reports=reports, status_options=status_options, message="Removed")

	# An edited report is updated
	elif request.form['btn'] == 'update':
		ID = request.form['id']
		for report in reports:
			if ID == report[0]:
				report[1] = request.form['unit']
				report[2] = request.form['status']
				report[3] = request.form['desc']
				return render_template('manage.html', report=report, reports=reports, status_options=status_options, message="Updated")
			

# This could be improved I guess, hash-solution to get unique IDs
def getNextID():
	if reports:
		return int(reports[-1][0]) + 1
	else:
		return 0

# Save the reports list to a CSV file
def saveToCsvFile():
	myFile = open(app.config['CSV_FILE'], 'w')
	with myFile:
	    writer = csv.writer(myFile)
	    for report in reports:
	    	writer.writerow(report)

# Reads the reports list from a CSV file
def readCsvFile():
	results = []
	try:
		file = open(app.config['CSV_FILE'], 'r')
		reader = csv.reader(file)
		for row in reader:
			results.append (row)
	except FileNotFoundError:
		file = open(app.config['CSV_FILE'], 'w')
	return results
	

# Server start
if __name__ == "__main__":
	reports = readCsvFile()
	app.run(debug=True, host='0.0.0.0')
