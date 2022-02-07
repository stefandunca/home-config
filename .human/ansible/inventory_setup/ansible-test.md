# Setup info

## Dev env

```python
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Run tests

```python
python .human/ansible/inventory_setup/main.py --config .human/ansible/inventory_setup/test/test_configuration.qml --output_dir .human/ansible/inventory_setup/test/
```
