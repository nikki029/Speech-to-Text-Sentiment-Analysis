### STEP 01- Create the new environment
```bash
conda create --prefix ./Venv python=3.9 -y
```

### STEP 02- Activate the environment
```bash
conda activate ./Venv
```
OR
```bash
source activate ./Venv
```

### STEP 03- Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 04- Run the main file
```bash
python test.py
```