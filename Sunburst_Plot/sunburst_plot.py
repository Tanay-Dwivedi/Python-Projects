import plotly.express as px

data = px.data.tips()
figure = px.sunburst(data, path=["day", "sex"], values="total_bill")
figure.show()
