✅ Automated Quality Inspection Dashboard
<br>
A lightweight and intelligent dashboard to assist in quality inspection workflows by analyzing production batches, tracking defect types, and visualizing real-time insights. Designed for flexible QA across domains, this project supports CSV/Excel imports and can evolve into a fully sensor-integrated or image-based system.

🌟 Key Features
Batch Monitoring: Track multiple production batches and visualize defect metrics.

Defect Analysis: Input and classify defects based on type, frequency, and severity.

Control Charts: View SQC plots to monitor stability, variation, and process control.

Custom Filters: Drill down by date range, batch ID, or machine.

Report Export: Export filtered data to PDF or CSV formats.

🚀 Getting Started
git clone https://github.com/yourusername/quality-inspection-dashboard.git
cd quality-inspection-dashboard
pip install -r requirements.txt
streamlit run app.py

🛠️ Tech Stack

Languages: Python

Visualization: Streamlit, matplotlib, seaborn

Data: CSV/Excel import support, report exports

Modular Code: Clean architecture for easy feature addition

📁 Folder Structure

quality-inspection-dashboard/
├── app.py
├── data/
├── modules/
│   ├── data_cleaning.py
│   ├── defect_analysis.py
│   └── report_generator.py
├── reports/
├── requirements.txt
└── README.md

🔮 Future Enhancements

Hardware Integration: Use image processing or sensor input for automated defect detection.

Predictive Quality Checks: Machine learning to predict defect likelihood from batch data.

Real-Time Alerts: Push notifications for QA rule breaches.

Cloud Reporting: Store and access reports via cloud QA portals.

📄 License
MIT License © 2025 Contributors
