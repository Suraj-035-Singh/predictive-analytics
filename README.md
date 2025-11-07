# predictive-analytics
## 🚀 Overview
This project applies predictive analytics and machine learning to enable intelligent resource scaling in a DevOps environment.
By forecasting system metrics like CPU, memory, and disk usage, the system allows proactive scaling of infrastructure resources, improving performance and reducing unnecessary costs.ling of infrastructure.
This helps reduce operational costs, prevent system overloads, and maintain optimal performance under varying workloads.


##🧠 Motivation

Conventional auto-scaling mechanisms react after thresholds are breached, often causing latency spikes or resource bottlenecks.
This project introduces a predictive layer that anticipates resource demands and scales systems before performance degradation occurs — enabling a smarter and more cost-efficient DevOps environment.


## 🧰 Tools & Frameworks
Category	- Tools/Frameworks
Monitoring -	Prometheus
Machine Learning -	Python (pandas, scikit-learn, Prophet)
Backend - / API	Flask
Visualization	- Grafana
Containerization -	Docker

##🖥️ Setup & Usage
1️⃣ path to the repository
cd predictive-analytics-resource-scaling

2️⃣ Start Docker containers
docker-compose up -d

3️⃣ Run the Flask app
python app/app.py


Flask App: http://localhost:5000

