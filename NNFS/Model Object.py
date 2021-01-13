# Model class
class Model:

    def __init__(self):
        # Create a list of network objects
        self.layers = []
    # Add objects to the model
    def add(self, layer):
        self.layers.append(layer)
    # Set loss and optimizer
    def set(self, *, loss, optimizer):
        self.loss = loss
        self.optimizer = optimizer
    # Finalize the model
    def finalize(self):
        # Create and set the input layer
        self.input_layer = Layer_Input()
        # Count all the objects
        layer_count = len(self.layers)
        # Iterate the objects
        for i in range(layer_count):
            # If it's the first layer,
            # the previous layer object is the input layer
            if i == 0:
                self.layers[i].prev = self.input_layer
                self.layers[i].next = self.layers[i+1]
                # All layers except for the first and the last
            elif i < layer_count - 1:
                self.layers[i].prev = self.layers[i-1]
                self.layers[i].next = self.layers[i+1]
                # The last layer - the next object is the loss
            else:
                self.layers[i].prev = self.layers[i-1]
                self.layers[i].next = self.loss



    # Train the model
    def train(self, X, y, *, epochs=1, print_every=1):
        # Main training loop
        for epoch in range(1, epochs+1):
            # Perform the forward pass
            output = self.forward(X)
            # Temporary
            print(output)
            exit()
        # Performs forward pass
        def forward(self, X):
            # Call forward method on the input layer
            # this will set the output property that
            # the first layer in "prev" object is expecting
            self.input_layer.forward(X)
            # Call forward method of every object in a chain
            # Pass output of the previous object as a parameter
            for layer in self.layers:
                layer.forward(layer.prev.output)
            # "layer" is now the last object from the list,
            # return its output
            return layer.output

# Create dataset
X, y = sine_data()