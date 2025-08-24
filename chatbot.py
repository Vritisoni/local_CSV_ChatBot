
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Local CSV Chatbot (No API Key)")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # Step 2: User Question
    user_question = st.text_input("Ask about your data (e.g. 'average of column X', 'plot column A vs column B'): ")

    if st.button("Ask") and user_question:
        st.write("### 🤖 Chatbot Answer:")
        
        try:
            # Handle average queries
            if "average" in user_question.lower():
                col = [c for c in df.columns if c.lower() in user_question.lower()]
                if col:
                    # avg = df[col[0]].mean()
                    # st.write(f"The average of **{col[0]}** is: {avg:.2f}")
                    df[col[0]] = pd.to_numeric(df[col[0]], errors='coerce')
                    avg = df[col[0]].mean()
                    st.write(f"The average of **{col[0]}** is: {avg:.2f} (ignoring non-numeric values)")

                else:
                    st.write("Couldn't find the column. Please check spelling.")

            # Handle sum queries
            elif "sum" in user_question.lower():
                col = [c for c in df.columns if c.lower() in user_question.lower()]
                if col:
                    total = df[col[0]].sum()
                    st.write(f"The sum of **{col[0]}** is: {total:.2f}")
                else:
                    st.write("Couldn't find the column. Please check spelling.")

            # Handle plotting queries
            elif "plot" in user_question.lower():
                cols = [c for c in df.columns if c.lower() in user_question.lower()]
                
                if len(cols) >= 2:
                    chart_type = "line"
                    if "bar" in user_question.lower():
                        chart_type = "bar"
                    elif "scatter" in user_question.lower():
                        chart_type = "scatter"
                    elif "hist" in user_question.lower():
                        chart_type = "hist"

                    fig, ax = plt.subplots()

                    if chart_type == "line":
                        ax.plot(df[cols[0]], df[cols[1]], marker="o")
                    elif chart_type == "bar":
                        ax.bar(df[cols[0]].astype(str), df[cols[1]])
                    elif chart_type == "scatter":
                        ax.scatter(df[cols[0]], df[cols[1]])
                    elif chart_type == "hist":
                        ax.hist(df[cols[0]], bins=10)


                    plt.xlabel(cols[0])
                    plt.ylabel(cols[1] if len(cols) > 1 else "")
                    plt.title(f"{cols[1]} vs {cols[0]}" if len(cols) > 1 else f"Histogram of {cols[0]}")
                    st.pyplot(fig)
                else:
                    st.write("Please mention at least two columns to plot (or one for histogram).")

            else:
                st.write("I can handle: average, sum, and plot (line, bar, scatter, hist).")

        except Exception as e:
            st.write(f"⚠️ Error: {e}")
