#AIM: To implement back propagation algorithm

import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])
inputLayer = inputs.shape[1]
hiddenLayer, output_neurons, lr = 4, 1, 0.1
error_history = []
weights_input_hidden = np.random.uniform(size=(inputLayer, hiddenLayer))
weights_hidden_output = np.random.uniform(size=(hiddenLayer, output_neurons))
for epoch in range(10000):
    input_layer = inputs
    hidden_layer = sigmoid(np.dot(input_layer, weights_input_hidden))
    predictions = sigmoid(np.dot(hidden_layer, weights_hidden_output))
    error_output = outputs - predictions
    adjustments_output = error_output * sigmoid_derivative(predictions)
    error_hidden = adjustments_output.dot(weights_hidden_output.T)
    adjustments_hidden = error_hidden * sigmoid_derivative(hidden_layer)
    weights_hidden_output += hidden_layer.T.dot(adjustments_output)*lr
    weights_input_hidden += input_layer.T.dot(adjustments_hidden)*lr
    if epoch % 1000 == 0:
        error_history.append(np.mean(np.abs(error_output)))
print("Predictions after training: \n", predictions)
plt.plot(range(0, 10000, 1000), error_history)
plt.title('Error Over Time')
plt.xlabel('Epochs')
plt.ylabel('Error')
plt.show()

'''
_____________________________________________________
output:
Predictions after training: 
 [[0.09827913]
 [0.92614249]
 [0.92015788]
 [0.06244861]]
                                [graph of error over time]
'''
