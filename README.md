# ⚖️ BMI Calculator & Health Classifier

A Python implementation of an Body Mass Index (BMI) calculator. This project uses **Object-Oriented Programming (OOP)** to manage personal physical data and provide medical interpretations based on international standards.

## Overview
The `Personne` class stores individual physical attributes and includes methods to compute health indicators. It automates the classification of weight categories, making it a foundation for health-tracking applications.

## Key Features
- **Data Encapsulation**: Stores height, weight, and age within a single object instance.
- **Automated Calculation**: A dedicated `IMC` method that applies the standard formula ($weight / height^2$).
- **Health Interpretation**: A logic engine that categorizes the result into standard brackets:
  - **Underweight** (Insuffisance pondérale)
  - **Normal** (IMC normal)
  - **Obesity** (Obésité)

## Technical Concepts
- **OOP Structure**: Clear use of `self` to access instance attributes.
- **Mathematical Modeling**: Implementation of power operations and division for biometric indexing.
- **Conditional Branching**: Use of `if/elif` structures for precise data classification.

## Usage Example
```python
# Create a person (Height: 1.75m, Weight: 70kg, Age: 25)
p = Personne(1.75, 70, 25)
value = p.IMC()
print(f"BMI: {value:.2 format}")
print(f"Status: {p.interpretation(value)}")
