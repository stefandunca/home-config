# Setup info

## Dev env

```python
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Generate config

```bash
python /home/$USER/.human/ansible/inventory_setup/main.py --config /home/$USER/.human/ansible/inventory_setup/configuration/configuration.qml --output_dir /home/$USER/.human/ansible/group_vars/
```
