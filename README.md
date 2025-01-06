# 🤖 Robot Bobby YouTube Dashboard

This is a **Streamlit** application that provides a dashboard for visualizing YouTube channel analytics. It processes and displays data from a CSV file containing information about video performance, such as views, subscribers, likes, and watch time.

[On Streamlit Cloud](https://youtube-dashboard-rb.streamlit.app/)

## Features
- **Key Metrics Display**: Shows total views, subscribers, and the number of videos in the dataset.
- **Data Preview**: Displays the first few rows of the processed data for quick inspection.
- **Bar Chart Visualization**: Visualizes metrics like likes, comments, and watch time for videos with significant engagement.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bobbyroe/yt-dash
   cd yt-dash
   ```

2. Install the required Python libraries (on MacOS):
   ```bash
   pip3 install streamlit pandas
   ```

3. Ensure you have a CSV file named `yt-data.csv` in the root directory with the following columns:
   - `Content`
   - `Views`
   - `Subscribers`
   - `Watch time (hours)`
   - `Duration`
   - Additional columns relevant to your YouTube analytics.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open the app in your web browser. By default, it will be available at:
   ```
   http://localhost:8501
   ```

## Data Preparation

The application processes the input data as follows:
1. Filters out rows with "Total" in the `Content` column and drops unnecessary columns.
2. Rounds watch time values to the nearest hour and converts video durations from seconds to minutes.
3. Filters videos based on a watch time threshold (default: 50 hours) for focused analysis.

## Customization

- To change the watch time threshold for filtering videos, modify the `threshold` variable in the script:
   ```python
   threshold = <new_value>
   ```

- Add or remove columns from the bar chart visualization by editing the `columns` list:
   ```python
   columns = ['Video title', 'Comments added', 'Shares', 'Likes']
   ```

## Example Dashboard

- **Key Metrics**: Total Views, Subscribers, and the number of videos.
- **Data Table**: A preview of the processed YouTube analytics data.
- **Bar Chart**: Horizontal bar chart for engagement metrics.

## Dependencies
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to contribute or suggest improvements!