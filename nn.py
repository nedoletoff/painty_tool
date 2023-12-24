import numpy as np

from img_to_binarr import img_to_bin


def load_inputs_and_labels():
    inputs = []
    labels = []
    with open('annotations.csv', 'r') as f:
        f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            line = line.split(',')
            inputs.append(line[0])
            labels.append(line[1].replace('\n', ''))
    for i in range(len(inputs)):
        inputs[i] = img_to_bin(inputs[i])[2]
        labels[i] = int(labels[i])

    inputs_list = []
    for image in inputs:
        image = np.array(image)
        inputs_list.append(image.reshape(896, 1))
    labels_list = np.array(labels).reshape(1000)
    return inputs_list, labels_list


class NeuralNetwork:
    def __init__(self):
        self.weights = np.random.rand(896, 1)

    def __str__(self):
        return str(self.weights) + "\n" + str(self.weights.shape)

    def forward(self, inputs):
        return self.activation(np.dot(inputs.T, self.weights))

    def activation(self, output):
        return 1 / (1 + np.exp(-output))

    def train(self, inputs, labels, num):
        for i in range(1000):
            if labels[i] == num:
                l = 1
            else:
                l = 0
            errors = l - self.forward(inputs[i])
            # print(errors, labels[i], self.forward(inputs[i]), i)
            self.weights += np.dot(inputs[i], errors) * 10

    def save_weights(self, n):
        np.save(f'weights{n}.npy', self.weights)

    def load_weights(self):
        self.weights = np.load('weights.npy')

    def test(self, inputs, num, a=0.8):
        s = []
        correct = 0
        for i in range(0, 1000, 10):
            s.append(self.forward(inputs[i]))
            if self.forward(inputs[i]) < a and i // 100 != num - 1:
                correct += 1
            if self.forward(inputs[i]) > a and i // 100 == num - 1:
                correct += 1
        print(correct, 100)
        return s


if __name__ == '__main__':
    inputs, labels = load_inputs_and_labels()
    n = NeuralNetwork()
    for i in range(5):
        n.train(inputs, labels, 3)
    #n.save_weights(3)
    t = n.test(inputs, 3)
    for i in range(100):
        print(t[i], ' - ', i // 10 + 1)
