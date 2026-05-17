Install Dependencies:

pip install streamlit pytest playwright coverage flake8
python -m playwright install


Run the Streamlit App:

python -m streamlit run streamlit_app.py


Then open:

http://localhost:8501


Run Unit and Functional Tests:

python -m unittest discover -s tests -v


Run Coverage Report:

python -m coverage run --source=app -m unittest discover -s tests
python -m coverage report -m


Optional HTML report:

python -m coverage html


Run Playwright UI Tests:

First, start the Streamlit app in one terminal:

python -m streamlit run streamlit_app.py

Then open a second terminal and run:

python -m pytest tests/test_streamlit_playwright.py -v


Run Performance Test:
python -m tests.test_performance