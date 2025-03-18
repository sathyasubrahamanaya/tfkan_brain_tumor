
### KAN Implementation Setup in VSCode

Follow these steps to configure your development environment:

1. **Open VSCode Terminal**  
   Navigate to your project directory in VSCode.

2. **Create a Virtual Environment**  
   Use Python 3.12 (or your preferred version) to create a new virtual environment:
   ```bash
   python3.12 -m venv env
   ```

3. **Activate the Virtual Environment**  
   For Windows, run:
   ```bash
   .\env\Scripts\activate
   ```

4. **Install Project Dependencies**  
   Install the required packages from `requirements.txt`:
   ```bash
   pip install -r .\requirements.txt
   ```

5. **Clone the tfkan Repository**  
   Clone the repository that contains the KAN implementation:
   ```bash
   git clone https://github.com/sathyasubrahamanaya/tfkan.git
   ```


6. **Install tfkan Package**  
   Change into the cloned repository directory and install the package:
   ```bash
   cd tfkan
   pip install .
   ```
7. **return to orginal project folder **
   ```bash
   cd ..
   ```
8. **Verify Installation**  
   Ensure that there are no errors and that the tfkan package is successfully installed. You can now start developing with the KAN implementation.

9. **Run the Streamlit Application**  
   Start the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```

---

This concise guide should help you quickly set up and run the KAN environment using VSCode, including launching the Streamlit application.
