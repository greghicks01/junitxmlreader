#Running the tests

Using this command line (with any other updates for CICD)

```python
pytest --ignore-glob=test_sample_set.py --junit-xml=output-unit.xml
```

##Sample Test
The sample test is there to ensure we can create a sample output of all desired marked and unmarked tests.

Run this command to generate a new sample set:
```python
pytest test_sample_set.py --junit-xml=sample.xml
```