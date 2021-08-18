# Suricata Markdown

A simple script to convert a Suricata rules file into a Markdown table

## Installation

```
pip install -r requirements.txt
```

## Usage

```
python suricata_md.py <rules file> <variables file> <output file>
```

[View sample rules](suricata.rules)

[View sample vars](variables.yml)

[View sample output](rules.md)


### Assumptions

The variables file should be in YAML format and structured as follows:

```yaml
ip_sets:
    VARIABLE_NAME:
        - value1/16
        - value2/24
        - value3/24
port_sets:
    VARIABLE_NAME:
        - 1
        - 2
        - 3
```
