import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Read the CSV file
mental_data = pd.read_csv("survey_mental_health.csv")

# Replace null values with "No Answer"
mental_data = mental_data.fillna("No Answer")

# Select the columns of interest
df = mental_data.loc[:, ["Gender_clean", "Country", "self_employed", "family_history", "Received_treatment", "work_interfere", "remote_work", "tech_company", "benefits_provided", "wellness_program", "seek_help", "anonymity", "coworkers_are_aware", "supervisor_is_aware", "mental_health_interview", "phys_health_interview"]]

# Remove rows with missing values
df1 = df.dropna()

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Mental Health Survey"),
    dcc.Graph(
        id="survey-graph",
        figure={
            "data": [
                {
                    "x": df["Country"].value_counts().index,
                    "y": df["Country"].value_counts().values,
                    "type": "bar"
                }
            ],
            "layout": {
                "title": "Country distribution",
                "xaxis": {"title": "Country"},
                "yaxis": {"title": "Count"}
            }
        }
    )
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
