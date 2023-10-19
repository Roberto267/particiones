import csv
import random
import matplotlib.pyplot as plt

# Cargar el dataset desde el archivo CSV
def load_dataset(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# Partición aleatoria simple
def random_split(data, train_size):
    random.shuffle(data)
    split_index = int(train_size * len(data))
    train_set = data[:split_index]
    test_set = data[split_index:]
    return train_set, test_set

# Partición por cantidad fija
def fixed_size_split(data, train_size):
    split_index = int(train_size * len(data))
    train_set = data[:split_index]
    test_set = data[split_index:]
    return train_set, test_set

# Partición por proporción de una característica
def feature_ratio_split(data, feature_index, ratio):
    if feature_index < 0 or feature_index >= len(data[0]):
        print("Invalid.")
        return
    
    split_value = ratio * (max(float(row[feature_index]) for row in data) - min(float(row[feature_index]) for row in data))
    train_set = [row for row in data if float(row[feature_index]) <= split_value]
    test_set = [row for row in data if float(row[feature_index]) > split_value]
    
    return train_set, test_set

# Partición estratificada
def stratified_split(data, train_size):
    class_groups = {}
    for row in data:
        class_label = row[-1]
        if class_label not in class_groups:
            class_groups[class_label] = []
        class_groups[class_label].append(row)

    train_set, test_set = [], []

    for class_label, class_data in class_groups.items():
        random.shuffle(class_data)
        split_index = int(train_size * len(class_data))
        train_set.extend(class_data[:split_index])
        test_set.extend(class_data[split_index:])

    return train_set, test_set

# Partición por clase
def class_split(data, train_size):
    class_groups = {}
    for row in data:
        class_label = row[-1]
        if class_label not in class_groups:
            class_groups[class_label] = []
        class_groups[class_label].append(row)

    train_set, test_set = [], []

    for class_data in class_groups.values():
        random.shuffle(class_data)
        split_index = int(train_size * len(class_data))
        train_set.extend(class_data[:split_index])
        test_set.extend(class_data[split_index:])

    return train_set, test_set

# Partición personalizada
def custom_split(data, train_indices):
    train_set = [data[i] for i in train_indices]
    test_set = [data[i] for i in range(len(data)) if i not in train_indices]
    return train_set, test_set

# Cargar el dataset
dataset = load_dataset('irisbin.csv')

# Ejemplo de uso de los métodos
train_set1, test_set1 = random_split(dataset, 0.6)
train_set2, test_set2 = fixed_size_split(dataset, 0.5)
train_set3, test_set3 = class_split(dataset, 0.6)
train_set4, test_set4 = stratified_split(dataset, 0.6)
train_set5, test_set5 = feature_ratio_split(dataset, 0, 0.8)

# Visualización de los datos seleccionados
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.scatter([float(row[0]) for row in train_set1], [float(row[1]) for row in train_set1], label='Train Set')
plt.scatter([float(row[0]) for row in test_set1], [float(row[1]) for row in test_set1], label='Test Set')
plt.title('Random Split')
plt.legend()

plt.subplot(2, 3, 2)
plt.scatter([float(row[0]) for row in train_set2], [float(row[1]) for row in train_set2], label='Train Set')
plt.scatter([float(row[0]) for row in test_set2], [float(row[1]) for row in test_set2], label='Test Set')
plt.title('Fixed Size Split')
plt.legend()

plt.subplot(2, 3, 3)
plt.scatter([float(row[0]) for row in train_set3], [float(row[1]) for row in train_set3], label='Train Set')
plt.scatter([float(row[0]) for row in test_set3], [float(row[1]) for row in test_set3], label='Test Set')
plt.title('Class Split')
plt.legend()

plt.subplot(2, 3, 4)
plt.scatter([float(row[0]) for row in train_set4], [float(row[1]) for row in train_set4], label='Train Set')
plt.scatter([float(row[0]) for row in test_set4], [float(row[1]) for row in test_set4], label='Test Set')
plt.title('Stratified Split')
plt.legend()

plt.subplot(2, 3, 5)
plt.scatter([float(row[0]) for row in train_set5], [float(row[1]) for row in train_set5], label='Train Set')
plt.scatter([float(row[0]) for row in test_set5], [float(row[1]) for row in test_set5], label='Test Set')
plt.title('Feature Ratio Split')
plt.legend()

plt.show()
