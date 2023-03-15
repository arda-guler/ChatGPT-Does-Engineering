import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights1 = np.random.rand(input_size, hidden_size)
        self.weights2 = np.random.rand(hidden_size, output_size)
    
    def forward(self, x):
        self.hidden_layer = np.dot(x, self.weights1)
        self.hidden_layer_activated = self.sigmoid(self.hidden_layer)
        self.output_layer = np.dot(self.hidden_layer_activated, self.weights2)
        self.output_layer_activated = self.sigmoid(self.output_layer)
        return self.output_layer_activated
    
    def backward(self, x, y, learning_rate):
        error = y - self.output_layer_activated
        output_error = error * self.sigmoid_derivative(self.output_layer)
        hidden_error = np.dot(output_error, self.weights2.T) * self.sigmoid_derivative(self.hidden_layer)
        self.weights2 += learning_rate * np.dot(self.hidden_layer_activated.T, output_error)
        self.weights1 += learning_rate * np.dot(x.T, hidden_error)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
