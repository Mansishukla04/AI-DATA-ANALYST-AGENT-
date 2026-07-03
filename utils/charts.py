import streamlit as st
import matplotlib.pyplot as plt

def plot_chart(df):

    chart_type = st.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Line Chart", "Pie Chart", "Histogram", "Box Plot"]
    )

    categorical_columns = df.select_dtypes(include="object").columns
    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) == 0:
        st.warning("No numeric columns found.")
        return

    fig, ax = plt.subplots(figsize=(8,5))

    if chart_type == "Bar Chart":

        x_column = st.selectbox("Select X-Axis", categorical_columns)
        y_column = st.selectbox("Select Y-Axis", numeric_columns)

        chart_data = df.groupby(x_column)[y_column].sum()

        chart_data.plot(kind="bar", ax=ax)

        ax.set_title(f"{y_column} by {x_column}")
        plt.savefig("chart.png")

        st.pyplot(fig)

    elif chart_type == "Line Chart":

        x_column = st.selectbox("Select X-Axis", categorical_columns)
        y_column = st.selectbox("Select Y-Axis", numeric_columns)

        chart_data = df.groupby(x_column)[y_column].sum()

        chart_data.plot(kind="line", marker="o", ax=ax)

        ax.set_title(f"{y_column} by {x_column}")
        plt.savefig("chart.png")

        st.pyplot(fig)
     
    elif chart_type == "Pie Chart":

        x_column = st.selectbox("Category", categorical_columns)
        y_column = st.selectbox("Values", numeric_columns)

        chart_data = df.groupby(x_column)[y_column].sum()

        chart_data.plot(
            kind="pie",
            autopct="%1.1f%%",
            ax=ax
        )

        ax.set_ylabel("")
        plt.savefig("chart.png")

        st.pyplot(fig)

    elif chart_type == "Histogram":

        column = st.selectbox("Select Column", numeric_columns)

        ax.hist(df[column], bins=10)

        ax.set_title(f"Histogram of {column}")
        plt.savefig("chart.png")

        st.pyplot(fig)

    elif chart_type == "Box Plot":

        column = st.selectbox("Select Column", numeric_columns)

        ax.boxplot(df[column])

        ax.set_title(f"Box Plot of {column}")
        plt.savefig("chart.png")

        st.pyplot(fig)